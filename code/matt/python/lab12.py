from os import remove

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
contacts = []
records = []

for line in lines:
    contacts.append(line.split(','))

for contact in contacts:
    if contact[0] == 'name':
        continue
    records.append({
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
    print()


def display_menu():
    print(f"""
1: Create new record
2: Retrieve_record
3: Update record
4: Delete Record
5: Display Records
6: End program""")


def create_record(contacts2):
    user_record = []

    user_record.append(input("Please enter the name to be added: "))
    user_record.append(input("Please enter the favorite fruit to be added: "))
    user_record.append(input("Please enter the favorite color to be added: "))
    print()
    append_record(contacts2, user_record)


def retrieve_record(contacts2):
    user_name = input('Please enter the name your looking for: ')
    for contact in contacts2:
        if user_name in contact['name']:
            print(contact)
            print()
            return contact

    print('Record does not exist.')


def update_record(contacts2):
    record = retrieve_record(contacts2)
    selection = int(
        input(f'Which record would you like to update 1, 2 , or 3? (enter 1 for name, 2 for favorite fruit, or 3 for favorite color): '))
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
        print('\nRecord does not exist.')


while True:
    display_menu()
    user_selection = int(input("Please enter your selection: "))
    if user_selection == 1:
        create_record(records)
    elif user_selection == 2:
        retrieve_record(records)
    elif user_selection == 3:
        update_record(records)
    elif user_selection == 4:
        delete_record(records)
    elif user_selection == 5:
        print_record(records)
    else:
        print('Program exiting')
        break

temp_list = []
updated_records = []
for contact in records:
    for key in contact.keys():
        if key not in temp_list:
            temp_list.append(key)
    for value in contact.values():
        temp_list.append(value)

i = 0
while i < len(temp_list):
    updated_records.append(temp_list[i:i + 3:])
    i += 3

with open("contacts2.csv", 'w', encoding='utf-8') as f:
    for list in updated_records:
        f.write(','.join(list))
        f.write("\n")
