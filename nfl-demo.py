from flask import Flask, render_template, request, redirect, url_for
import random as rnd
import subprocess as subproc
import sys

app = Flask(__name__)

global narrative, label

def clean_label(unclean_label):
    return unclean_label.replace('__label__','').replace('_',' ').upper()

def proc_fasttext(in_text):
    ft_in_file = 'temp.buffer'
    cleaned_text = in_text.strip().lower()
    sentences_text = cleaned_text.split('.')
    with open(ft_in_file,'w') as fwrite:
        #fwrite.write('the fries were cold')
        for sentence in sentences_text:
            if len(sentence) > 3:
                fwrite.write(sentence+'\n')
    # PLACEHOLDER FOR TEXT PARSER THAT RETURNS LIST OF LABELS AND SCORES
    dlist = ['__label__Food_3','__label__Team_10', 'parking', 'seats', 'directions']
    clean_labels = [clean_label(d) for d in dlist]
    print(clean_labels)
    return clean_labels

@app.route('/nflParser', methods=['POST'])
def do_search() -> 'html':
    global narrative, label
    narrative = request.form['narrative'] 
    print('nflParser:',narrative, label)
    #label = 'DUMMY VARIABLE.'
    labels = proc_fasttext(narrative)
    return render_template('entry.html',
                           the_query=narrative,
                           the_match=labels)

@app.route('/nflParser', methods=['GET'])
def back_to_home():
    return redirect('/')

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    global narrative, label
    print('ENTRY:',narrative, label)
    return render_template('entry.html')

if __name__ == '__main__':
    rnd.seed()
    global narrative, label
    narrative='AWAITING INPUT'
    label='AWAITING INPUT'
    print('MAIN:',narrative,label)
    app.run('0.0.0.0', 8085)

