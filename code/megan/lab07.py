number = list(input("Please enter your 16 digit credit card number: "))

digits = [int(i) for i in number]

digits_minus_one = digits[0:15]

digits_reversed = digits_minus_one[::-1]
print(digits_reversed)
 
doubled = []

for every_other in digits_reversed:
    if every_other % 2 == 0:
        doubled.append(every_other * 2)

print(doubled)

for digit in digits_reversed:
    if digit < 9:
        print(digit - 9)

last = sum(digits_reversed)
print(last)

if 8 == digits[15]:
    print("This is a valid credit card number.")
else:
    print("Sorry. This is not a valid credit card number.")

