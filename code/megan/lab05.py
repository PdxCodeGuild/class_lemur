print("Please select three cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")

faceCards = {
    'J' : 10,
    'K' : 10,
    'Q' : 10,
    'A' : 1
}

first = int(input("What's your first card? "))

second = int(input("What's your second card? "))

third = int(input("What's your third card? "))

total = first + second + third 


if total < 17:
    print(f"Your total was {total}. I think you should hit.")
elif total >= 17 and total < 21:
    print(f"Your total was {total}. I think you should stay.")
elif total == 21:
    print(f"Your total was {total}. Blackjack!")
else:
    print(f"Your total was {total}. Already busted!")

