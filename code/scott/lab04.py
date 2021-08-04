# Class Lemur- Day Course
# Lab 4, Number to Phrase
# Scott Cormack
# Python 3.9.6

# Establish dicts for translation
ones_word = {
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}

teens_word = {
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'
}

odd_word = {
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'
}

tens_word = {
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'
}

hundreds_word = {
    1:'one-hundred',
    2:'two-hundred',
    3:'three-hundred',
    4:'four-hundred',
    5:'five-hundred',
    6:'six-hundred',
    7:'seven-hundred',
    8:'eight-hundred',
    9:'nine-hundred'
}

# Function to convert numerals to phrases
def digits_to_words(number):
    # Find how many digits are in the number
    digits = number
    count = 0
    while digits > 0:
         digits = digits // 10
         count += 1

    if count <= 1:
        print(f'Your number is, {ones_word[number]}.')
    elif number in range(10, 19):
        print(f'Your number is, {teens_word[number]}.')
    elif number in odd_word:
        print(f'Your number is, {odd_word[number]}.')
    elif count == 2:
        tens_digit = number // 10
        ones_digit = number % 10
        print(f'Your number is, {tens_word[tens_digit]}-{ones_word[ones_digit]}.')
    elif count == 3:
        hundreds_digit = number // 100 
        tens_digit = number // 10 % 10
        ones_digit = number % 10
        # Concatenate tens and ones digit to see if they are 1 - 19
        teens = int(str(tens_digit) + str(ones_digit))
        if tens_digit == 0 and ones_digit in ones_word:
            print(f'Your number is, {hundreds_word[hundreds_digit]}-{ones_word[ones_digit]}.')
        elif tens_digit in tens_word and ones_digit == 0:
            odd_digit = tens_digit * 10
            print(f'Your number is, {hundreds_word[hundreds_digit]}-{odd_word[odd_digit]}')
        elif teens in teens_word:
            print(f'Your number is, {hundreds_word[hundreds_digit]}-{teens_word[teens]}.')
        else:
            print(f'Your number is, {hundreds_word[hundreds_digit]}-{tens_word[tens_digit]}-{ones_word[ones_digit]}.')

# Prompt user and get number
digits = int(input('Enter a number to be converted to words: '))
digits_to_words(digits)