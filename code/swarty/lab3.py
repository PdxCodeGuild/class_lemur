""" 
Lab 3 David Swartwood
Let's convert a dollar amount into a number of coins. The input will be the total amount, 
the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
"""
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

#coins = [25,10,5,1]


total_cash=input("enter the cash amount in $.$$ format: ")
pennies=100 * float(total_cash)
change=[]
for coin in coins:
    print(f"There are {int(pennies//(coin[1]))} {coin[0]} ") #print # of the current coin
#    change.append(round(pennies//(coin[1])))
    pennies = pennies%coin[1]                       #Change Remining cents
#print(change)

#print("change is: ", change[0], coins[0], change[1], change[2], "nickels", change[3], "pennies")

