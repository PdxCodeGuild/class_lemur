'''
Class Lemur, CSV Redux
Scott Cormack
Python 3.9.6
'''
import json
from flask import Flask, render_template, request

def read_json():
    with open('smite_characters.json', 'r') as f:
        data = json.load(f)
    return data.get('characters')

def write_json():
    with open('file_name1.json') as f:
        json.dump({})

app = Flask(__name__)

# Home page view
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        characters = read_json()
        write_json(characters)
    characters = read_json()
    return render_template('index.html', characters=characters)

app.run(debug=True)