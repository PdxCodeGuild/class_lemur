from flask import Flask, render_template, request, redirect
import json

from werkzeug.wrappers import response

app = Flask(__name__)

def import_json():
    with open("content.json", "r") as file:
        contents = json.load(file)
    return contents

def dump_json(contents):
    with open("content.json", "w") as file:
        json.dump({"posts": contents}, file)

@app.route('/', methods = ['GET', 'POST'])
def index():
    contents = import_json()
    contents = contents['posts']
    return render_template('index.html', contents=contents)

@app.route('/submit_blog/', methods = ['GET', 'POST'])
def submit_blog():
    if request.method == 'POST':
        contents = import_json()
        new_blog_dict = dict(request.form)
        contents = contents['posts']
        post_number = len(contents) + 1
        new_blog_dict['number'] = str(post_number)
        contents.append(new_blog_dict)
        dump_json(contents)
        return redirect('/')
    return render_template('/submit_blog.html')


app.run(debug=True)