# Class Lemur - Day Course
# Lab 8, Credit Card Validation
# Scott Cormack
# Python 3.9.6

# Function to check if credit card number is valid
def cc_validate(num):
    # Turn string into a list of integers
    int_list = list(map(int, num))
    # Save check digit
    check_num = int_list[-1:]
    del int_list[-1]
    print(check_num)
    print(int_list)
    # Reverse integer list
    int_list.reverse()
    print(int_list)
    # Double every other digit
    for i in range(len(int_list)):
        if i % 2 == 0:
            int_list[i] = int_list[i] * 2
    print(int_list)
    # Subtract 9 from all numbers over 9
    for i in range(len(int_list)):
        if int_list[i] > 9:
            int_list[i] = int_list[i] - 9
    print(int_list)
    # Sum of all numbers
    total = sum(int_list)
    print(total)
    # Pull second digit from sum and check against check digit
    total_check_str = str(total)
    total_check_list = list(map(int, total_check_str))
    total_check = total_check_list[-1:]
    if total_check == check_num:
        print(f'{num} is a valid credit card number.')
    else:
        print(f'{num} is not a valid credit card number')

# Prompt user
ctrl = True
while ctrl == True:
    number_str = input('Input 16 digit credit card number to validate (ex 1234567890123456): ')
    if len(number_str) != 16 or number_str.isalpha:
        print('Please enter a valid 16 digit credit card number.')
    if len(number_str) == 16 and number_str.isnumeric:
        cc_validate(number_str)
        ctrl = False