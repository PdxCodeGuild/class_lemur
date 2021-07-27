import math

user_input = float(input("Enter a dollar amount: "))
number_of_pennies = math.floor(user_input * 100)
result_dict = {}
while number_of_pennies > 0:
    if number_of_pennies > 25:
        number_of_coins = number_of_pennies//25
        if number_of_coins == 1:
            result_dict["quarter"] = number_of_coins
        else:
            result_dict["quarters"] = number_of_coins
        number_of_pennies = number_of_pennies%25
    elif number_of_pennies > 10:
        number_of_coins = number_of_pennies//10
        result_dict["dime"] = number_of_coins
        number_of_pennies = number_of_pennies%10
    elif number_of_pennies > 5:
        number_of_coins = number_of_pennies//5
        result_dict["nickel"] = number_of_coins
        number_of_pennies = number_of_pennies%5
    else:
        number_of_coins = number_of_pennies
        result_dict["penny"] = number_of_coins
        number_of_pennies = 0

print(result_dict)

