from hashlib import new
import random 
import mingus.core.keys as keys
import mingus.core.notes as notes
import mingus.core.intervals as intervals


def new_interval(note1, note2):
    '''This function will take two notes and determine the interval between them'''
    return intervals.determine(note1, note2)
 
def random_notes(list):
    '''This function will choose a random letter from the scale list and return it'''
    return random.choice(list)

def random_key_signature(list):
    return keys.get_key_signature(list)

def relative_keys(list):
    return intervals.keys.relative_minor(list)

# scale = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#','Ab']
scale = ['A', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G','Ab']


while True:

    skills = input("Please enter the skill you would like to work on or 'quit' to exit: ")
    
    if skills == 'quit':
        break
    
    if skills == 'intervals':

        note1 = random_notes(scale)
        note2 = random_notes(scale)

        print(note1)
        print(note2)      

        while True:

            answer = input("Please enter the interval between these two notes or 'quit' to exit: ")

            if answer == 'quit':
                break

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

    elif skills == 'key signatures':
        
        signature = random_notes(scale) 

        while True: 

            ask = int(input(f"How many sharps or flats are in the key of {signature}? \nPositive numbers for sharp keys and negative numbers for flat keys "))

            if ask == 'quit':
                break

            if ask == random_key_signature(signature):
                print("You got it!")
                
                signature = random_notes(scale) 

            elif ask == 'I don\'t know':
                print(f"The answer was {random_key_signature(signature)}")
                
                signature = random_notes(scale) 

            else:
                print("Sorry, try again!")

    elif skills == 'relative minor keys':

        original_key = random_notes(scale)

        while True:

            new_key = input(f"What is the relative minor of the key of {original_key}? ")

            if new_key == 'quit':
                    break

            if new_key == relative_keys(original_key):
                print("You got it!")
                
                original_key = random_notes(scale)


            elif new_key == 'I don\'t know':
                print(f"The answer was {relative_keys(original_key)}")
                
                original_key = random_notes(scale)

            else:
                print("Sorry, try again!")


'''

Features:
---------

- Display two notes and ask user what the interval between them is ---> DONE
- Display key and ask user for the notes in the diatonic scale (ex: C - CDEFGABC) ---> DONE
- Display a key and ask for the parallel minor/major ---> DONE

- Display a note and ask for the note that is a specific interval above or below it 

'''