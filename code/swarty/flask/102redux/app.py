from flask import Flask, render_template, request, redirect
from random import choice, sample, shuffle
import string
import decimal as dec

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
        unit_out=inputs['unit_out']
        distance = round(float(inputs['distance']) *units[inputs['unit_in']] / units[inputs['unit_out']],2)
    return render_template('unit.html', distance=distance, unit=unit_out)

@app.route('/anagram/',methods=['GET', 'POST'])
def anagram():
    if request.method == 'POST':
        inputs=dict(request.form)
        print(inputs)
        firststr=inputs['first'].lower()
        secondstr=inputs['second'].lower()
        print(firststr,secondstr)
        first=list(firststr)
        second=list(secondstr)
        print(first)
        print(second)
        first.sort()
        second.sort()
        if first == second:
            response=f'{firststr} and {secondstr} are anagrams'
        else:
            response=f'{firststr} and {secondstr} are not anagrams'
    return render_template('anagram.html',words=response)

    



app.run(debug=True)
