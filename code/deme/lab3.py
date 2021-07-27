total = float(input("Enter amount: "))

total = total * 100
quarters = total // 25
dimes = (total -(quarters * 25)) // 10
# nickels = ((total - (quarters * 25)) + (total - (dimes * 10))) % 5
print(total, quarters, dimes)