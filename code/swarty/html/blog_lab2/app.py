


from flask import Flask, render_template, request
import json
from markupsafe import Markup


app = Flask(__name__)
#Storage file
file1='templates/data.json'

def read_posts():
    with open(file1, 'r') as file:
        posts=json.load(file)
    return posts.get('posts')

#Write back to JSON as dict
def write_posts(posts):
    with open(posts.json, 'w') as file:
        json.dump({'posts': posts}, file)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Sent a GET request, this view lists all of the posts.
    Sent a POST request, this view adds a new post to the
    json file, and redirects back to the same view with a GET request
    """   
    if request.method == 'POST':
        posts=read_posts()
        # get new post from page and add to dictionary of posts.
        while request.form != posts:
            posts.append(dict(request.form))
        #posts=sorted(posts, key=lambda i:i['date'])
        print(posts)
        
        # write new post dictionary to posts
        write_posts(posts)
    posts=read_posts()
    # render index template, passing blog post list as a context kwarg
    # print(posts)
    return render_template('index.html', posts=posts)



app.run(debug=True)