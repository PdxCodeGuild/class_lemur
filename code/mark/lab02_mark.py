# nums = [5, 0, 8, 3, 4, 1, 6]
def calculate_average(number_list):
    sum_of_list = 0
    for num in number_list:
        sum_of_list += num
        #print(sum_of_list)

    average_of_list = sum_of_list / len(number_list)
    #print(average_of_list)
    return average_of_list

def get_user_input():
    nums_list = []
    while True:
        user_input = input("\nEnter number to add to the list or 'done' to finish: ")
        if user_input == 'done':
            break
        else:
            try:
                input_float = float(user_input)
                nums_list.append(input_float)
            except ValueError:
                print("That is not a valid number")
                continue
    return nums_list

def main():
    number_list = get_user_input()
    if len(number_list) > 0:
        average_of_list = calculate_average(number_list)
        print(f"The average is: {average_of_list}")
    else:
        print("You didn't enter any numbers.")


main()