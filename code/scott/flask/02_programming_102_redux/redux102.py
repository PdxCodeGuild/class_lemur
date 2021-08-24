'''
Class Lemur, Programming 102 Redux
Scott Cormack
Python 3.9.6
'''
from flask import Flask, render_template, request

app = Flask(__name__)

# Home page view
@app.route('/')
def index():
    return render_template('index.html')

# Unit converter view
@app.route('/unit-converter/', methods=['GET','POST'])
def unit_converter():
    if request.method == 'POST':
        result = round(float(request.form.get('miles')) * 1.6093, 3)
        return render_template('unit-converter.html', result = result)
    return render_template('unit-converter.html')

@app.route('/user-login/', methods=['GET', 'POST'])
def user_login():
    details = {
        'username':'gandalfTheGrey',
        'pass':'noneShallPass!'
    }
    login = 'You must enter a username and password.' #Or True
    if request.method == 'POST':
        if request.form.get('username') == details['username'] and request.form.get('pass') == details['pass']:
            login = 'You have successfully logged in.'
            return render_template('user-login.html',login=login)
        else:
            login = 'Your username or password was not found.'
            return render_template('user-login.html',login=login)
    return render_template('user-login.html', login=login)
        
app.run(debug=True)        