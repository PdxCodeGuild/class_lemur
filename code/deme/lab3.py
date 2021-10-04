total = float(input("Enter amount: "))

total = int(total * 100)
quarters = (total) // 25
dimes = (total -(quarters* 25)) // 10
nickels = ((total - (quarters * 25)) - (dimes * 10)) // 5
pennies = ((total - (quarters * 25)) - (dimes * 10)) - (nickels * 5) // 1
print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies.")


