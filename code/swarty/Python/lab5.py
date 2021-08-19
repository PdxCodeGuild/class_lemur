"""
lab 5 David Swartwood


Let's write a python program to give basic blackjack playing advice during a game by asking 
the player for cards. First, ask the user for three playing cards 
(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card 
individually. Number cards are worth their number, all face cards are worth 10. At this point, 
assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted
"""

card=""
while card == "":
    card=input("What is your first card? ")
    playercards= [card]
    if card in ("2","3","4","5","6","7","8","9","10"):
        card=int(card)
    # Face or Ace"
    elif card in ("A", "J", "Q", "K"):
        if card == "A":
            card=1
        else:
            card=10
    #not in deck
    else:
        print("not a standard card")
        card=""
total=card
hit=1
while hit:
    card=""
    while card == "":
        card=input("What is your next card? ")
        playercards.append(card)
        if card in ("2","3","4","5","6","7","8","9","10"):
            card=int(card)
        #Face or Ace
        elif card in ("A", "J", "Q", "K"):
            if card == "A":
                card=1
            else:
                card=10
        #not in deck
        else:
            print("not a standard card")
            card=""
    total+=card
    hit=0
    if total > 21:
        print(f"{playercards, total} You busted!")
    elif total == 21:
        print(f"{playercards, total} Blackjack!")
    elif total <17:
        print(f"{playercards, total} Hit!")
        hit=1
    else:
        print(f"{playercards, total} stay")
        
    


