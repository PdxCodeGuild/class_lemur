'''
create a blackjack advicer
'''

from random import randint, choice

hand = []
hand_value = 0

face_cards = {
    'K' : 10,
    'Q' : 10,
    'J' : 10,
    '10' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
    'A' : 1
}


def sum_hand(uHand):
    uVal = 0
    for card in uHand:
        print(face_cards[card])
        uVal += face_cards[card]
    print(uVal)
    if uVal < 17:
        print('hit')
        new_card = input('take another card ')
        hand.append(new_card)
        return sum_hand(uHand)
    elif uVal < 21:
        print('stay')
    elif uVal == 21:
        print('winning hand')
    else:
        print('bust')
    # for card in userHandlist:
    #     currentCardValue = face_cards[card]
    #     # # print(currentCardValue)
    #     # currentCardValue = sum(face_cards.values())
    #     # print(currentCardValue)
    #     # # print(type(currentCardValue))


while len(hand) < 2:
    user_hand = input('what cards do you have in your hand? ')
    if user_hand in face_cards:
        hand.append(user_hand)



sum_hand(hand)
# print(len(hand))
