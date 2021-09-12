# Class Lemur Day Course
# Lab 12, CSV
# Scott Cormack
# Python 3.9.6

characters = []

# Unpack the CSV and turn it into a working list of dictionaries
with open('E:/class_lemur/code/scott/python/smite_characters.csv', 'r') as f:
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
            print(
                f'\nName: {character["name"].title()}\nPantheon: {character["pantheon"].title()}\nClass: {character["class"].title()}\n')


def update(name):
    retrieve(name)
    while True:
        for character in characters:
            if name in character['name']:
                choice = input(
                    'Input one of the following commands:\n(n) - to change the name\n(p) - to change the pantheon\n(c) - to change the class\n(e) - to return to the main menu\n:').lower()
                if choice == 'n':
                    change = input(
                        'Enter the new name of the character: ').lower()
                    character['name'] = change
                    print('New character: \n')
                    retrieve(character['name'])
                    update(character['name'])
                elif choice == 'p':
                    change = input(
                        'Enter the new pantheon of the character: ').lower()
                    character['pantheon'] = change
                    retrieve(character['name'])
                elif choice == 'c':
                    change = input(
                        'Enter the new class of the character: ').lower()
                    character['class'] = change
                    retrieve(character['name'])
                else:
                    main()


def create():
    nme = input('Enter the name of the new character: ').lower()
    pnth = input('Enter the new character\'s pantheon: ').lower()
    cl = input('Enter the new character\'s class: ').lower()
    x = {
        'name': nme,
        'pantheon': pnth,
        'class': cl
    }
    characters.append(x)
    print('You have created the following character: ')
    retrieve(nme)


def delete(name):
    for character in characters:
        if name in character['name']:
            characters.remove(character)


def write():
    with open("E:/class_lemur/code/scott/python/file_name1.csv", 'w') as f:
        f.write(f'name,pantheon,class')
        f.write('\n')
        for character in characters:
            nme = character['name']
            pnth = character['pantheon']
            cl = character['class']
            f.write(f'{nme},{pnth},{cl}')
            f.write('\n')

# The one method to rule them all


def main():
    while True:
        choice = input('Input one of the following commands:\n(r) - to retrieve a record by name\n(u) - to update an existing record\n(c) - to create a new record\n(d) - to delete a record\n(e) - to exit\n:').lower()
        if choice == 'r':
            choice = input('Enter the name of the character: ')
            if check(choice):
                retrieve(choice)
        elif choice == 'u':
            choice = input('Enter the name of the character: ')
            if check(choice):
                update(choice)
        elif choice == 'c':
            create()
        elif choice == 'd':
            choice = input('Enter the name of the character: ')
            if check(choice):
                delete(choice)
        elif choice == 'e':
            print('Writing any changes to the CSV.')
            write()
            print(
                'Please leave a 5 star review on Yelp for the jankest database EVAR.  Thanks.')
            quit()
        else:
            print('Incorrect entry.  Try again.')


print('Welcome to the jankest, most put together by duct tape, Smite Character database. ')
main()
