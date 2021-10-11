'''
create monetary change
'''
from typing import Counter


coins = [
    ("half dollar", .5),
    ('quarter', .25),
    ('dime', .10),
    ('nickle', .05),
    ('penny',  .01)
]

'''
pass in total dollar amount from input
convert to pennies
record running sum
divide total by 25(quarters)
'''

def make_change(user_in):
    pennies = user_in * 100
    # print(round(pennies, 2))
    count = 0
    for coin in coins:
        coinConvert = coin[1] * 100 # convert to pennies
        print(pennies)
        coinCount =  int(pennies) // int(coinConvert) # floor divide to determine how many pennies there are
        pennies -= coinCount * coinConvert # subtract remaining pennies from total
        # print(count)
        print(coinCount, coins[count][0])
        count +=1
    total = print(f'\n is what you have when {user_in} is converted to pennies. {coinCount} pennies is the remainder you will have with {coins[0][0]}.')

    return total
    




total = input('how much money would you like to make change out of? ')
total = float(total)

make_change(total)


# if total == 0:
#     print("i see no money")

# else:
   