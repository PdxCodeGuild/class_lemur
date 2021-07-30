import random

balance = 0

match = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def pick6():
    return [random.randint(1, 99) for i in range(6)]

winning = pick6(

purchased = []

for i in range(100000):

    purchased.append(pick6())

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
    print(matches)
                  


    # iterate over the bought list 
    # for each element of the bought list, compare it to the winning ticket 
    # since each element is also a list, iterate over the list element itself 
    # find the matches 
    # create a counter for number of matches, starting at 0 
    # create dictionary for what # of matches means

# num_matches(winning, purchased)

for ticket in purchased:
    num_matches(winning, ticket)



#     for ticket in tickets:
#         print(tickets)
#         balance -= 2
#         print(balance)

# print(winning)
# print(pick6())
# print(len(purchased))
# print(purchased)


