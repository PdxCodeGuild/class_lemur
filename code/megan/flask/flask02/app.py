from os import RTLD_NODELETE
from flask import Flask, render_template, request


app = Flask(__name__) 

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/unit-converter/', methods=['GET', 'POST'])
def unit_converter():
    if request.method == 'POST':
        print('you did a POST request')
        print(request.form)
        data = dict(request.form)
        print(data)
        distance = int(data.get('distance'))
        units = data.get('units')

        conversions = {
        'feet': 0.3048,
        'miles': 1609.34,
        'meters': 1,
        'kilometers': 1000,
        'yards': 0.9144,
        'inches': 0.0254
        }

        choice = conversions[units]

        distance = float(distance)

        convert = distance * choice

        rounded = round(convert,2)

        return render_template('unit-converter.html', distance=distance, units=units, rounded=rounded)
    
    print('you did a GET request')
    return render_template('unit-converter.html')
    

@app.route('/anagram-checker/', methods=['GET', 'POST'])
def anagram_checker():
    if request.method == 'POST':
        print('you did a POST request')
        data = dict(request.form)

        first = data.get('first')
        second = data.get('second')

        first1 = sorted(first)
        second2 = sorted(second)

        first1 = ''.join(map(str, first1))
        second2 = ''.join(map(str, second2))
        
        if first1 == second2:
            anagram_check = "are anagrams!"
        else:
            anagram_check = "are not anagrams."

        return render_template('anagram-checker.html', first=first, second=second, anagram_check=anagram_check)

    print('you did a GET request')
    return render_template('anagram-checker.html')

app.run(debug=True)