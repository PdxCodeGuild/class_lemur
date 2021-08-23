from flask import Flask, render_template, request
from login_func import login

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/unit-converter/',  methods=['GET', 'POST'])
def unit_converter():
    conversions = {'feet': 0.3048, 'meters': 1, 'yard': 0.9144,
                   'inch': 0.0254, 'miles': 1609.34, 'kilometers': 1000}
    if request.method == 'POST':
        distance1 = int(request.form.get('distance'))
        starting_unit = request.form.get('starting_unit')
        ending_unit = request.form.get('ending_unit')
        distance2 = distance1 * conversions[starting_unit]
        distance3 = round(distance2 / conversions[ending_unit], 4)
        return render_template('unit-converter.html', starting_unit=starting_unit, ending_unit=ending_unit, distance1=distance1, distance3=distance3)
    return render_template('unit-converter.html')


@app.route('/anagram-checker/', methods=['GET', 'POST'])
def anagram_checker():
    if request.method == 'POST':
        word1 = (request.form.get('word1')).lower()
        word2 = (request.form.get('word2')).lower()
        word1_list = list(word1).sort()
        word2_list = list(word2).sort()
        if word1_list == word2_list:
            message = f'{word1} is an anagram of {word2}'
        else:
            message = f'{word1} is not an anagram of {word2}'
        return render_template('anagram-checker.html', word1=word1, word2=word2, message=message)
    return render_template('anagram-checker.html')


@app.route('/user-login/', methods=['GET', 'POST'])
def user_login():
    profile = [
        {'username': 'bilbo',
         'password': 'baggins'},
        {'username': 'gandalf',
         'password': 'thegrey'}
    ]
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        for dictionary in profile:
            if login(username, password, dictionary):
                message = f'Welcome! {dictionary["username"]}'
                break
        if not login(username, password, dictionary):
            message = f'username or password incorrect'

        return render_template('user-login.html', message=message)

    return render_template('user-login.html')


app.run(debug=True)
