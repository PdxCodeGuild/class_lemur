from hashlib import new
import random 
import mingus.core.notes as notes
import mingus.core.intervals as intervals

def new_interval(note1, note2):
    '''This function will take two notes and determine the interval between them'''
    return intervals.determine(note1, note2)
 
def random_notes(list):
    '''This function will choose a random letter from the scale list and return it'''
    return random.choice(list)

scale = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#','Ab']

while True:

    # skills = input("Do you want to test your interval skills? yes/no: ")
    skills = input("What skill do you want to test? ")
    
    if skills == 'none':
        break
    
    elif skills == 'intervals':

        note1 = random_notes(scale)
        note2 = random_notes(scale)

        print(note1)
        print(note2)      

        while True:

            answer = input("Please enter the interval between these two notes: ")

            if answer == new_interval(note1, note2):
                print("You got it!")

                note1 = random_notes(scale)
                note2 = random_notes(scale)

                print(note1)
                print(note2)  

            elif answer == 'I don\'t know':
                print(f'The answer was {new_interval(note1, note2)}')

                note1 = random_notes(scale)
                note2 = random_notes(scale)

                print(note1)
                print(note2) 

            else:
                print("Sorry, try again!")

                print(note1)
                print(note2) 
            


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
or ask the user to input the notes of a particular chord (What notes make up a dominant seventh chord in the key of C?)

'''