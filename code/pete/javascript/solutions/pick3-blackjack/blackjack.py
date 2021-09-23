card_dict = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

card1 = input('Enter a card: ')
card2 = input('Enter another card: ')
card3 = input('Enter yet another card: ')

cards = [card1, card2, card3]

total = 0

for card in cards:
    total += card_dict[card]

print('your total is: ' + str(total))

if total < 17:
    print('hit')
elif total < 21:
    print('stay')
elif total == 21:
    print('blackjack')
else:
    print('bust')