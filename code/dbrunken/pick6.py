'''
pick6

computer picks 6 random numbers from 1-99
matching numbers between ticket and winning numbers determines payoff
'''

import random
#got help from https://www.tutorialspoint.com/generating-random-number-list-in-python

winning_numbers = []
for i in range(0, 6):
    nums = random.randint(0, 99)
    winning_numbers.append(nums)

# print(winning_numbers)

userGuess = int(input('guess the numbers between 1 and 99 to win a prize '))

while userGuess != winning_number:
    if userGuess == winning_numbers:
        print("Wow, great guess! That's the winning numbers!")
        break

    if userGuess 
