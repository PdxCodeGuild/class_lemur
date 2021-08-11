import random 
import mingus.core.notes as notes
import mingus.core.intervals as intervals
import mingus.core.chords as chords

def new_interval(note1, note2):
    '''This functinon will take two notes and determine the interval between them'''
    return intervals.determine(note1, note2)

scale = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#','Ab']


note1 = random.choice(scale)
note2 = random.choice(scale)

while True: 

    skills = input("Do you want to test your interval skills? yes/no: ")

    if skills == 'no':
        break
    
    elif skills == 'yes':

        print(note1)
        print(note2)      

    answer = input("Please enter the interval between these two notes: ")

    if answer == new_interval(note1, note2):
        print("You got it!")

    else:
        print("Sorry, try again.")



'''

Features:
---------

- Display two notes and ask user what the interval between them is 
- Display a note and ask for the note that is a specific interval above or below it 
- Display a key and ask for the parallel minor/major (They're given C major - parallel minor is a)

???
----
- Display a scale and ask user to identify it 
- Display a chord and ask user the proper name of the chord (Major triad, minor 7th, etc

'''