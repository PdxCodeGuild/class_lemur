from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/password-generator/', methods=['GET', 'POST'])
def password_generator():
    letter = string.ascii_letters
    num = string.digits
    punc = string.punctuation
    if request.method == 'POST':
        letters = int(request.form.get('letters'))
        numbers = int(request.form.get('numbers'))
        punctuation = int(request.form.get('punctuation'))
        password = []
        for x in range(letters):
            password.append(random.choice(letter))
        for x in range(numbers):
            password.append(random.choice(num))
        for x in range(punctuation):
            password.append(random.choice(punc))
        random.shuffle(password)
        new_password = ''.join(password)
        return render_template('password-generator.html', new_password=new_password)
    return render_template('password-generator.html')


@app.route('/grading/', methods=['GET', 'POST'])
def grading():
    if request.method == 'POST':
        grade = int(request.form.get('grade'))
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
        elif grade < rival_grade:
            message = 'Your rival did better then you.'
        elif grade == rival_grade:
            message = 'You tied with your rival.'
        if grade == 100:
            letter_grade += '+'
        elif grade % 10 <= 3 and grade > 60:
            letter_grade += '-'
        elif grade % 10 >= 7 and grade > 60:
            letter_grade += '+'
        if grade == 100:
            rival_letter_grade += '+'
        elif rival_grade % 10 <= 3 and rival_grade > 60:
            rival_letter_grade += '-'
        elif rival_grade % 10 >= 7 and rival_grade > 60:
            rival_letter_grade += '+'

        return render_template('grading.html', message=message, grade=grade, rival_grade=rival_grade, letter_grade=letter_grade, rival_letter_grade=rival_letter_grade)
    return render_template('grading.html')


app.run(debug=True)
