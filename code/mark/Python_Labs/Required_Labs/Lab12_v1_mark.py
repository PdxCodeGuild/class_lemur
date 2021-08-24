file_name = "contacts.csv"

def open_and_read(file_name):
    with open(file_name, "r") as file:
        lines = file.read().split('\n')
        for i in range(len(lines)):
            lines[i] = lines[i].split(',')
    file.close
    return lines


def create_contacts_list(lines, contacts):
    for i in range(1,len(lines)):
        contacts.append({
            lines[0][0]: lines[i][0],
            lines[0][1]: lines[i][1],
            lines[0][2]: lines[i][2]
        })
    return contacts

def main(file_name):
    contacts = []
    lines = open_and_read(file_name)
    create_contacts_list(lines, contacts)
    for contact in contacts:
        print(contact)

main(file_name)