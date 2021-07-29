# Ask for user input for cards.
first_card = input("What's your first card? ")

second_card = input("What's your second card? ")

third_card = input("What's your third card? ")

# Create blackjack dictionary to contain card values.
blackjack_value_dict = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

# Add card values together
sum_of_cards = (blackjack_value_dict[first_card] + blackjack_value_dict[second_card]
               + blackjack_value_dict[third_card])

# Use if statements to give advice to user.
if sum_of_cards < 17:
    print(f"{sum_of_cards} Hit")
elif sum_of_cards >= 17 and sum_of_cards < 21:
    print(f"{sum_of_cards} Stay")
elif sum_of_cards == 21:
    print(f"{sum_of_cards} Blackjack!")
else:
    print(f"{sum_of_cards} Busted")

