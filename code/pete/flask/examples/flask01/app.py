from flask import Flask, render_template, request
from random import choice, sample

app = Flask(__name__)

@app.route('/') # it's at the / route
def index(): # this is the index view
    return render_template('index.html')

@app.route('/colors/')
def colors():
    return "Red, Green, & Blue"

@app.route('/random-color/', methods=['GET', 'POST'])
def random_color():
    if request.method == 'POST':
        return 'you did a post request'
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    color = choice(colors)
    return render_template('random-color.html', color=color)

@app.route('/random-colors/<int:number>/')
def random_colors(number):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    colors = sample(colors, number)
    return str(colors)

app.run(debug=True)