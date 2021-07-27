ten = {
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

x = int(input("Please enter a number between 0 and 99: "))

tens = x//10
ones = x%10

print(ten[tens], one[ones])
