user_input = float(input("Please enter a dollar amount: "))
# 1.83
cents = user_input * 100

quarter = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5


print(f"You have {quarter} quarters")
print(f"You have {dimes} dimes")
print(f"You have {nickels} nickles")
print(f"You have {cents} pennies")