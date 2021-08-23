import json
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

def read_contacts():
    """Reads the contents of contacts.json and returns the list of contacts"""
    with open("contacts.json", 'r') as file:
        data = json.load(file)
    return data.get('contacts')

def write_contacts(contacts):
    """Passed a list of cities, writes those cities to the json file"""
    with open("contacts.json", "w") as file:
        json.dump({"contacts": contacts}, file)

def return_contact(contacts, name):
    for contact in contacts:
        if contact['Name'] == name:
            return contact

# 127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def index():
    """
Sent a GET request, this view lists all of the cities.
Sent a POST request, this view adds a new city to the
json file, and redirects back to the same view with a GET request
    """
    if request.method == 'POST':
        contacts = read_contacts() # read cities from json file
        new_contact = dict(request.form)
        contacts.append(new_contact)
        write_contacts(contacts) # write updated cities to json file
        return redirect('/') # redirect back to the same view, as a GET request
    contacts = read_contacts() # read cities from json file
    # render index template, passing cities list as a context kwarg
    return render_template('index.html', contacts=contacts)

@app.route('/<name>/', methods=['GET', 'POST'])
def detail(name):
    contacts = read_contacts()
    contact = return_contact(contacts, name)
    return render_template('detail.html', contact=contact)

@app.route('/<name>/update/', methods=['POST'])
def update(name):
    # extract data from form
    contacts = read_contacts()
    contact_update = dict(request.form)
    for contact in contacts:
        if contact['Name'] == name:
            for k,v in contact_update.items():
                if v != '':
                    contact[k] = v
            name = contact.get('Name')
    # update city in list of dictionaries
    write_contacts(contacts)
    return redirect(f'/{name}/')


@app.route('/<name>/delete/', methods=['POST'])
def delete(name):
    contacts = read_contacts()
    for i, contact in enumerate(contacts):
        if contact['Name'] == name:
            contacts.pop(i)
    write_contacts(contacts)
    return redirect('/')

app.run(debug=True)

