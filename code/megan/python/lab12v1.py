with open('contact.csv', 'r') as file:
    lines = file.read().split('\n')


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

print(contacts)