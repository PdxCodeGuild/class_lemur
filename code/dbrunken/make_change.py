'''
create monetary change
'''
coins = [
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
    
    for coin in coins:
        coinConvert = coin[1] * 100 # convert to pennies
        # print(pennies)
        coinCount =  int(pennies) // int(coinConvert) # floor divide to determine how many pennies there are
        pennies -= coinCount * coinConvert # subtract remaining pennies from total
        
        total = print(f' ')
        # print(coinCount, coinConvert)
    return 
    




total = input('how much money would you like to make change out of? ')
total = float(total)
print(make_change(total))


# if total == 0:
#     print("i see no money")

# else:
   