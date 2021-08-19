from flask import Flask, render_template, request
from random import choice, sample, shuffle
import string

app = Flask(__name__)

@app.route('/')
def index(): # this is the index
    return render_template('index.html')

@app.route('/random-pswd/')
def random_color():
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)
    all=list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
    pswd=''
    shuffle(all)
    for i in range(10):
        pswd+=all[i]
    return render_template('random-pswd.html', password=pswd)

@app.route('/grading/', methods=['GET', 'POST'])
def grades():
    if request.method == 'POST':
        numgrade = (request.form['input_text'])
        if numgrade >=90:
            ltrgrade='A'
        elif numgrade >=80:
            ltrgrade='B'
        elif numgrade >=70:
            ltrgrade='C'
        elif numgrade >=60:
            ltrgrade='D'
        else:
            ltrgrade='F'
    else:
        ltrgrade=''
    return render_template('grading.html',grade=ltrgrade)



app.run(debug=True)
