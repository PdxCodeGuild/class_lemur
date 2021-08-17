from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route('/')#it's at the / route
def index(): #this is the index view
    return render_template('index.html')

@app.route('/emoticon-generator/')
def emoticon_generator():
    # emoticon='???'
    eyes  = [':', ';', '8', '=']
    nose = ['-', 'o', '>', '*']
    mouth = ['c', '@', '(', ')']
    emoticon = choice(eyes) + choice(nose) + choice(mouth)
    return render_template('emoticon-generator.html', emoticon=emoticon)

@app.route('/guess-the-number/')
def guess_the_number():
    return "Enter a number into the url bar(i.e.: 127.0.0.1:5000/5"
#     number = choice(range(1,10))
#     guess = int(input("Guess a number between 1 and 10: "))

#     return render_template('guess-the-number.html', guess = guess)

@app.route('/guess-the-number/<int:guess>/')
def guess_the_number_guess(guess):
    number = choice(range(1,10))
    if guess == number:
        guess_result = "Correct"
    else:
        guess_result =("Guess is incorrect. Try again")
        # guess_result = 'low'
        return render_template('guess-the-number-guess.html', guess=guess, guess_result = guess_result)

app.run(debug=True)
