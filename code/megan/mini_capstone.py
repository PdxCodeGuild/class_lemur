import random
from easygui.boxes.button_box import buttonbox
from easygui.boxes.derived_boxes import enterbox, integerbox, msgbox
import mingus.core.keys as keys
import mingus.core.intervals as intervals

def random_notes(list):
    '''This function will choose a random letter from the scale list and return it'''
    return random.choice(list)

def new_interval(note1, note2):
    '''This function will take two notes and determine the interval between them'''
    return intervals.determine(note1, note2)

def random_key_signature(list):
    '''This function with return the key signature of any key'''
    return keys.get_key_signature(list)

def relative_keys(list):
    '''This function will take a key and return the relative minor'''
    return intervals.keys.relative_minor(list)


scale = ['A', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G','Ab']

# ------------------------------------------------------------------------------------------ #

while True:

    msg = "What would you like to work on?"
    title = "Let's practice music theory!"

    choices = ["Intervals", "Key signatures", "Relative minor keys", "Quit"]
    choice = buttonbox(msg, title, choices)

    if choice == 'Quit':
        break

    elif choice == 'Intervals':
        note1 = random_notes(scale)
        note2 = random_notes(scale)
        # both_notes = note1 + ' and ' + note2
        # msgbox(both_notes)

        while True:

            answer = enterbox(f"What is the interval between {note1} and {note2} \n(or 'done' to exit)")
            # answer = enterbox("Please enter the interval between these two notes \n(or 'done' to exit): ")

            if answer == 'done':
                break

            elif answer == new_interval(note1, note2):
                msgbox("You got it!")

                note1 = random_notes(scale)
                note2 = random_notes(scale)
                # both_notes = note1, note2
                # msgbox(both_notes)

            elif answer == 'I don\'t know':
                msgbox(f"The answer was {new_interval(note1, note2)}")

                note1 = random_notes(scale)
                note2 = random_notes(scale)
                # both_notes = note1, note2
                # msgbox(both_notes)

            elif answer != new_interval(note1, note2): 
                msgbox("Sorry, not quite!")

    elif choice == 'Key signatures':

        signature = random_notes(scale) 

        while True: 

            ask = enterbox(f"How many sharps or flats are in the key of {signature}? \nPositive numbers for sharp keys and negative numbers for flat keys \n(or 'done' to exit)")

            if ask == 'done':
                break

            elif ask == 'I don\'t know':
                msgbox(f"The answer was {random_key_signature(signature)}")
                
                signature = random_notes(scale) 

            elif int(ask) == random_key_signature(signature):
                msgbox("You got it!")

                signature = random_notes(scale) 

            else:
                msgbox("Sorry, try again!")

    elif choice == 'Relative minor keys':

        original_key = random_notes(scale)

        while True:

            new_key = enterbox(f"What is the relative minor of the key of {original_key}? \n(or 'done' to exit) ")

            if new_key == 'done':
                    break

            if new_key == relative_keys(original_key):
                msgbox("You got it!")
                
                original_key = random_notes(scale)


            elif new_key == 'I don\'t know':
                msgbox(f"The answer was {relative_keys(original_key)} minor")
                
                original_key = random_notes(scale)

            else:
                msgbox("Sorry, try again!")


'''

Features:
---------

- Display two notes and ask user what the interval between them is ---> DONE
- Display key and ask for key signature ---> DONE
- Display a key and ask for the parallel minor/major ---> DONE

'''