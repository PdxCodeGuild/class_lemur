# Class Lemur Day Course
# Lab 2, Average Numbers
# Scott Cormack
# Python 3.9.6

# Prompt user
print('This program will find the average for all numbers you input.')

# Establish empty list for user input
nums = []

# Establish loop control boolean
loop_bool = True

# Input loop
while loop_bool:
    user_input = input('Please enter a number or type "done" to continue: ')
    # Turn user input to a lowercase string to avoid errors
    # user_input_lower = user_input.lower
    if user_input != 'done':
        # Convert user input to integer
        user_input_int = int(user_input)
        # Add user number to list
        nums.append(user_input_int)
    else:
        loop_bool = False    

# Loop to list all input numbers
print('You have input the following numbers:')
list_length = len(nums)
for i in range(list_length):
    print(nums[i], sep=', ')

# Loop to calculate average numbers
total = 0
average = 0

for i in range(list_length):
    total = total + nums[i]

average = total / (list_length +1)

# Print results
print(f'The average of all input numbers is {average}.')