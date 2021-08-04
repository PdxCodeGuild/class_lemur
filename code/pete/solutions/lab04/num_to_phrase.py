translator = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens_translator = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}

tens_translator = {
    0: '',
    1: '',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def translate(number):
    """Given a number (int 0-999), returns the number as word/s
    For example: given 67, returns 'sixty-seven'"""

    if type(number) != int:
        raise TypeError("number must be an integer")

    if 0 <= number <= 999:
        raise ValueError("number must be from 0-999")

    if number == 0:
        return 'zero'
    ones = number % 10
    tens = number % 100 // 10
    hundreds = number // 100

    ones_str = translator[ones]
    tens_str = tens_translator[tens]
    hundreds_str = translator[hundreds]

    dash = '-' if ones != 0 and tens != 0 else ''
    space = ' ' if ones != 0 or tens != 0 else ''

    if number < 100:
        if tens == 1:
            teens_str = teens_translator[ones]
            return teens_str
        return tens_str + dash + ones_str

    if tens == 1:
        teens_str = teens_translator[ones]
        return hundreds_str + ' hundred' + space + teens_str

    return hundreds_str + ' hundred' + space + tens_str + dash + ones_str


if __name__ == '__main__':
    translate(9)
    translate(35)
    translate(264)

    translate(1001)

    translate('sixty-seven')
