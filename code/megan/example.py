from easygui.boxes.derived_boxes import enterbox
from mingus.core import chords
from mingus.core.keys import get_key
import mingus.core.notes as notes
import mingus.core.progressions as progressions
import random
import mingus.core.intervals as intervals

def random_notes(list):
    '''This function will choose a random letter from the scale list and return it'''
    return random.choice(list)

scale = ['A', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G','Ab']

# ------------------------------------------------------------------------------------------- #
'''
Possible addition: 
-----------------

Determine the note that is _ number of half steps away from a given note

while True: 

    note_one = random_notes(scale)
    num = random.randint(1, 12)


    while True: 
        
        solution = intervals.get_interval(note_one, num, key="C")

        answer = input(f"What is the note that is {num} half steps above {note_one}? ")

        if answer == 'done':
            break

        if answer == solution:
            print("You got it!")

            note_one = random_notes(scale)
            num = random.randint(1, 12)

            solution = intervals.get_interval(note_one, num, key="C")

        else:
            print(f"Sorry, not quite. The answer was {solution}")

            note_one = random_notes(scale)
            num = random.randint(1, 12)

            solution = intervals.get_interval(note_one, num, key="C")
                
'''
