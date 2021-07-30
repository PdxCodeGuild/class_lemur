from os import name


file_name = "contacts.csv"



def get_user_selection():
    while True:
        try:
            selection = int(input("Select one of the following options: \n\t1. Create contact, \n\t2. Retrieve Contact, \n\t3. Update Contact, \n\t4. Delete Contact : "))
        except ValueError:
            print("That is not a valid selection")
            continue
        else:
            return selection
    
def create_new_contact(headers, contacts):
    new_line = []
    new_line.append(input("Enter the new contact's name: ").lower())
    new_line.append(input("Enger the new contact's favorite color: ").lower())
    new_line.append(input("Enter the new contact's favorite color: ").lower())
    append_contacts_list(new_line, headers, contacts)
    

def retrieve_contact(contacts):
    contact_to_retrieve = input("Name of contact you would like to retrieve: ").lower()
    while True:
        retrieved_contact = check_if_exists(contacts, contact_to_retrieve) 
        if retrieved_contact is False:
            contact_to_retrieve = input("Name of contact you would like to retrieve: ").lower()
        else:
            break
    #print(retrieved_contact)
    return contact_to_retrieve
    


def update_contact(contacts):
    contact_to_update = retrieve_contact(contacts)
    new_fruit = input("Enter the new favorite fruit: ").lower()
    new_color = input("Enter the new favorite color: ").lower()
    for contact in contacts:
        if contact_to_update in contact.get("name"):
            contact["favorite fruit"] = new_fruit
            contact["favorite color"] = new_color
    return contacts

def delete_contact(contacts):
    contact_to_delete = retrieve_contact(contacts)
    for contact in contacts:
        if contact_to_delete in contact.get("name"):
            contacts.remove(contact)
    for contact in contacts:
        print(contact)
    return contacts

def check_if_exists(contacts, name_of_contact):
    for contact in contacts:
        if name_of_contact in contact.get("name"):
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

def headers(lines):
    headers_list = lines.pop(0)
    return headers_list, lines

def main(file_name):
    contacts = []
    lines = open_and_read(file_name)
    headers_list, lines = headers(lines)
    create_contacts_list(lines, headers_list, contacts)
    for contact in contacts:
        print(contact)
    selection = get_user_selection()
    if selection == 1:
        contacts = create_new_contact(headers_list, contacts)
    elif selection == 2:
        print(retrieve_contact(contacts))
    elif selection == 3:
        contacts = update_contact(contacts)
    elif selection == 4:
        contacts = delete_contact(contacts)
    else:
        raise ValueError
    for contact in contacts:
        print(contact)
    

main(file_name)