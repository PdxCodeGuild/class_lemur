from flask import Flask, render_template
from random import choice

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

@app.route('/guess-the-number/')
def guess_the_number():
    return render_template('guess-the-number.html')

@app.route('/guess-the-number/<int:guess>/')
def guess_the_number_guess(guess):
        guess_result = 'low'
        return render_template('guess-the-number-guess.html', guess_result=guess_result)
app.run(debug=True)



