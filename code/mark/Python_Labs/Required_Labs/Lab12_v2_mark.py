from os import name


file_name = "contacts.csv"



def get_user_selection():
    while True:
        try:
            selection = int(input("Select one of the following options: \n\t1. Create contact \n\t2. Retrieve Contact \n\t3. Update Contact \n\t4. Delete Contact \n\t5. Display all Contacts \n\t"))
        except ValueError:
            print("That is not a valid selection")
            continue
        else:
            return selection

def continue_or_quit():
    possible_options = [['y','yes','yeah'], ['n','no','nope']]
    user_input = input("\nWould you like to continue (yes/no)? ").lower()
    while user_input not in possible_options[0] and user_input not in possible_options[1]:
        print("That is not a valid entry.")
        user_input = input("\nWould you like to continue (yes/no)? ")
    if user_input in possible_options[0]:
        return True
    else:
        return False
    
def create_new_contact(headers, contacts):
    new_line = []
    for header in headers:
        new_line.append(input(f"Enter the new contact's {header}: ").lower())
    contacts = append_contacts_list(new_line, headers, contacts)
    print(f"New contact added: {contacts[-1]}")
    return contacts
    

def retrieve_contact(contacts):
    contact_to_retrieve = input("Name of contact you would like to retrieve: ").lower()
    while True:
        retrieved_contact = check_if_exists(contacts, contact_to_retrieve) 
        if retrieved_contact is False:
            contact_to_retrieve = input("Name of contact you would like to retrieve: ").lower()
        else:
            break
    print(retrieved_contact)
    return contact_to_retrieve
    


def update_contact(contacts, headers_list):
    options = headers_list
    loop_active = True
    contact_to_update = retrieve_contact(contacts)
    selection = input(f"Which feature would you like to update? ({options[0]}, {options[1]}, or {options[2]}) ").lower()
    while selection not in options:
        print("That is not a valid entry.")
        selection = input(f"Which feature would you like to update? ({options[0]}, {options[1]}, or {options[2]}) ").lower()
    updated_value = input(f"Enter the new value for {selection}: ")
    for contact in contacts:
        if contact_to_update in contact.get("name"):
            contact[selection] = updated_value
            print(f"Contact updated: {contact}")

    return contacts

def delete_contact(contacts):
    contact_to_delete = retrieve_contact(contacts)
    for contact in contacts:
        if contact_to_delete in contact.get("name"):
            contacts.remove(contact)
    return contacts

def check_if_exists(contacts, name_of_contact):
    for contact in contacts:
        if name_of_contact == contact.get("name"):
            print("contact Found!")
            return contact
    print("That name does not exist.")
    return False

def open_and_read(file_name):
    with open(file_name, "r") as file:
        lines = file.read().split('\n')
        for i in range(len(lines)):
            lines[i] = lines[i].split(',')
    file.close
    return lines

def create_contacts_list(lines, headers, contacts):
    for line in lines:
        append_contacts_list(line, headers, contacts)
    return contacts

def append_contacts_list(new_contact, headers, contacts):
    contacts.append({
        headers[0]: new_contact[0].lower(),
        headers[1]: new_contact[1].lower(),
        headers[2]: new_contact[2].lower()
    })
    return contacts

def headers(lines):
    headers_list = lines.pop(0)
    return headers_list, lines

def main(file_name):
    contacts = []
    loop_active = True
    lines = open_and_read(file_name)
    headers_list, lines = headers(lines)
    create_contacts_list(lines, headers_list, contacts)
    for contact in contacts:
        print(contact)
    while loop_active == True:
        selection = get_user_selection()
        if selection == 1:
            contacts = create_new_contact(headers_list, contacts)
        elif selection == 2:
            retrieve_contact(contacts)
        elif selection == 3:
            contacts = update_contact(contacts, headers_list)
        elif selection == 4:
            contacts = delete_contact(contacts)
        elif selection == 5:
            [print(contact) for contact in contacts]
        else:
            raise ValueError
        loop_active = continue_or_quit()
    

main(file_name)

