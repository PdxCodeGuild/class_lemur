"""

Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
"""


#import modules
from datetime import datetime

def retriever(brand):
    for item in database:
        if item['Brand']==brand:
            for key in item:
                print(f'{key}:\n\t{item[key]}')




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
print(cars)

def carsort(db):
    cars=lines[0]+'\n'
    db.sort(key= lambda b:b['Brand'])
    for dictionary in db:
        line=''
        for key in dictionary:
            line+= dictionary[key] +", "
        line.strip(', ')
        cars+=line+'\n'
    return database, cars

action=input('''
c for create
r for retrieve
u for update
d for delete
What action would you like to perform? ''')
#Create a record
if action == 'c':
    loopout='y'
    while loopout=='y':
        car_brand=input('What is the car brand? ').title()
        category=input(f'What is the category for {car_brand}? ').title()
        known=input(f'What is that {car_brand} known for? ').title()
        hq_location=input(f'Where are the headquarters for {car_brand}? ').title()
        owner=input(f'Who is the majority owner of {car_brand}? ').title()
        
        database.append({
            data[0][0]:car_brand,
            data[0][1]:category,
            data[0][2]:known,
            data[0][3]:hq_location,
            data[0][4]:owner
        })
        loopout=input('Would you like to enter another (y/n)? ').lower()
    database, cars=carsort(database)
    print(cars)
    #Write to file
    with open(updated, 'w') as file:
        file.write(cars)

#retrieve a record
if action =='r':
    record=input('what brand would you like to retrieve? ').title()
    retriever(record)

#update a record
if action =='u':
    record=input('what brand would you like to update? ').title()
    retriever(record)
    for item in database:
        if item['Brand']==record:
            change_loc=input(f'What would you like to update in {item["Brand"]}?').title()
            change=input(f'What would you like to change {change_loc} to? ').title()
            for key in item:
                if key == change_loc:
                    item[key]=change
                    break
    retriever(record)
    database, cars=carsort(database)
    print(database)
    with open(updated, 'w') as file:
        file.write(cars)
                

if action == 'd':
    doomed=input('what brand would you like to remove? ').title()
    retriever(doomed)
    for item in database:
        if item['Brand']==doomed:
            i=database.index(item)
            database.pop(i)
    database, cars=carsort(database)
    print(cars)
    with open(updated, 'w') as file:
        file.write(cars)