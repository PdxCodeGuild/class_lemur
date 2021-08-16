import random
from easygui.boxes.button_box import buttonbox
from easygui.boxes.derived_boxes import enterbox, msgbox
import mingus.core.keys as keys
import mingus.core.intervals as intervals
import mingus.core.scales as scales

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
options = ['I don\'t know', 'idk', 'not sure', 'i don\'t know', 'don\'t know']

# ------------------------------------------------------------------------------------------ #

while True:

    msg = "What would you like to work on?"
    title = "Let's practice music theory!"

    choices = ["Intervals", "Key signatures", "Relative minor keys", "Scales", "Quit"]
    choice = buttonbox(msg, title, choices)

    if choice == 'Quit':
        break

    elif choice == 'Intervals':
        note1 = random_notes(scale)
        note2 = random_notes(scale)

        while True:

            answer = enterbox(f"What is the interval between {note1} and {note2} \n(or 'done' to exit) ")

            if answer == 'done':
                break

            elif answer == new_interval(note1, note2):
                msgbox("You got it!")

                note1 = random_notes(scale)
                note2 = random_notes(scale)

            elif answer in options:
                msgbox(f"The answer was {new_interval(note1, note2)}")

                note1 = random_notes(scale)
                note2 = random_notes(scale)

            elif answer != new_interval(note1, note2): 
                msgbox("Sorry, try again!")

    elif choice == 'Key signatures':

        signature = random_notes(scale)

        while True: 

            ask = enterbox(f"How many sharps or flats are in the key of {signature}? \nPositive numbers for sharp keys and negative numbers for flat keys \n(or 'done' to exit) ")

            if ask == 'done':
                break

            elif ask in options:
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

            elif new_key in options:
                msgbox(f"The answer was {relative_keys(original_key)} minor")
                
                original_key = random_notes(scale)

            else:
                msgbox("Sorry, try again!")
    
    elif choice == 'Scales':
        
        pick_a_chord = random_notes(scale)

        while True:

            tonic_notes = enterbox(f"Please enter the notes of the tonic scale in the key of {pick_a_chord} \n(or 'done' to exit) ")

            if tonic_notes == 'done':
                break
            
            elif tonic_notes in options:
                msgbox(f"The answer was {scales.get_notes(pick_a_chord)}")

                pick_a_chord = random_notes(scale)

                continue

            tonic_notes = list(tonic_notes.split(' '))

            if tonic_notes == scales.get_notes(pick_a_chord):
                msgbox("You got it!")

                pick_a_chord = random_notes(scale)

            else:
                msgbox("Sorry, try again!")

