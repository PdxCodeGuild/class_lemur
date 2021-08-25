from flask import Flask, render_template

app = Flask(__name__)

people = [
    {'name': 'pete', 'job': 'instuctor'},
    {'name': 'lisa', 'job': 'ta'},
    {'name': 'david', 'job': 'student'},
]

@app.route('/')
def index():
    return render_template('index.html', people=people)
    # message = ''
    # for person in people:
    #     message += f"{person['name']} is a {person['job']}"
    # return message

app.run(debug=True)