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

x = int(input("Please enter a number between 0 and 99: "))

tens = x//10
ones = x%10

if x == 10:
    print("ten")
elif x == 11:
    print("eleven")
elif x == 12:
    print("twelve")
elif x == 13:
    print("thirteen")
elif x == 14:
    print("fourteen")
elif x == 15:
    print("fifteen")
elif x == 16:
    print("sixteen")
elif x == 17:
    print("seventeen")
elif x == 18:
    print("eighteen")
elif x == 19:
    print("nineteen")
else:
    print(ten[tens], one[ones])
