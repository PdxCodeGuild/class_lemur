# Class Lemur - Day Course
# Lab 5, Blackjack Advice
# Scott Cormack
# Python 3.9.6

# Prompt user
print('This is a tool to advise you on whether you should hit or stay while playing blackjack.')

# Function to gather user cards in hand
def blackjack_hand():
    cards = []
    while len(cards) < 3:
        cards.append((input('Enter a card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ').upper()))
    return cards
    
# Function to calculate total
def calculate(hand):
    total = 0
    for i in range(len(hand)):
        if hand[i] == 'A':
            total += 1
        elif hand[i].isnumeric():
            total = total + int(hand[i])
        else:
            total += 10
    return total

# Function to decide to hit or stay
def decide(num):
    if num < 17:
        print(f'You have {num}.  You should hit.')
    elif num == 21:
        print(f'You have {num}.  Blackjack!')
    elif num >= 17:
        print(f'You have {num}.  You should stay.')
    else:
        print(f'You have {num}.  You lost by busting.')

# Call functions to run program
hand = blackjack_hand()
score = calculate(hand)
decide(score)
