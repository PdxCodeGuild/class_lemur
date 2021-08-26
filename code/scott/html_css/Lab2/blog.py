'''
Class Lemur - HTML CSS Lab 2
Scott Cormack
Python 3.9.6
'''

from flask import Flask, render_template

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)

