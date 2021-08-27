'''
Class Lemur, Programming 101 Redux
Scott Cormack
Python 3.9.6
'''
from flask import Flask, render_template
import random
import string

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return render_template('index.html')

# Password Generator view
@app.route('/password-generator/')
def password_generator():
    chars = string.ascii_letters + string.punctuation + string.digits
    result = ''.join(random.sample(chars, 10))
    return render_template('page.html', result = result)

# Magic 8 Ball View
@app.route('/magic-8-ball/')
def magic_8_ball():
    choices = ['Yes', 'No', 'Maybe', 'Ask Again']
    result = random.choice(choices)
    return render_template('page.html', result = result)

# Random Emoticon Generator
@app.route('/random-emoticon/')
def random_emoticon():
    eyes = [':','8',';','@']
    noses = ['>','^']
    mouths = ['S','D',')','P','/','O']
    result = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    return render_template('page.html', result = result)

app.run(debug=True)
