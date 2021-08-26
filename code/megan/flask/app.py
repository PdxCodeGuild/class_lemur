from flask import Flask, render_template
import random 
import string

app = Flask(__name__) 

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/password-generator/<password>')
def password_generator(password): 
    alphabet = string.ascii_letters 
    digits = string.digits
    punctuation = string.punctuation

    all = alphabet + digits + punctuation

    control = 0 
    user_password = []


    while control < 10:
        char = random.choice(all)
        total = user_password.append(char)
        final = ''.join(map(str, user_password))

        control += 1

    output_password = final
    return render_template('password-generator.html', html_password=output_password)


@app.route('/grading/<grade>')
def grading(grade):

    localhost:5000/grading/88
    return render_template('grading.html', html_grade=grade)

app.run(debug=True)