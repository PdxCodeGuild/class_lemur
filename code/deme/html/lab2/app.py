import json
from flask import Flask, render_template

app = Flask(__name__)
def read_json():
    with open('blog.json', 'r') as f:
        data = json.load(f)
    return data.get('blog')

def write_posts(blog):
    with open('blog.json', 'w') as f:
        json.dump({'blog': blog}, f)


@app.route('/')
def index():
    blog = read_json()
    return render_template('index.html', blog = blog)

app.run(debug=True)
