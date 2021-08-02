number = list(input("Please enter your 16 digit credit card number: "))

digits = [int(i) for i in number]

check_digit = digits.pop(-1)
print(digits)

digits_reversed = digits[::-1]
print(digits_reversed)

doubled = []
index = 0

for every_other in digits_reversed:

    if index % 2 == 0:
        doubled.append(every_other * 2)
    else:
        doubled.append(every_other)
    index += 1

print(doubled)

minus_nine = []

for digit in doubled:
    if digit > 9:
        minus_nine.append(digit - 9)
    else:
        minus_nine.append(digit)

print(minus_nine)

last = sum(minus_nine)
print(last)

final = [int(x) for x in str(last)]
print(final)

if final[1] == check_digit:
    print("This is a valid credit card number.")
else:
    print("Sorry. This is not a valid credit card number.")

