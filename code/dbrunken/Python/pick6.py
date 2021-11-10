'''
pick6

computer picks 6 random numbers from 1-99
matching numbers between ticket and winning numbers determines payoff
'''

import random

#got help from https://www.tutorialspoint.com/generating-random-number-list-in-python

winning_numbers = []
drawn_numbers = []
balance = 0
ticket_cost = 2
num_games = 100000

''' Winning numbers function '''

def make_nums(ticket):
    for i in range(6):
        nums = random.randint(0, 99)
        ticket.append(nums)
    return ticket


def check_ticket(drawn, winning):
    wins = 0
    for i in range(len(drawn)):
        if drawn[i] == winning[i]:
            wins += 1
    return wins


def match_payout(win_nums, winnings):
    if win_nums == 6:
        winnings += 25000000
    elif win_nums == 5:
        winnings += 1000000
    elif win_nums == 4:
        winnings += 500000
    elif win_nums == 3:
        winnings += 100
    elif win_nums == 2:
        winnings += 7
    elif win_nums == 1:
        winnings += 4
    return winnings

i =0
while i < num_games:
    winning_numbers = make_nums(winning_numbers)
    drawn_numbers = make_nums(drawn_numbers)
    wins = check_ticket(drawn_numbers,winning_numbers)
    balance = match_payout(wins, balance)
    winning_numbers =[]
    drawn_numbers =[]
    i += 1

expenses = num_games * ticket_cost
final_earning = balance - expenses
roi = final_earning / expenses
print(f'You spent ${expenses}, with a final balance of ${final_earning}')
print(f'ROI: {roi}')