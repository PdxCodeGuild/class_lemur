from math import pi
from easygui.boxes.derived_boxes import enterbox
import easygui
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

# ------------------------------------------------------------------------------------------- #
'''
Possible additions: 
-----------------

''' 

pick_a_chord = random.choice(scale)
print(pick_a_chord.split(' '))

result  = scales.get_notes(pick_a_chord)
print(result)

while True:

    tonic_notes = input(f"Please enter the notes of the tonic scale in the key of {pick_a_chord}: ")

    tonic_notes = list(tonic_notes.split(' '))

    print(tonic_notes)

    if tonic_notes == result:
        print("Genius!")
        break
    else:
        print("Not quite")