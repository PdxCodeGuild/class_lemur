from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'

db = SQLAlchemy(app)
class contacts(db.Model):
    name = db.Column('Name', db.String(50), primary_key=True)
    fruit = db.Column('Favorite_Fruit', db.String(50))
    color = db.Column('Favorite_Color', db.String(50))

    def __init__(self, name, fruit, color):
        self.name = name
        self.fruit = fruit
        self.color = color

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_contact = contacts(request.form['Name'], request.form['Favorite_Fruit'], request.form['Favorite_Color'])
        db.session.add(new_contact)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', contacts = contacts.query.all())

@app.route('/<name>/')
def detail(name):
    return render_template('detail.html', contact=contacts.query.get(name))

@app.route('/<name>/update/', methods=['POST'])
def update(name):
    contact = contacts.query.get(name)
    if request.form.get('Name') != '':
        contact.name = request.form.get('Name')
    if request.form.get('Favorite_Fruit') != '':
        contact.fruit = request.form.get('Favorite_Fruit')
    if request.form.get('Favorite_Color') != '':
        contact.color = request.form.get('Favorite_Color')
    db.session.commit()
    return redirect(f'/{contact.name}/')

@app.route('/<name>/delete/', methods=['GET','POST'])
def delete(name):
    contacts.query.filter_by(name=name).delete()
    db.session.commit()
    return redirect('/')

app.run(debug=True)