from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def read_contacts():
    with open('contacts.json', 'r') as f:
        data = json.load(f)

    return data.get('contacts')

def write_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump({'contacts': contacts}, f)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contacts = read_contacts()

        info = dict(request.form)
        
        contacts.append(info)

        write_contacts(contacts)
        return redirect('/')

    contacts = read_contacts()
    return render_template('index.html', contacts=contacts)
    

@app.route('/<name>/')
def detail(name):

    contacts = read_contacts()

    return render_template('detail.html', contacts=contacts, name=name)


app.run(debug=True)
