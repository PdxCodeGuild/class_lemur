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

        distance = request.form.get('distance')
        units = request.form.get('units')

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

        return render_template('unit-converter.html', rounded=rounded)
    

@app.route('/anagram-checker/', methods=['GET', 'POST'])
def anagram_checker():
    if request.method == 'POST':
        print('you did a POST request')
        print(request.form)
        
        first = request.form.get('first')
        second = request.form.get('second')

        first = list(first)
        second = list(second)

        first.sort()
        second.sort()

        anagram_check = ...

        return render_template('anagram-checker.html', anagram_check=anagram_check)

    print('you did a GET request')
    return render_template('anagram-checker.html')

app.run(debug=True)