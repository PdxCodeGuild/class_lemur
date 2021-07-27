""" 
Lab 3 David Swartwood
Let's convert a dollar amount into a number of coins. The input will be the total amount, 
the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
"""

coins = [25,10,5,1]


total_cash=input("enter the cash amount in $.$$ format: ")
pennies=100 * float(total_cash)
change=[]
for coin in coins:
#   if pennies%coin == 0:
#       break
    change.append(pennies//coin)
    pennies = pennies%coin
print(change)

pennies=100 * float(total_cash)
quarters = pennies//25
pennies = pennies%25
dimes = pennies//10
pennies = pennies%10
nickels = pennies//5
pennies = pennies%5

print("change is: ", quarters, "quarters", dimes, "dimes", nickels, "nickels", pennies, "pennies")
