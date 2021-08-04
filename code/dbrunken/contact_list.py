'''
Contact list
8/4
create a contact list using a csv file
'''

with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

contacts = [
    {'name': 'David Brunken', 'numbers': '91735-9374937', 'city': 'Lake Oswergo', 'occupation': 'Code Student'},
    {'name': 'Micah Romani', 'numbers': '348713-9348', 'city': 'Lake Oswergo', 'occupation': 'Supply Delivery'},
    {'name': 'Old Man', 'numbers': '32174-8748732', 'city': 'Canby', 'occupation': 'Pilot'},
    {'name': 'Nick McKenzie', 'numbers': '6123-64012', 'city': 'Avondale', 'occupation': 'Life Insurance'},
]

user_in = input('Would you like to add any other contacts to the list? ')

while user_in == 'yes' or 'Yes' or 'Y':
    user_name = input("\nWho would you like to add? ")
    user_number = input("\nWhat's their number? ")
    user_city= input("\nWhere do they live? ")
    user_occ= input("\nWhere do they live? ")

    contacts[]
    