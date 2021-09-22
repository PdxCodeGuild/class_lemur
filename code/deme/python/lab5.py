card1 = input("Enter card 1: ")
card2 = input("Enter card 2: ")
card3 = input("Enter card 3: ")

cards = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10
}
total = cards[card1] + cards[card2] + cards[card3]
hand = [card1, card2, card3]
for card in hand:
    if card == "A" and total <= 10:
        print("Deme")
        total += 10

if total < 17:
    print(f"{total} Hit")
elif total >= 17 and total <= 21:
    print(f"{total} Stay")
elif total == 21:
    print(f"{total} Blackjack!")
else:
    print(f"{total} Already Busted ")


