import random

def pick_six():
    number_list = []
    for i in range(6):
        number_list.append(random.randint(1,99))
    return number_list



def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
        i += 1
    return matches

def money_won(matches):
    winning_dict = {
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }
    if winning_dict.get(matches) == 6:
        print("JACKPOT!!!")
    return winning_dict.get(matches)

def main():
    balance = 0
    winning = pick_six()
    for i in range(100000):
        ticket = pick_six()
        matches = num_matches(winning, ticket)
        balance -= 2
        if matches > 0:
            balance += money_won(matches)
    print(f"Your ending balance is {balance}")

main()
        