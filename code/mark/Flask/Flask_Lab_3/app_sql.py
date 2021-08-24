import sqlite3
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

def open_connection():
    conn = sqlite3.connect('contacts.db')
    return conn

def dict_factory(cursor, row):
    return_dict = {}
    for i, column in enumerate(cursor.description):
        return_dict[column[0]] = row[i]
    return return_dict

def read_contacts_sql():
    con = open_connection()
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    results = cur.fetchall()
    con.close()
    return results

def write_contacts_sql(contact_info):
    con = open_connection()
    sql = '''INSERT INTO contacts(
        Name,
        Favorite_Fruit,
        Favorite_Color)
        VALUES(?,?,?)
        '''
    cur = con.cursor()
    cur.execute(sql, contact_info)
    con.commit()
    con.close()

def update_contacts(contact_info):
    con = open_connection()
    sql = '''UPDATE contacts 
            SET Name = ?,
            Favorite_Fruit = ?,
            Favorite_Color = ?
            WHERE Name = ?'''
    cur = con.cursor()
    cur.execute(sql, contact_info)
    con.commit()
    con.close()

def delete_contact(name):
    con = open_connection()
    sql = f'DELETE FROM contacts WHERE Name=?'
    cur = con.cursor()
    cur.execute(sql, (name,))
    con.commit()
    con.close()


def return_contact(contacts, name):
    for contact in contacts:
        if contact['Name'] == name:
            return contact

# 127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contacts = read_contacts_sql()
        new_contact = dict(request.form)
        contact_values = list(new_contact.values())
        write_contacts_sql(contact_values)
        return redirect('/') 
    contacts = read_contacts_sql()
  
    return render_template('index.html', contacts=contacts)

@app.route('/<name>/', methods=['GET', 'POST'])
def detail(name):
    contacts = read_contacts_sql()
    contact = return_contact(contacts, name)
    return render_template('detail.html', contact=contact)

@app.route('/<name>/update/', methods=['POST'])
def update(name):
    contacts = read_contacts_sql()
    contact_update = dict(request.form)
    for contact in contacts:
        if contact['Name'] == name:
            for k,v in contact_update.items():
                if v != '':
                    contact[k] = v
            update_contact = list(contact.values())
            update_contact.append(name)
            name = contact.get('Name')
    update_contacts(update_contact)     
    return redirect(f'/{name}/')


@app.route('/<name>/delete/', methods=['POST'])
def delete(name):
    delete_contact(name)
    return redirect('/')

app.run(debug=True)