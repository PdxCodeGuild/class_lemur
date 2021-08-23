# Class Lemur Day Course
# Lab 12, CSV
# Scott Cormack
# Python 3.9.6

characters = []

# Unpack the CSV and turn it into a working list of dictionaries
with open('smite_characters.csv', 'r') as f:
    lines = f.read().split('\n')
headers = lines.pop(0).split(',')
characters = []
for line in lines:
    temp = []
    line = line.split(',')
    temp = dict(zip(headers, line))
    characters.append(temp)

def check(name):
    for character in characters:           
        if name in character['name']:
            return(True)
    print('Character not found.')

def retrieve(name):
    for character in characters:           
        if name in character['name']:
            print(character)  

def update():
    ...

def create():
    ...

def delete(name):
    for character in characters:
        if name in character['name']:
            del(character)
            
# The one method to rule them all
def main():
    while True:
        choice = input('Input one of the following commands:\n(r) - to retrieve a record by name\n(u) - to update and existing record\n(c) - to create a new record\n(d) - to delete a record\n(e) - to exit\n:').lower()
        if choice == 'r':
            choice = input('Enter the name of the character: ')
            if check(choice):
                retrieve(choice)
        elif choice == 'u':
            choice = input('Enter the name of the character: ')
            if check(choice):
                update(choice)
        elif choice == 'c':
            choice = input('Enter the name of the character: ')
            create(choice)
        elif choice == 'd':
            choice = input('Enter the name of the character: ')
            if check(choice):
                delete(choice)
        elif choice == 'e':
            print('Please leave a 5 star review on Yelp for the jankest database EVAR.  Thanks.')
            quit()
        else:
            print('Incorrect entry.  Try again.')

print('Welcome to the jankest, most put together by duct tape, Smite Character database. ')
main()

print(characters, type(characters))



    
