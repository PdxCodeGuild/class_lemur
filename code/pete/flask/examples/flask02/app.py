from flask import Flask, render_template

app = Flask(__name__) # instantiate a Flask app

# localhost:5000/
@app.route('/') # this decorator is declaring the route for the following view function
def index(): # this is the index view function (aka: home page)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', colors=colors)

# localhost:5000/green localhost:5000/#00cc00
@app.route('/<color>/')
def color_view(color):
    return render_template('color.html', color=color)

app.run(debug=True)