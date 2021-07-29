'''
convert numbers to words
'''

#number structures (10s)
nums_10s = {
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety"
}
# teens

#number structures (singles)
nums_1s = {
    0 : 'zero',
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

x = int(input("give a number: "))
place10 = x // 10
print(place10)
place1 = x % 10
print(place1)

def num_phrase(tens, singles,):
    if tens > 0:
        return nums_10s.get(tens) + '-' + nums_1s.get(singles)
    if singles >= 0:
        return nums_1s.get(singles)


phrase = num_phrase(place10, place1)
print(phrase)
