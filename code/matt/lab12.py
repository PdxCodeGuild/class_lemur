from os import remove

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []
contacts2 = []

for line in lines:
    contacts.append(line.split(','))

for contact in contacts:
    if contact[0] == 'name':
        continue
    contacts2.append({
        contacts[0][0]: contact[0],
        contacts[0][1]: contact[1],
        contacts[0][2]: contact[2]
    })


def append_record(contacts2, contact):
    contacts2.append({
        contacts[0][0]: contact[0],
        contacts[0][1]: contact[1],
        contacts[0][2]: contact[2]
    })


def print_record(contacts2):
    for contact in contacts2:
        print(contact)


def create_record(contacts2):
    user_record = []

    user_record.append(input("Please enter the name to be added: "))
    user_record.append(input("Please enter the favorite fruit to be added: "))
    user_record.append(input("Please enter the favorite color to be added: "))

    append_record(contacts2, user_record)


def retrieve_record(contacts2):
    user_name = input('Please enter the name your looking for: ')
    for contact in contacts2:
        if user_name in contact:
            print(contact)
            return contact
        else:
            print('Record does not exist.')


def update_record(contacts2):
    record = retrieve_record(contacts2)
    selection = int(
        input("Which record would you like to update? (enter 1,2, or 3): "))
    if selection == 1:
        record['name'] = input("Enter the new name: ")
    elif selection == 2:
        record['favorite fruit'] = input("Enter the new favorite fruit: ")
    elif selection == 3:
        record['favorite color'] = input("Enter the new favorite color: ")


def delete_record(contacts2):
    record = retrieve_record(contacts2)
    if record in contacts2:
        contacts2.remove(record)
    else:
        print('Record does not exist.')


create_record(contacts2)
retrieve_record(contacts2)
for contact in contacts2:
    print(contact)

# while True:
#     user_selection = int(input("Please enter your selection: "))
#     if user_selection == 1:
#         create_record(contacts2)
#         print_record(contacts2)
#     elif user_selection == 2:
#         retrieve_record(contacts2)
#         print_record(contacts2)
#     elif user_selection == 3:
#         update_record(contacts)
#         print_record(contacts2)
#     elif user_selection == 4:
#         delete_record(contacts2)
#         print_record(contacts2)
#     else:
#         print('Program exiting')
#         break


# for contact in contacts2:
#     print(contact)
