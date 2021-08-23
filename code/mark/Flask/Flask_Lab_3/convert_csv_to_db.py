import csv, sqlite3

con = sqlite3.connect("contacts.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE Contacts (Name, Favorite_Fruit, Favorite_Color);") # use your column names here

with open('contacts.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Name'], i['Favorite Fruit'], i['Favorite Color']) for i in dr] # these are the column headers in your csv (first row)

cur.executemany("INSERT INTO Contacts (Name, Favorite_Fruit, Favorite_Color) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()