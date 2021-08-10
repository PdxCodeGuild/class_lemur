digit_phrase = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def get_user_input():
    while True:
        try:
            user_number = int(input("Enter an integer between 100 and 999: "))
        except ValueError:
            print("Invalid entry.  Please enter an integer between 100 and 999.")
            continue
        else:
            if user_number > 999 or user_number < 100:
                print("Invalid entry.  Please enter an integer between 100 and 999.")
                continue
            else:
                break
    return user_number

def print_result(ones_digit, tens_digit, hundreds_digit, digit_to_phrase):
    if tens_digit < 20:
        ones_english = digit_to_phrase[ones_digit + tens_digit]
        hundreds_english = digit_to_phrase[hundreds_digit] + " hundred"
        if ones_english == 'zero':
            print(hundreds_english)
        else:
            print(f"{hundreds_english} {ones_english}")
    else: 
        ones_english = digit_to_phrase[ones_digit]
        tens_english = digit_to_phrase[tens_digit]
        hundreds_english = digit_to_phrase[hundreds_digit] + " hundred"
        if ones_english == 'zero':
            print(f"{hundreds_english} {tens_english}")
        else:
            print(f"{hundreds_english} {tens_english}-{ones_english}")

def main(digit_phrase):
    user_number = get_user_input()
    ones_digit = user_number%10
    tens_digit = (user_number%100//10)*10
    hundreds_digit = user_number//100
    print_result(ones_digit, tens_digit, hundreds_digit, digit_phrase)


main(digit_phrase)