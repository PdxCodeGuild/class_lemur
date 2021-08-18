from flask import Flask, render_template, request
from random import choice, sample, shuffle
import string

app = Flask(__name__)

units = {
    'm' : 1,
    'ft' : .3048,
    'mi' : 1609.34,
    'km' : 1000,
    'yd' : .9144,
    'in' : .0254
}

@app.route('/')
def index(): # this is the index
    return render_template('index.html')


@app.route('/unit-converter/',methods=['GET', 'POST'])
def unit_converter():
    if request.method == 'POST':
        inputs=dict(request.form)
        print(inputs)
        distance = float(inputs['distance']) *units[inputs['unit_in']] / units[inputs['unit_out']]
    return render_template('index.html', distance=distance)


    



app.run(debug=True)
