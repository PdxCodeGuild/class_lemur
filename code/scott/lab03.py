# Class Lemur Day Course
# Lab 3, Make Change
# Scott Cormack
# Python 3.9.6

# Prompt and get input
print('This program will break down a currency amount into coins.')
dollar_amount = float(input('Input the dollar amount that you wish to calculate: '))

# Convert dollar amount into pennies and shave off decimals
total_cents = int(dollar_amount * 100)

# Calculate change
quarters = total_cents // 25
dimes = total_cents % 25 // 10
nickels = total_cents % 25 % 10 // 5
pennies = total_cents % 5

# Print result
print(f'Total coins to make ${dollar_amount} is:')
print(f'Quarters: {quarters}')
print(f'Dimes: {dimes}')
print(f'Nickels: {nickels}')
print(f'Pennies: {pennies}')