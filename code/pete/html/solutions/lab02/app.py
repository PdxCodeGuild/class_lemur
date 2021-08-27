from flask import Flask, render_template
import json
from random import randint

app = Flask(__name__)

"""Auxillary Functions"""
def read_posts():
    """
Reads the contents of posts.json and returns the list of posts
    """
    with open('posts.json', 'r') as f:
        data = json.load(f)
    return data.get('posts')

def write_posts(posts):
    """
Passed a list of posts, writes those posts to the json file
    """
    with open('posts.json', 'w') as f:
        json.dump({'posts': posts}, f)


"""Flask Views"""
@app.route('/')
def index():
    posts = read_posts()
    for post in posts:
        w = 600 + randint(-10, 10)
        h = 300 + randint(-10, 10)
        post['cat_photo'] = f'https://placekitten.com/{w}/{h}/'
    return render_template('index.html', posts=posts)

app.run(debug=True)
