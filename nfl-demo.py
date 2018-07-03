from flask import Flask, render_template, request, redirect, url_for
from flask_sslify import SSLify
import random as rnd
import subprocess as subproc
import sys
import requests

from google.cloud import speech

def cloud_speech(data):
    client = speech.SpeechClient()

    audio = speech.types.RecognitionAudio(content=data)
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US'
    )

    response = client.recognize(config, audio)

    if response.results:
        print(response)
        return [None, response.results[0].alternatives[0].transcript]
    else:
        return ['Unable to transcribe audio', None]

    # for i, result in enumerate(response.results):
    #     alternative = result.alternatives[0]
    #     print('-' * 20)
    #     print('First alternative of result {}'.format(i))
    #     print('Transcript: {}'.format(alternative.transcript))

app = Flask(__name__)
sslify = SSLify(app)

def clean_label(unclean_label):
    return unclean_label.replace('__label__','').replace('_',' ').upper()

def proc_fasttext(in_text):
    cleaned_text = in_text.strip().lower()
    print('Requesting labels for "%s"' % (cleaned_text))

    try:
        r = requests.post('http://35.226.125.1:8085/nfl_vof_parse', json={'vof-text': cleaned_text}, timeout=5)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:",errc)
        return ['Error connecting to model. Please try again later.', None]
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:",errt)
        return ['Timeout connecting to model. Please try again later.', None]
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else",err)
        return ['Unknown error. Please try again later.', None]

    if (r.status_code == 200):
        data = r.json()
        print('Received %s from Parser' % (data))
        labels = data.get('parsed-list', ['FOOD 4', 'SAFETY 5'])
    else:
        print('Bad response from Parser %s. Faking it.' % (r.status_code))
        labels = ['__label__Food_3','__label__Team_10']
        if 'seats' in in_text:
            labels.append('seats_10')
        if 'usher' in in_text:
            labels.append('staff_8')
        if 'security' in in_text:
            labels.append('security_8')

    clean_labels = [clean_label(x) for x in labels]
    print(clean_labels)
    return [None, clean_labels]

@app.route('/', methods=['POST'])
def do_search() -> 'html':
    narrative = request.form['narrative']
    [error, labels] = proc_fasttext(narrative)
    print('Narrative: %s, labels: %s, error: %s' % (narrative, labels, error))
    return render_template('entry.html', the_query=narrative, the_match=labels, the_error=error)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html')

@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():
    data = request.get_data()
    print('Received audio data of length: %s' % (len(data)))
    [error, text] = cloud_speech(bytes(data))
    if error:
        return error, 500
    else:
        return text, 200

if __name__ == '__main__':
    rnd.seed()
    print('Starting MAIN:')
    app.run('0.0.0.0', 8080)
