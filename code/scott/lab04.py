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

def digits_to_words(number):
    if number in ones_word:
        print(f'Your number is, {ones_word[number]}.')
    elif number in teens_word:
        print(f'Your number is, {teens_word[number]}.')
    else:
        tens_digit = number // 10
        ones_digit = number % 10
        print(f'Your number is, {tens_word[tens_digit]}-{ones_word[ones_digit]}.')



# Prompt user and get number
digits = int(input('Enter a number to be converted to words: '))
digits_to_words(digits)