card_dict = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def get_user_input(card_dict):
    first_card = input("What's your first card? ").capitalize()
    while first_card not in card_dict:
        print("That is not a valid card, please enter 2-10, or A,J,Q,K")
        first_card = input("What's your first card? ").capitalize()
    second_card = input("What's your second card? ").capitalize()
    while second_card not in card_dict:
        print("That is not a valid card, please enter 2-10, or A,J,Q,K")
        second_card = input("What's your second card? ").capitalize()
    third_card = input("What's your third card? ").capitalize()
    while third_card not in card_dict:
        print("That is not a valid card, please enter 2-10, or A,J,Q,K")
        third_card = input("What is your third card? ").capitalize()
    return [first_card, second_card, third_card]

def current_card_total(card_list, card_dict):
    running_total = 0
    for card in card_list:
        running_total += card_dict.get(card)
    return running_total

def give_advice(hand_value):
    if hand_value < 17:
        print(f"{hand_value} Hit")
    elif hand_value < 21:
        print(f"{hand_value} Stay")
    elif hand_value == 21:
        print(f"{hand_value} Blackjack!")
    else:
        print(f"{hand_value} Already Busted")

def main(card_dict):
    card_list = get_user_input(card_dict)
    hand_value = current_card_total(card_list, card_dict)
    give_advice(hand_value)

main(card_dict)


