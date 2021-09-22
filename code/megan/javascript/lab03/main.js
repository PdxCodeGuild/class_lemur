contacts = {
    first_name: 'Megan',
    favorite_artist: 'Raleigh Ritchie',
    favorite_album: 'Andy'
}

console.log(contacts)
 
loop_control = true

while (loop_control == true) {

    requested_action = prompt("To create a contact, enter create. To retrieve a contact, enter retrieve. To update a contact, enter update. To delete a contact, enter delete: ")

    if (requested_action == 'retrieve') {

        person = prompt("Who do you want to retrieve? ")
        final = retrieve(person)

        console.log(final)

        again = prompt("Do you want to do something else? yes/no: ")

        if (again == 'no') {
            loop_control == false
            break
        }
    }

    else if (requested_action == 'update') {

        person = prompt("Who do you want to update? ")
        attribute = prompt("Do you want to update name, favorite artist, or favorite album? ")
        value = prompt("What do you want to change it to? ")

        selected_dict = retrieve(person)

        selected_dict[attribute] = value
        console.log(selected_dict)

        again = prompt("Do you want to do something else? yes/no: ")

        if (again == 'no') {
            loop_control == false
            break
        }

    }

    else if (requested_action == 'delete') {

        person = prompt("Who do you want to delete? ")
        selected_dict = retrieve(person)

        contacts.remove(selected_dict)

        again = prompt("Do you want to do something else? yes/no: ")

        if (again == 'no') {
            loop_control == false
            break
        }
    
    }

    else if (requested_action == 'create') {
        
        first_name = prompt("Please enter your name: ")
        artist = prompt("Please enter your favorite artist: ")
        album = prompt("Please enter your favorite album by that artist: ")

        contacts.append({
        "name" : first_name,
        "artist" : artist,
        "album" : album
    })
        
        again = prompt("Do you want to do something else? yes/no: ")

        if (again == 'no') {
            loop_control == false
            break
        }
}
}