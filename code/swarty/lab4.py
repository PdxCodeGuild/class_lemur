"""
Lab 3 '# 2 Phrase'
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

V2 Handle numbers from 100-999.

V3 Convert a number to roman numerals.

V4 Convert a time given in hours and minutes to a phrase.
"""

#x=input("Enter a whole integer number to translate: ")

x=input("put in a mumber: ")
x=int(x)
numwords= {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    "c" : "hundred",
    "m" : "thousand",
    "g" : "million",
    "b" : "billion"
}

xstr=str(x)
xlen=len(xstr)
xcnt=xlen-1
if x<=19:
    print(numwords.get(x))
else:
    place=[]
    wordy=""
    for i in range(xlen):
        place.append((x//(10**(xcnt-i)))*(10**(xcnt-i)))
        wordy+= f'-{numwords.get(place[i])}'
        x=x%(10**(xcnt-i))
print("That number is "+ wordy.strip("-"))

