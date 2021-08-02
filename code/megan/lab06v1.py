import random

balance = 0

match = {
    0 : 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def pick6():
    return [random.randint(1, 99) for i in range(6)]

def num_matches(winning_ticket, current_ticket):
    '''
    This is going to return the amount of money made off of each individual ticket 
    '''
    matches = 0 
    for i in range(len(current_ticket)):
        # print(current_ticket[i], 'current ticket index')
        # print(winning_ticket[i], 'winning ticket index')
        if current_ticket[i] == winning_ticket[i]:
            matches += 1

    return matches 

def ROI(a, b):
    return (a - b) / b
    

winning = pick6()

purchased = []

for i in range(100000):

    purchased.append(pick6())
                  

for ticket in purchased:
    balance -= 2 
    matches = num_matches(winning, ticket)

    balance += match[matches]

print(balance)

expenses = 100000 * -2
earnings = balance - expenses

print(expenses)
print(earnings)

print(ROI(earnings, expenses))
