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
from random import randint
import decimal

prizes={
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}


def pick6():
    numbers=[]
    for i in range(6):
        numbers.append(randint(1,20))
    return numbers

def num_match(winning, ticket):
    matches=0
    for i in range(6):
        if winning[i]==ticket[i]:
            matches+=1
    cash=prizes[matches]
    print(matches,cash,winning,ticket)
    return matches, cash
cost=0
won=0
luck=0
for i in range(100000):
    cost+=2
    ticket_luck,ticket_win=num_match(pick6(),pick6())
    luck+=ticket_luck
    won+=ticket_win

print(f'You spent ${cost} and won ${won}\nYou picked correctly {round((luck/6),1)}% of the time\nYour ROI was {round(((won-cost)/cost)*100,1)}%')   
