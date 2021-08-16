from easygui.boxes.derived_boxes import enterbox, msgbox
from mingus.core import chords
import mingus.core.notes as notes
import mingus.core.progressions as progressions
import random
import mingus.core.intervals as intervals
import mingus.core.scales as scales

def random_notes(list):
    '''This function will choose a random letter from the scale list and return it'''
    return random.choice(list)

def new_interval(note1, note2):
    '''This function will take two notes and determine the interval between them'''
    return intervals.determine(note1, note2)

scale = ['A', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G','Ab']

options = ['I don\'t know', 'idk', 'not sure', 'i don\'t know', 'don\'t know']

# ------------------------------------------------------------------------------------------- #
'''
pick_key = random_notes(scale)

while True:

    first = enterbox(f"Please enter the notes for the subdominant triad in the key of {pick_key}: ")
    second = enterbox(f"Please enter the notes for the dominant triad in the key of {pick_key}: ")

    if first == 'done' or second == 'done':
        break
    
    elif first in options or second in options:
        msgbox(f"The answer was {chords.IV(pick_key)}")
        msgbox(f"The answer was {chords.V(pick_key)}")

        pick_a_chord = random_notes(scale)

        continue

    first = list(first.split(' '))
    second = list(second.split(' '))

    if first == chords.IV(pick_key) and second == chords.V(pick_key):
        msgbox("Correct!")
        
        pick_a_chord = random_notes(scale)

    else: 
        msgbox("Sorry, not quite")
'''