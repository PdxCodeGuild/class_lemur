import sqlite3

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d

# con = sqlite3.connect("contacts.db")
# con.row_factory = dict_factory
# cur = con.cursor()
# cur.execute("SELECT * FROM contacts")
# print(cur.fetchall())

# con.close()

contact_info = ['Richard', 'apple', 'purple', 'Rick']

con = sqlite3.connect('contacts.db')
sql = '''UPDATE contacts 
    SET Name = ?,
    Favorite_Fruit = ?,
    Favorite_Color = ?
    WHERE Name = ?'''
cur = con.cursor()
cur.execute(sql, contact_info)
con.commit()
con.close()