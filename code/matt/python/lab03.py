dollars = float(input("Enter a dollar amount: "))

# Convert dollars to cents
cents = dollars * 100

# After each floor division modulus cents to get the remainder of the change.
quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickel = cents // 5
cents = cents % 5

pennies = cents % 10

# Print the number of each coin in the given dollar amount.
print(f"{quarters} quarters, {dimes} dimes, {nickel} nickels {pennies} pennies.\n")

# Create list of coins the string value pairs
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

# Get dollar amount from user.
dollars2 = float(input("Enter a dollar amount: "))

# Convert dollars to cents
cents2 = dollars2 * 100

# Loop through each coin and print the amount of coins you can get out of cents  
# then get the remainder of the division and reasign to cents
for coin in coins:
    print(f"{cents2 // coin[1]} {coin[0]}(s)")
    cents2 = cents2 % coin[1]