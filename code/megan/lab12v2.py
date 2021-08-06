file_path = '/Users/meganbradner/Desktop/pdx_code/class_lemur/code/megan/contact.csv'
file_path_2 = '/Users/meganbradner/Desktop/pdx_code/class_lemur/code/megan/contact2.csv'

def retrieve(userInput):
    '''Locates a user's information by their name, favorite artist, or favorite album'''
    for dict in contacts:
    # print(dict)
        for el in dict:
            # print(dict[el])
            if dict[el] == userInput:
                return dict


with open(file_path, 'r') as file:
    lines = file.read().split('\n')
# print(lines)


keys = lines.pop(0).split(",")
# print(keys)
# print(lines)

contacts = []

for line in lines:

    values = line.split(",")
    # print(values)

    pairs = dict(zip(keys, values))
    # print(pairs)
    contacts.append(pairs)

loop_control = True

while loop_control == True: 

    requested_action = input("To create a contact, enter create. To retrieve a contact, enter retrieve. To update a contact, enter update. To delete a contact, enter delete: ")

    if requested_action == 'retrieve':

        person = input("Who do you want to retrieve? ")
        print(retrieve(person))

        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False

    elif requested_action == 'update':

        person = input("Who do you want to update? ")
        attribute = input("Do you want to update name, favorite artist, or favorite album? ")
        value = input("What do you want to change it to? ")

        selected_dict = retrieve(person)

        selected_dict[attribute] = value
        print(selected_dict)

        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False

    elif requested_action == 'delete':

        person = input("Who do you want to delete? ")
        selected_dict = retrieve(person)

        contacts.remove(selected_dict)
        
        print(contacts)

        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False

    elif requested_action == 'create':

        name = input("Please enter your name: ")
        artist = input("Please enter your favorite artist: ")
        album = input("Please enter your favorite album by that artist: ")

        contacts.append({
        "name" : name,
        "artist" : artist,
        "album" : album
    })

        print(contacts)

        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False

    break 

lines = ','.join(lines)
# print(lines)

with open(file_path_2, 'w') as file:
    file.write(lines)

# print(contacts)