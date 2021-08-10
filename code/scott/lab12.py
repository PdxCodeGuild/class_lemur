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
    loop = True
    while loop == True:
        choice = input('Choose if you would like to "create", "retrieve", "update" or "delete" a record ("exit" to quit): ').lower()
        if choice == 'exit':
            loop = False
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
    loop = True
    while loop == True:
        new_dict = {}
        # Get name
        data = input('Enter a character name: ').lower()
        if data in complete:
            print('That name already exists. Enter another name: ')
        else:
            new_dict['name'] = data
        # Get pantheon
            data = input('Enter a character pantheon: ').lower()
            new_dict['pantheon'] = data
        # Get class
            data = input('Enter a character class: ').lower()
            new_dict['class'] = data
        # Add to final list
            complete.append(new_dict)
            loop = False
        
def retrieve():
    while True:
        choice = input('Which character information would you like to get?: ').lower()
        for i in complete:
            if i['name'] == choice:
                print(i)
                main()

def update():
    while True:
        choice = input('Which character would you like to update?: ').lower()
        for i in complete:
            if i['name'] == choice:
                print(f'Current information for this character is {i}.')
                choice = input('Which attribute do you want to change?: ').lower()
                if choice == 'name':
                    change = input('What would you like to change it to?: ').lower()
                    temp = i
                    i['name'] = change
                    complete.append(i)
                    complete.remove(temp)
                elif choice == 'pantheon':
                    change = input('What would you like to change it to?: ').lower()
                    temp = i
                    i['pantheon'] = choice
                    complete.append(i)
                    complete.remove(temp)
                elif choice == 'class':
                    change = input('What would you like to change it to?: ').lower()
                    temp = i
                    i['class'] = choice
                    complete.append(i)
                    complete.remove(temp)
               
                main()

def delete():
    while True:
        choice = input('Which character would you like to delete?: ').lower()
        for i in complete:
            if i['name'] == choice:
                complete.remove(i)
                main()

print('Welcome to the Smite Character database.')
main()
print('Writing changes to CSV.')
final = ''
with open('file_name1.csv', 'w') as f:
    
        
print(final, type(final))
        
   
