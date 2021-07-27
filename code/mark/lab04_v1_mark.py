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
            user_number = int(input("Enter an integer between 0 and 99: "))
        except ValueError:
            print("Invalid entry.  Please enter an integer between 0 and 99.")
            continue
        else:
            if user_number > 99 or user_number < 0:
                print("Invalid entry.  Please enter an integer between 0 and 99.")
                continue
            else:
                break
    return user_number

def convert_numbers_to_words(digit_phrase, user_number):
    ones_digit = digit_phrase[user_number%10]
    tens_digit = digit_phrase[(user_number//10) *10]
    return tens_digit, ones_digit

def main(digit_phrase):
    user_number = get_user_input()
    tens_digit, ones_digit = convert_numbers_to_words(digit_phrase, user_number)
    if ones_digit == 'zero':
        print(tens_digit)
    else:
        print(f"{tens_digit}-{ones_digit}")

main(digit_phrase)