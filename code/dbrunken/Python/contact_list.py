'''
Contact list
8/4
create a contact list using a csv file
'''
'''
contact_list = [
    {'name': 'David Brunken', 'numbers': '91735-9374937', 'city': 'Lake Oswergo', 'occupation': 'Code Student'},
    {'name': 'Micah Romani', 'numbers': '348713-9348', 'city': 'Lake Oswergo', 'occupation': 'Supply Delivery'},
    {'name': 'Old Man', 'numbers': '32174-8748732', 'city': 'Canby', 'occupation': 'Pilot'},
    {'name': 'Nick McKenzie', 'numbers': '6123-64012', 'city': 'Avondale', 'occupation': 'Life Insurance'},
]
'''

from os import name


with open('contact_list.csv', 'r') as file:
    contacts = file.read().split('\n')
    # print(contacts)

headers = contacts.pop(0)
headers = headers.split(',')
# print(headers)

contact_list = []

for contact in contacts:
    contact = contact.split(',')
    # print(contact)
    contact_dict = dict(zip(headers, contact))
    contact_list.append(contact_dict)
# print(contact_list)

# contacts = list(contacts)
# print(contacts)


while True:
    # print(contact_list)no
    user_in = input('Add, Retrieve, Update, or Delete from the list? ')
    no = 'no'
    add = 'add'
    update = 'update'
    retrieve = 'retrieve'
    delete = 'delete'
    if user_in == 'no':
        print('goodbye')
        break
    
    #----------Add Contact-------------#
    elif user_in == add:
        user_name = input("\nWho would you like to add? ")
        user_number = input("\nWhat's their number? ")
        user_city= input("\nWhere do they live? ")
        user_occ= input("\nWhat do they do? ")
        user_dict = dict(zip(headers, [user_name.title(), user_number, user_city, user_occ]))
        print(user_dict, 'user_dict')
        contact_list.append(user_dict)
        print('\n', contact_list, 'contact list')
  
    #----------Retrieve Contact---------#
    elif user_in == retrieve:
        fetch_name = input("\n Who's contact info do you want to see? ")
        for contact in contact_list:
            # print(contact[name], 'contact')
            if contact['name'] == fetch_name.title():
                print('\n', contact, '\n')
            else:
                print('something went wrong')
    #----------Update Contact-----------#
    elif user_in == update:
        fetch_name = input("\n Who's contact needs to be updated? ")
        for contact in contact_list:
            if contact['name'] == fetch_name.title():
                print(contact)
                new_update = input('\n What needs to be updated? name, numbers, city, or occupation: ')
                contact[new_update] = input('\n Enter new information: ')
                updated_contact = contact
                print(updated_contact)

        '''
        ask user who needs to be updated with a for contact in contacts loop
        ask what part of contact needs to be updated .get()
            what needs to be updated? numbers
            enter new info: 8749874
            "print(updated_contact)"
        reassign
        '''
    
    #---------Delete Contact----------#
    elif user_in == delete:
        name_delete = input("\nWho needs to be removed? ")
        # loop over list of dictionaries
        for contact in contact_list: # contact is the loop variable
            if contact['name'] == name_delete.title(): # contact['name'] matches what you want to delete
                contact_list.remove(contact)
                print(contact_list)

    else:
        print("don't recognize that command")  
