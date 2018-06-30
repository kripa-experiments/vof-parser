from flask import Flask, render_template, request
import random as rnd
import subprocess as subproc
import sys

app = Flask(__name__)

global narrative, label

def procFastText(in_text):
    ft_in_file = 'temp.buffer'
    cleaned_text = in_text.strip().lower()
    sentences_text = cleaned_text.split('.')
    with open(ft_in_file,'w') as fwrite:
        #fwrite.write('the fries were cold')
        for sentence in sentences_text:
            if len(sentence) > 3:
                fwrite.write(sentence+'\n')
    # PLACEHOLDER FOR TEXT PARSER THAT RETURNS LIST OF LABELS AND SCORES
    dlist = ['__label__Food_3','__label__Team_10']
    clean_ds = ''
    for d in dlist:
        newline = ';\r\n'
        clean_ds = clean_ds + d.replace('__label__','').replace('_',' ').upper() + newline
    print(clean_ds)
    return clean_ds

@app.route('/nflParser', methods=['POST'])
def do_search() -> 'html':
    global narrative, label
    narrative = request.form['narrative'] 
    # TODO: error handling around empty?
    print('nflParser:',narrative, label)
    #label = 'DUMMY VARIABLE.'
    label = procFastText(narrative)
    return render_template('results.html',
                           the_query=narrative,
                           the_match=label)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    global narrative, label
    print('ENTRY:',narrative, label)
    return render_template('entry.html')

@app.route('/retry', methods=['POST'])
def retry_page() -> 'html':
    global narrative, label
    print('RETRY:',narrative, label)

    return render_template('entry.html')

if __name__ == '__main__':
    rnd.seed()
    global narrative, label
    narrative='AWAITING INPUT'
    label='AWAITING INPUT'
    print('MAIN:',narrative,label)
    app.run('0.0.0.0', 8085)

