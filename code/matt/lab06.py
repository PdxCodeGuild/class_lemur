def main():
    import random

    def random_ticket():
        i = 0
        ticket = []
        while i < 6:
            x = random.randint(1, 99)
            ticket.append(x)
            i += 1 
        return ticket

    winning_ticket = random_ticket()

    def compare_tickets(winning_ticket,player_ticket):
        matches = 0
        i = 0
        while i < 6:
            if winning_ticket[i] == player_ticket[i]:
                matches += 1
            i += 1
        return matches
        
    j = 0
    earnings = 0
    expenses = 0

    while j < 100000:
        expenses += 2
        player_ticket = random_ticket()
        number_of_matches = compare_tickets(winning_ticket, player_ticket)
        if number_of_matches == 1:
            earnings += 4
        elif number_of_matches == 2:
            earnings += 7
        elif number_of_matches == 3:
            earnings += 100
        elif number_of_matches == 4:
            earnings += 50000
        elif number_of_matches == 5:
            earnings += 1000000
        elif number_of_matches == 6:
            earnings += 25000000
        j += 1

    roi = (earnings - expenses) / expenses

    print(earnings)
    print(expenses)
    print(roi)

main()

