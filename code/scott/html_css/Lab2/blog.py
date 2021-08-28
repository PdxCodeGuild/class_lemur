'''
Class Lemur - HTML CSS Lab 2
Scott Cormack
Python 3.9.6
'''

from flask import Flask, render_template
import json

app = Flask(__name__)

# Read Json Posts
def read_posts():
    with open('static/posts.json', 'r') as f:
        data = json.load(f)
    return data.get('posts')

# Views
@app.route('/')
def index():
    return render_template('index.html', posts=read_posts())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/posts/')
def posts():
    return render_template('posts.html')

@app.route('/photos/')
def photos():
    return render_template('photos.html')

app.run(debug=True)

