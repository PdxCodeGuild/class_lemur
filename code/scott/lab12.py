# Class Lemur Day Course
# Lab 12, CSV
# Scott Cormack
# Python 3.9.6
file_name = 'smite_characters.csv'
complete = []
# Open CSV and convert to a list of dictionaries
def convert_csv(file):
    temp = []
    with open(file, 'r') as f:
        lines = f.read().split('\n')
    for i in lines:
        temp.append(i.split(','))
    for i in range(1, len(lines)):
        complete.append({
            temp[0][0] : temp[i][0],
            temp[0][1] : temp[i][1],
            temp[0][2] : temp[i][2]
        })

def main():
    convert_csv(file_name)
    # Process input
    while True:
        choice = input('Choose if you would like to "create", "retrieve", "update" or "delete" a record ("exit" to quit): ').lower()
        if choice == 'exit':
            break
        # Direct to proper function
        elif choice == 'create':
            create()
        elif choice == 'retrieve':
            retrieve()
        elif choice == 'update':
            update()
        elif choice == 'delete':
            delete()
        else:
            print('Invalid entry. Enter "create", "retrieve", "update" or "delete". ')

def create():
    while True:
        new_dict = {}
        # Get name
        data = input('Enter a character name or "exit" to quit: ').lower()
        if data == 'exit':
            break
        elif data in complete:
            print('That name already exists. Enter another name: ')
        else:
            new_dict['name'] = data
        # Get pantheon
        data = input('Enter a character pantheon or "exit" to quit: ').lower()
        if data == 'exit':
            break
        else:
            new_dict['pantheon'] = data
        # Get class
        data = input('Enter a character class or "exit" to quit: ').lower()
        if data == 'exit':
            break
        else:
            new_dict['class'] = data
        # Add to final list
        complete.append(new_dict)
        main()
        
def retrieve():
    while True:
        choice = input('Which character information would you like to get?: ').lower()
        for i in complete:
            if i['name'] == choice:
                print(i)
            main()
        else:
            print('That character does not exist. Try again.')
            continue



def update():
    main()

def delete():
    main()

print('Welcome to the Smite Character database.')
main()
# print(complete)