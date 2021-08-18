'''
flask 2 lab
incorporate user input from 102 lab
*User Login*
'''

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/login/', methods= ['GET', 'POST'])
def login(name, word):
    if request.METHOD == 'POST':
        if name != dict['username']:
            return redirect('/login/failure')
        if word != dict['password']:
            return redirect('/login/failure')
        else:
            return redirect('/login/success')

