faceCards = {
    'J' : 10,
    'K' : 10,
    'Q' : 10,
    'A' : 1
}

print("Please select three cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")

first = input("What's your first card? ")

second = input("What's your second card? ")

third = input("What's your third card? ")


if first in faceCards:
    first = faceCards[first]

if second in faceCards:
    second = faceCards[second]

if third in faceCards:
    third = faceCards[third]
    

total = int(first) + int(second) + int(third)

if total < 17:
    print(f"Your total was {total}. I think you should hit.")
elif total >= 17 and total < 21:
    print(f"Your total was {total}. I think you should stay.")
elif total == 21:
    print(f"Your total was {total}. Blackjack!")
else:
    print(f"Your total was {total}. Already busted!")
