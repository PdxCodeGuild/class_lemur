from flask import Flask, render_template
from random import choice
app = Flask(__name__)

colors=['red','green','blue','orange','indoio','purple']

@app.route('/')
def index(): # this is the index
    return render_template('index.html')

@app.route('/colors/')
def colors():
    return "red, Green, & Blue"

@app.route('random-color/')
def random_color(colors=colors):
    color = choice(colors)
    return render_template('random-color.html', color=color)

app.route('random-colors/<int:number>/')
def random_colors(number, colors=colors):
    rancolors=sample(colors, number)
    return str(number)

app.run(debug=True)

