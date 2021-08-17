from flask import Flask, render_template
from random import choice
app = Flask(__name__)

@app.route('/')
def index(): # this is the index
    return render_template('index.html')

@app.route('/colors/')
def colors():
    return "red, Green, & Blue"

@app.route('random-color/')
def random_color():
    colors=['red','green','blue','orange']
    color = choice(colors)
    return render_template('random-color.html', color=color)


app.run(debug=True)

