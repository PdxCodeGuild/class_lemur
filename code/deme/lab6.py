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

for i in range (0, 1000000):
    balance -= 2
    match = 0
    numbers = pick_6()
    for k in range(len(numbers)):
        if win[k] == numbers[k]:
            match += 1
    
    if match == 1:
        print(f"Balance = ${4 - balance}" )
    # elif match == 2:
        print(f"Balance = ${7 - balance}" )
    elif match == 3:
        print(f"Balance = ${100 - balance}" )
    elif match == 4:
        print(f"Balance = ${50000 - balance}" )
    elif match == 5:
        print(f"Balance = ${1000000 - balance}" )
    elif match == 6:
        print(f"Balance = ${25000000 - balance}" ) 
    else:
        print("You lose")


