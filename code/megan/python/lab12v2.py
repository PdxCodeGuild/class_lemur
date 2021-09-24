
file_path = '/Users/meganbradner/Desktop/pdx_code/class_lemur/code/megan/python/contact.csv'
file_path_2 = '/Users/meganbradner/Desktop/pdx_code/class_lemur/code/megan/python/contact2.csv'

def retrieve(userInput):
    '''Locates a user's information by their name, favorite artist, or favorite album'''
    for dict in contacts:

        for el in dict:
            if dict[el] == userInput:
                return dict


with open(file_path, 'r') as file:
    lines = file.read().split('\n')


keys = lines.pop(0).split(",")

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
        final = retrieve(person)

        print(final)

        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False
            break

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
            break

    elif requested_action == 'delete':

        person = input("Who do you want to delete? ")
        selected_dict = retrieve(person)

        contacts.remove(selected_dict)

        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False
            break

    elif requested_action == 'create':
        
        name = input("Please enter your name: ")
        artist = input("Please enter your favorite artist: ")
        album = input("Please enter your favorite album by that artist: ")

        contacts.append({
        "name" : name,
        "favorite_artist" : artist,
        "favorite_album" : album
    })
        
        again = input("Do you want to do something else? yes/no: ")

        if again == 'no':
            loop_control == False
            break

# contacts = str(contacts)
# print(contacts)


for contact in contacts:

    keys = list(contact.keys())


names = []

for contact in contacts:

    for key in keys:

        names.append(contact[key])


final = keys + names

final_output = ','.join(final)

words = final_output.split(',')
new_line = ""
word_count = 0

for word in words:

    new_line += word + ","
    word_count += 1
    
    if word_count == 3: 
        new_line += "\n"
        word_count = 0


with open(file_path, 'w') as file:
        file.write(new_line)

# final_list = ''.join(contacts)

with open(file_path_2, 'w') as file:
        file.write(contacts).split('\n')
