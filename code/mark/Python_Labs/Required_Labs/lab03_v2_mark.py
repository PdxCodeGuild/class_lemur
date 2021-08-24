import math
coins = [
    ('half-dollar', 'half-dollars', 50),
    ('quarter', 'quarters', 25),
    ('dime', 'dimes', 10),
    ('nickel', 'nickels', 5),
    ('penny', 'pennies', 1)
]

def get_user_input():
    while True:
        try:
            user_input = float(input("Enter a dollar amount: "))
        except ValueError:
            print("Invalid entry.  Please enter a dollar amount.")
            continue
        else:
            break
    number_of_pennies = math.floor(user_input * 100)
    return number_of_pennies

def make_change(number_of_pennies, coins):
    result_dict = {}
    while number_of_pennies > 0:
        for i in range(len(coins)):
            if number_of_pennies > coins[i][2]:
                number_of_coins = number_of_pennies // coins[i][2]
                if number_of_coins > 1:
                    result_dict[coins[i][1]] = number_of_coins
                    number_of_pennies %= coins[i][2]
                else:
                    result_dict[coins[i][0]] = number_of_coins
                    number_of_pennies %= coins[i][2]
    return result_dict

def convert_dict_to_lists(result_dict):
    keys_list = list(result_dict.keys())
    values_list = list(result_dict.values())
    return keys_list, values_list

def print_result(keys_list, values_list):
    for i in range(len(keys_list)):
        print(f"{values_list[i]} {keys_list[i]}", end="")
        if i < len(keys_list)-2:
            print(", ", end="")
        elif i == len(keys_list)-2:
            print(", and ", end="")

def main(coins):
    number_of_pennies = get_user_input()
    result_dict = make_change(number_of_pennies, coins)
    keys_list, values_list = convert_dict_to_lists(result_dict)
    print_result(keys_list, values_list)

main(coins)
