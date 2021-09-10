from os import name
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        form = dict(request.form)

        return render_template('confirmation.html', form=form)
    return render_template('index.html')


@app.route('/confirmation/<confirmation_data>/')
def confirmation(confirmation_data):
    ...


app.run(debug=True)
