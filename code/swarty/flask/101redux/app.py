from flask import Flask, render_template, request
from random import choice, sample
import string

app = Flask(__name__)

@app.route('/')
def index(): # this is the index
    return render_template('index.html')

@app.route('/random-pswd/', methods=['GET', 'POST'])
def random_color():
    if request.method == 'POST':
        return 'you did a post request'
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)
    

    password=
    return render_template('random-pswd.html', password=pswd)


app.run(debug=True)
