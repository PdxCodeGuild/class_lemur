'''
Contact list
8/4
create a contact list using a csv file
'''

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
print(contact_list)

# contacts = list(contacts)
# print(contacts)


'''
contact_list = [
    {'name': 'David Brunken', 'numbers': '91735-9374937', 'city': 'Lake Oswergo', 'occupation': 'Code Student'},
    {'name': 'Micah Romani', 'numbers': '348713-9348', 'city': 'Lake Oswergo', 'occupation': 'Supply Delivery'},
    {'name': 'Old Man', 'numbers': '32174-8748732', 'city': 'Canby', 'occupation': 'Pilot'},
    {'name': 'Nick McKenzie', 'numbers': '6123-64012', 'city': 'Avondale', 'occupation': 'Life Insurance'},
]
'''


while True:
    user_in = input('Would you like to add any other contacts to the list? ')
    no = 'no'
    if user_in == 'no':
        print('goodbye')
        break

    user_name = input("\nWho would you like to add? ")
    user_number = input("\nWhat's their number? ")
    user_city= input("\nWhere do they live? ")
    user_occ= input("\nWhat do they do? ")
    user_dict = dict(zip(headers, user_name, user_number, user_city, user_occ))
    contact_list.append(user_dict)
    
    print('\n', contact_list)
    