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

if x == 110:
    print("one hundred ten")
elif x == 111:
    print("one hundred eleven")
elif x == 112:
    print("one hundred twelve")
elif x == 113:
    print("one hundred thirteen")
elif x == 114:
    print("one hundred fourteen")
elif x == 115:
    print("one hundred fifteen")
elif x == 116:
    print("one hundred sixteen")
elif x == 117:
    print("one hundred seventeen")
elif x == 118:
    print("one hundred eighteen")
elif x == 119:
    print("one hundred nineteen")
else:
    print(hundred[hundreds], ten[tens], one[ones])

