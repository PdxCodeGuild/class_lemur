from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    return render_template(index.html) #pulling from another file. file not made, hence 

@app.route('/<color>/')
def color_view(color):
    return render_template('color.html', color=color)
app.run(debug=True)