from flask import Flask, render_template
from random import choice
import string
from grading import compare_and_return_grades

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/grading/')
def grading():
    return render_template('grading.html')

@app.route('/grading/<int:user_score>/')
def grading_result(user_score):
    rival_score, user_grade, compare_result, rival_grade = compare_and_return_grades(user_score)
    return render_template('grading-result.html', user_score=user_score, user_grade=user_grade, compare_result=compare_result, rival_score=rival_score, rival_grade=rival_grade)


@app.route('/password-generator/')
def password_generator():
    return render_template('password-generator.html')

@app.route('/password-generator/<int:length>/')
def password_generator_result(length):
    all_letters = string.ascii_letters + string.digits + string.punctuation
    password_list = []
    for i in range(length):
        password_list.append(choice(all_letters))
    var1 = "".join(password_list)
    return render_template('password-generator-result.html', var1=var1)

@app.route('/emoticon-generator/')
# Random Emoticon Generator
# Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Assemble and display the emoticon
# You can find examples of emoticons here
def emoticon_generator():
    eyes_list = ['=', 'x','X','8',':']
    noses_list = ['-','o','c','','^']
    mouths_list = ['/','D',')',']','<','(','[']
    eye_choice = choice(eyes_list)
    nose_choice = choice(noses_list)
    mouth_choice = choice(mouths_list)
    emoticon = eye_choice+nose_choice+mouth_choice
    return render_template('emoticon-generator.html', emoticon=emoticon)

app.run(debug=True)

