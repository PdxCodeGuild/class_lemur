from flask import Flask, render_template
import random
import string
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/password-generator/')
def password_generator():
    characters = string.printable
    password = ''
    while len(password) < 9:
        password += random.choice(characters)
    return render_template('password-generator.html', password=password)


@app.route('/grading/<int:number>/')
def grading(number):
    grade = number
    rival_grade = random.randint(1, 100)
    rival_letter_grade = ''
    letter_grade = ''
    message = ''
    if grade > 89:
        letter_grade = 'A'
    elif grade > 79:
        letter_grade = 'B'
    elif grade > 69:
        letter_grade = 'C'
    elif grade > 59:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    if rival_grade >= 90:
        rival_letter_grade = 'A'
    elif rival_grade >= 80:
        rival_letter_grade = 'B'
    elif rival_grade >= 70:
        rival_letter_grade = 'C'
    elif rival_grade >= 60:
        rival_letter_grade = 'D'
    else:
        rival_letter_grade = 'F'
    if grade > rival_grade:
        message = 'You did better then your rival!'
    else:
        message = 'Your rival did better then you.'
    if grade % 10 <= 3 and grade > 60:
        letter_grade += '-'
    elif grade % 10 >= 7 and grade > 60:
        letter_grade += '+'
    if rival_grade % 10 <= 3 and rival_grade > 60:
        rival_letter_grade += '-'
    elif rival_grade % 10 >= 7 and rival_grade > 60:
        rival_letter_grade += '+'

    return render_template('grading.html', message=message, grade=grade, rival_grade=rival_grade, letter_grade=letter_grade, rival_letter_grade=rival_letter_grade)


app.run(debug=True)
