


from flask import Flask, render_template, request
import json
from markupsafe import Markup


app = Flask(__name__)
#Storage file
file1='templates/data.json'

def read_posts():
    with open(file1, 'r') as file:
        jfile=json.loads(file.read())
    posts=jfile['posts']
    return posts

#Write back to JSON as dict
def write_posts(posts):
    jfile={'posts': posts}
    with open(file1, 'w') as file:
        file.write(json.dumps(jfile, indent=4))

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Sent a GET request, this view lists all of the posts.
    Sent a POST request, this view adds a new post to the
    json file, and redirects back to the same view with a GET request
    """   
    if request.method == 'POST':
        posts=read_posts()
        # extract new brand data from request.form
        while request.form != posts:
            posts.append(dict(request.form))
        posts=sorted(posts, key=lambda i:i['Brand'])
        print(posts)
        
        # add new brand dictionary to brands list
        write_posts(posts)
        # car_data = pd.DataFrame(brands).style 
        # car_data=car_data.hide_index() 
        # cars=Markup(car_data.to_html(table_uuid='panda'))
        # return render_template('index.html', cars=cars) # redirect back to the same view, as a GET request
    posts=read_posts()
    
    # render index template, passing brands list as a context kwarg
    # print(car_data)
    return render_template('index.html', posts=posts)