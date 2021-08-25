from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def import_json():
    with open("content.json", "r") as file:
        contents = json.load(file)
    return contents

@app.route('/', methods = ['GET', 'POST'])
def index():
    contents = import_json()
    contents = contents['posts']
    return render_template('index.html', contents=contents)

app.run(debug=True)