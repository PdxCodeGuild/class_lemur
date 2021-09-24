'''
flask lab 1
upload programming101 labs using flask
'''

from flask import Flask, render_template
import string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password-gen/')
def password_gen():
    length = 8
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    pw = letters + numbers + symbols
    pw2 = ''

    while length > 0:
        pw2 += random.choice(pw)
        length = length - 1

    return render_template('password_gen.html', pword=pw2)

app.run(debug=True)