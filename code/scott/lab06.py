# Class Lemur - Day Course
# Lab 6, Pick 6
# Scott Cormack
# Python 3.9.6

import random

# Declare variables
ticket_num = []
winning_num = []
balance = 0
ticket_cost = 2
ticket_size = 6
num_games = 100000
# Prompt user
input('Welcome to the lottery simulator.  Press enter to start.')

# Generate random numbers and append list
def gen_numbers(list, num):
    i = 0
    while i < num:
        list.append(random.randint(1,99))
        i += 1
    return list

# Compare ticket numbers to winning numbers
def compare_num(ticket, winning):
    wins = 0
    for i in ticket:
        if i in winning:
            wins += 1
    return wins

# Process earnings and charge for ticket
def win_amount(win, amount):
    amount -= ticket_cost
    if win == 6:
        amount += 25000000
    elif win == 5:
        amount += 1000000
    elif win == 4:
        amount += 50000
    elif win == 3:
        amount += 100
    elif win == 2:
        amount += 7
    elif win == 1:
        amount += 4
    return amount


# Run process
i = 0
while i < num_games:
    ticket_num = gen_numbers(ticket_num, ticket_size)
    ticket_num.sort()
    winning_num = gen_numbers(winning_num, ticket_size)
    winning_num.sort()
    wins = compare_num(ticket_num, winning_num)
    balance = win_amount(wins, balance)
    # Wipe tickets to start over
    ticket_num = []
    winning_num = []
    i += 1

# Print results
print(f'You have earned ${balance} after playing {num_games} lottery tickets.')
