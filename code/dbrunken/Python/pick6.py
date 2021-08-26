'''
pick6

computer picks 6 random numbers from 1-99
matching numbers between ticket and winning numbers determines payoff
'''

import random

#got help from https://www.tutorialspoint.com/generating-random-number-list-in-python
winning_numbers = []
for i in range(6):
    nums = random.randint(0, 99)
    winning_numbers.append(nums)
print(winning_numbers)

drawn_numbers = []
for i in range(6):
    nums = random.randint(0, 99)
    drawn_numbers.append(nums)
print(drawn_numbers)

def match_payout():
    matches = 0
    pay_key = {
        1 : 4,
        2 : 7,
        3 :100,
        4 :50000,
        5 :1000000,
        6: 25000000
    }
    if pay_key(matches) == 6:
        return print("Jack Pot!")
    else:
        return pay_key(matches)


def lotto():
    play_money = 0
    jP = winning_numbers
    for i in range(1000):
        win_list = winning_numbers

