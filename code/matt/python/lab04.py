# Create dictionary to hold all number combinations.
numbers_dict = {
    0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",
    9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
    15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
    20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",
    80:"eighty", 90:"ninety", 100:"one-hundered", 200:"two-hundered", 300:"three-hundered",
    400:"four-hundered", 500:"five-hundered", 600:"six-hundered", 700:"seven-hundered",
    800:"eight-hundered", 900:"nine-hundered",
}

# Get user input to decide number.
num = int(input("Please enter a number 1 - 999: "))

# Set places to have 0 in positions not relevent to their location.
hundreds_place = num - (num % 100)

tens_place = num % 100 

ones_place = num % 10

# Determine tens place if it is between 11 and 20 and if not 0 out other places.
if tens_place >= 11 and tens_place <= 19:
    ones_place = 0
else:
     tens_place = num % 100 - (num % 10)

print() 
# Just used to get rid of spaces if theres no hundreds or tens place.
if hundreds_place == 0 and tens_place == 0:
    print(f"{numbers_dict[ones_place]}")
elif hundreds_place == 0:
    print(f"{numbers_dict[tens_place]} {numbers_dict[ones_place]}")
else: 
    print(f"{numbers_dict[hundreds_place]} {numbers_dict[tens_place]} {numbers_dict[ones_place]}")

print()

# Set tens place to have 0 in other positions.
tens_place = num % 100 - (num % 10)

roman_numeral_dict =  {
    0:"", 1: "I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X",
    20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",100:"C",
    200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
}

print(f"{roman_numeral_dict[hundreds_place]}{roman_numeral_dict[tens_place]}{roman_numeral_dict[ones_place]}")