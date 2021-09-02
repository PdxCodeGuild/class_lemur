import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html', blogs=read_blogs())

def read_blogs():
    with open('blog.json', 'r') as f:
        data = json.load(f)
        return data.get('blogs')
    
app.run(debug=True)