import re
from flask import Flask
from random import choice

app = Flask(__name__)

@app.route('/') #it at th / route
def index(): # this is the index view
    return 'this is Flask'

@app.route('/colors/')
def colors():
    return 'RGB'

@app.route('/random-colors/')
def random_colors():
    colors = ['red', 'orange', 'blue', 'green', 'yellow']
    return choice.colors

print(index)