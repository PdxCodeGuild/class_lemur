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

# print(contacts)

while True: 

    name = input("Please enter your name: ")
    artist = input("Please enter your favorite artist: ")
    album = input("Please enter your favorite album by that artist: ")

    contacts.append({
        "name" : name,
        "artist" : artist,
        "album" : album
    })

    break

print(contacts)

