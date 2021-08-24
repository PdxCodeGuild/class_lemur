import random

def pick6():
    return random.sample(range(100), 6)
#     ticket = []
#     for _ in range(6):
#         ticket.append(random.randint(0, 99))
#         ticket.append(random.sample())
#     return ticket
# for _ in range(1000000):
#     ticket = pick6()
#     if len(set(ticket)) < 6:
#         print(ticket)


def num_matches(winning_ticket, ticket):
    matches = 0
    for winning_num, ticket_num in zip(winning_ticket, ticket):
        if winning_num == ticket_num:
            matches += 1
    return matches
    # for i in range(len(winning_ticket)):
    #     winning_num = winning_ticket[i]
    #     ticket_num = ticket[i]
    #     if winning_num == ticket_num:
    #         matches += 1

# print(num_matches([1, 2, 3, 4, 5, 6], [1, 2, 4, 5, 3, 6]))


winning_ticket = pick6()
balance = 0
expenses = 0
earnings = 0

matches_to_winnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000,
}

for _ in range(100_000):
    ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_ticket, ticket)
    balance += matches_to_winnings[matches]
    earnings += matches_to_winnings[matches]

print('Final Balance:')
print(balance)
print()
print('ROI:')
print((earnings - expenses) / expenses)