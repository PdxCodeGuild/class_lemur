from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/anagram/')
def anagram():
    return render_template('anagram.html')


@app.route('/anagram/', methods=['POST']) 
def anagram_check():
    word_one = request.form.get("word_one").lower()
    word_two = request.form.get("word_two").lower()
    word_one_list = sorted(list(word_one.strip(' ')))
    word_two_list = sorted(list(word_two.strip(' ')))
    if word_one_list == word_two_list:
        anagram_check = True
    else:
        anagram_check = False
    return render_template('anagram.html', word_one=word_one, word_two=word_two, anagram_check=anagram_check)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    profile = {"user_name": "mark", "user_password": "babygoats"}
    if request.method == 'POST':
        username = request.form.get('user_name')
        password = request.form.get('user_password')
        if username == profile['user_name'] and password == profile['user_password']:
            result = f"Login in successful.  Welcome {username.capitalize()}."
            return render_template('index.html', result=result)

        else:
            result = "Unsuccessful Attempt.  Please try again."
        return render_template('login.html', result=result)
    return render_template('login.html')

@app.route('/unit-converter/')
def unit_converter():
    return render_template('unit-converter.html')

@app.route('/unit-converter/feet/', methods=['POST'])
def unit_converter_feet():
    if request.method == 'POST':
        number_in_feet = float(request.form.get('feet'))
        feet_meters = number_in_feet * .3048
        return render_template('unit-converter.html', feet_meters=feet_meters)
    return render_template('unit-converter.html')

@app.route('/unit-converter/miles/', methods=['POST'])
def unit_converter_miles():
    if request.method == 'POST':
        number_in_feet = float(request.form.get('miles'))
        miles_meters = number_in_feet * 1609.34
        return render_template('unit-converter.html', miles_meters=miles_meters)
    return render_template('unit-converter.html')

@app.route('/unit-converter/meters/', methods=['POST'])
def unit_converter_meters():
    if request.method == 'POST':
        number_in_feet = float(request.form.get('meters'))
        meters_meters = number_in_feet * 1
        return render_template('unit-converter.html', meters_meters=meters_meters)
    return render_template('unit-converter.html')

@app.route('/unit-converter/kilometers/', methods=['POST'])
def unit_converter_kilometers():
    if request.method == 'POST':
        number_in_feet = float(request.form.get('kilometers'))
        feet_meters = number_in_feet * 1000
        return render_template('unit-converter.html', km_meters=feet_meters)
    return render_template('unit-converter.html')


app.run(debug=True)
