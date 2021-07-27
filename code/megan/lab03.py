cents = float(input("Please enter a dollar amount: "))

quarter = cents // 25
dimes = cents % 25

dime = dimes // 10
nickels = dimes % 10

nickel = nickels // 5
pennies = nickels % 5

penny = cents // 1

print(f"You have {quarter} quarters")
print(f"You have {dimes} dimes")
print(f"You have {nickels} nickles")
print(f"You have {pennies} pennies")