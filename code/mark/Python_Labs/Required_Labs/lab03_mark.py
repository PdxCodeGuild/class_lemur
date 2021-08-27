import math

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

def make_change(number_of_pennies):
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
            if number_of_coins == 1:
                result_dict["dime"] = number_of_coins
            else:
                result_dict["dimes"] = number_of_coins
            number_of_pennies = number_of_pennies%10
        elif number_of_pennies > 5:
            number_of_coins = number_of_pennies//5
            if number_of_coins == 1:
                result_dict["nickel"] = number_of_coins
            else:
                result_dict["nickels"] = number_of_coins
            number_of_pennies = number_of_pennies%5
        else:
            number_of_coins = number_of_pennies
            if number_of_coins == 1:
                result_dict["penny"] = number_of_coins
            else:
                result_dict["pennies"] = number_of_coins
            number_of_pennies = 0
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

def main():
    number_of_pennies = get_user_input()
    result_dict = make_change(number_of_pennies)
    keys_list, values_list = convert_dict_to_lists(result_dict)
    print_result(keys_list, values_list)

main()
