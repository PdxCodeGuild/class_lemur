'''
convert numbers to words
'''
nums_1s = {
    0 : '',
    1 : 'one', 
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine'
}

teens = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen'
}

nums_10s = {
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
x = int(input("give a number: "))

def convert(num):
    
    if x == 0:
        return 'zero'
    
    place1 = num % 10
    place10 = num % 100 // 10
    place100 = num // 100

    ones = nums_1s[place1]
    tens = nums_10s[place10]
    hundreds = nums_1s[place100]

    if num < 100:
        if tens == 1:
            tens = teens[place1]
            return tens
        return tens + '-' + ones
    
    if place10 == 1:
        tens = teens[place1]
        return hundreds + ' hundred ' + tens
    return hundreds + ' hundred ' + tens + '-' + ones

print(convert(x))