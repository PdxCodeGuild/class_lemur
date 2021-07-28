"""
Lab 6 - David Swartwood

Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

V2 - add ROI
"""
prizes={
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

from random import randint
def pick6():
    numbers=[]
    for i in range(6):
        numbers.append(randint(1,99))
    return numbers

def num_match(winning=pick6(), ticket=pick6()):
    matches=0
    for i in range(6):
        if winning[i]==ticket[i]:
            matches+=1
    cash=prizes[matches]
    return matches, cash
cost=0
won=0
luck=0
for i in range(100):
    cost+=2
    luck,won+=num_match()

print(f'You spent ${cost} and won ${won}\nYou picked correctly {luck/600}% of the time')   