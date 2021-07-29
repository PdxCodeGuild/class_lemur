import random

balance = 0
winningTicket = [5, 3, 7, 2, 6, 3]
myTicket = [3, 6, 7, 2, 1, 6]


# def pick6():
#     for winningTicket in range(6):
#         print(random.randint(0,10))

def num_matches(winning, ticket):
    return set(winning) & set(ticket)   

num_matches(winningTicket, myTicket)
# print(num_matches)

