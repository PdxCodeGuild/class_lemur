import random
def pick_6():
    win = []
    while len(win) < 6:
        win.append(random.randint(1,99))

    return win

win = pick_6()
balance = 0
numbers = []
cost = 2
loops = 0

for i in range (0, 10):
    loops += 1
    balance -= 2
    # cost +=2
    match = 0
    numbers = pick_6()
    for k in range(len(numbers)):
        if win[k] == numbers[k]:
            match += 1

    if match == 1:
        balance += 4
        match += 1
    elif match == 2:
        balance += 7
        match += 2
    elif match == 3:
        balance += 100
        match += 3
    elif match == 4:
        balance += 50000
        match += 4
    elif match == 5:
        balance += 1000000
        match += 5
    elif match == 6:
        balance += 25000
        match += 6

roi = (balance / (cost * loops) )
print(f"You had {match} matches.")
print(f"Your final balance is {balance}")
print(f"ROI is {roi}")


