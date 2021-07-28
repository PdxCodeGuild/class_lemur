hundred = {
    '': '',
    0: '',
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred', 
    9: 'nine hundred'
}

ten = {
    0: '',
    1: '',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}


one = {
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
    10: 'ten'
}

x = int(input("Please enter a number between 100 and 999: "))

hundreds = x//100

if hundreds > 0:
    toSubtract = hundreds * 100 
    newTotal = x - toSubtract 
    tens = newTotal//10
    ones = newTotal%10


print(hundred[hundreds], ten[tens], one[ones])

