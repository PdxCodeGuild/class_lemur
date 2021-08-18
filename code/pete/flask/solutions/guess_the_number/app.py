from flask import Flask, render_template
from random import randint

app = Flask(__name__)

# normal difficulty num
num = randint(1, 10)

# hard mode num
RANGE = 1000
hard_mode_num = randint(1, RANGE)

# 127.0.0.1:5000/
@app.route('/')
def index():
    global num
    return render_template('index.html', num=num)

# 127.0.0.1:5000/4
@app.route('/<int:guess_num>/')
def guess(guess_num):
    global num
    if guess_num < num:
        result = 'low'
    elif guess_num > num:
        result = 'high'
    else:
        result = 'correct'
        num = randint(1, 10)
    return render_template('index.html', num=num, guess_num=guess_num, result=result)

# localhost:5000/hard-mode/
@app.route('/hard-mode/')
def hard_mode():
    global RANGE
    nums = range(1, RANGE + 1)
    return render_template('hard-mode.html', nums=nums, range=RANGE)

@app.route('/hard-mode/<int:guess_num>/')
def hard_mode_guess(guess_num):
    global hard_mode_num
    global RANGE
    nums = range(1, RANGE + 1)
    if guess_num < hard_mode_num:
        result = 'low'
    elif guess_num > hard_mode_num:
        result = 'high'
    else:
        result = 'correct'
        hard_mode_num = randint(1, 10)
    return render_template('hard-mode.html', nums=nums, range=RANGE, guess_num=guess_num, result=result)

app.run(debug=True)
