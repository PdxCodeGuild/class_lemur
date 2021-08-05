"""

Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
"""


#import modules
from datetime import datetime

file='../../code/swarty/DavidsData.csv'
updated=f'../../code\swarty\DavidsData_{datetime.now().strftime("%b%d_%Y")}.csv'
#Read current file

with open(file, 'r') as file:
    cars=file.read()
    lines=cars.split('\n')
    #categories=lines.pop(0)
data=[]
database=[]
for line in lines:
    line=line.split(',')
    data.append(line)
for i in range(1,len(data)):
    item={}    #new object with new ID
    for j in range(len(data[i])):
        category_name=data[0][j].strip()
        category_data=data[i][j].strip()
        item.update({category_name:category_data})  
    database.append(item)

# add things

#Create a record
loopout='y'
while loopout=='y':
    car_brand=input('What is the car brand? ')
    category=input('What is the category for {car_brand}? ')
    known=input('What is that {car_brand} for? ')
    hq_location=input('Where are the headquarters for {car_brand}? ')
    owner=input('Who is the majority owner of {car_brand}? ')
    
    database.append({
        data[0][0]:car_brand,
        data[0][1]:category,
        data[0][2]:known,
        data[0][3]:hq_location,
        data[0][4]:owner
    })
    cars+=f'\n{car_brand},{category},{known},{hq_location},{owner}'
    loopout=input('Would you like to enter another (y/n)? ').lower()


#Write to file
with open(updated, 'w') as file:
    file.write(cars)