import random
from flask import Flask, render_template, request
from random import choice, randint

app = Flask(__name__)

@app.route('/')#it's at the / route
def index(): #this is the index view
    return render_template('index.html')

@app.route('/emoticon-generator/')
def emoticon_generator():
    emoticon='???'
    eyes  = [':', ';', '8', '=']
    nose = ['-', 'o', '>', '*']
    mouth = ['c', '@', '(', ')']
    emoticon = choice(eyes) + choice(nose) + choice(mouth)
    return render_template('emoticon-generator.html', emoticon=emoticon)

# @app.route('/guess-the-number/')
# def guess_the_number():
#     randNumber = random.randint(1, 10)
#     if request.method == 'POST':
#         meters = float(request.form.get('feet')) * 0.3048
    
#     return render_template('guess-the-number.html')

# @app.route('/guess-the-number/<int:guess>/')

# def guess_the_number_guess(guess):
#         guess_result = 'low'
#         return render_template('guess-the-number-guess.html', guess_result=guess_result)
# app.run(debug=True)
@app.route('/guess-the-number/', methods=['GET','POST'])
def guess_the_number():
    num = random.randint(1,10)
    if request.method == 'POST':
        guess = int(request.form.get('guess'))
        if guess > num:
            guess_result = "Too High"
        if guess < num:
            guess_result = "Too Low"
        if guess == num:
            guess_result = "Correct"
        return render_template('guess-the-number.html',  guess = guess, num = num, guess_result = guess_result)
    return render_template('guess-the-number.html')



