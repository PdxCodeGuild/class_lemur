from flask import Flask, render_template, request
import json

app = Flask(__name__)

def read_posts():
    with open('posts.json', 'r') as f:
        data = json.load(f)

    return data.get('posts')


@app.route('/', methods=['GET'])
def index():

    posts = read_posts()
    return render_template('index.html', posts=posts)

app.run(debug=True)