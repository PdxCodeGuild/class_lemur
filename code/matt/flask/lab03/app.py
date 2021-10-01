import json
from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)


def read_characters():
    with open('characters.json', 'r') as f:
        data = json.load(f)
    return data.get('characters')


def write_characters(characters):
    with open('characters.json', 'w') as f:
        json.dump({'characters': characters}, f)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('POST')
        characters = read_characters()
        name = request.form.get("name")
        race = request.form.get("race")
        clas = request.form.get("class")
        background = request.form.get("background")
        character = {"name": name,
                     "race": race,
                     "class": clas,
                     "background": background}
        characters.append(character)
        write_characters(characters)
        return redirect('/')
    print('GET')
    characters = read_characters()
    return render_template('index.html', characters=characters)


@app.route('/<name>/')
def detail(name):
    characters = read_characters()
    for character in characters:
        if character['name'] == name:
            characters = character
    return render_template('detail.html', characters=characters)


@app.route('/<name>/update', methods=['POST'])
def update(name):
    characters = read_characters()
    for character in characters:
        if character['name'] == name:
            if request.method == 'POST':
                character['name'] = request.form.get("new_name")
                character['race'] = request.form.get("new_race")
                character['class'] = request.form.get("new_class")
                character['background'] = request.form.get("new_background")
                name = character['name']
                write_characters(characters)
    return redirect(f'/{name}/')


@app.route('/<name>/delete', methods=['POST'])
def delete(name):
    characters = read_characters()
    for character in characters:
        if character['name'] == name:
            characters.remove(character)
            write_characters(characters)
    return redirect('/')


app.run(debug=True)
