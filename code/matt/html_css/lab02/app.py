import json
from os import name
from flask import Flask, render_template, request
from werkzeug.utils import redirect


app = Flask(__name__)


def read_characters(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data.get('characters')


@app.route('/')
def index():
    characters = read_characters('valhalla.json')
    return render_template('index.html', characters=characters)


@app.route('/<name>/')
def update(name):
    characters = read_characters(name)
    return render_template('index.html', characters=characters)


app.run(debug=True)
