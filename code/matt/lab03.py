dollars = float(input("Enter a dollar amount: "))

# Convert dollars to cents
cents = dollars * 100

quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickel = cents // 5
cents = cents % 5

print(cents)
pennies = cents % 10

print(f"{quarters} quarters, {dimes} dimes, {nickel} nickels {pennies} pennies.")