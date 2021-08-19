# Declare nums array and running_sum
nums = [5, 0, 8, 3, 4, 1, 6]
running_sum= 0

# Define function to average numbers
def average(number1, number2):
    average = number1 / number2
    return average

# Use for loop to iterte through nums and add each to running_sum
for num in nums:
    running_sum += num

# Use function average and print result.
average_num = average(running_sum, len(nums))

print(f"average: {average_num}")

# Set running_sum to 0 and initialize empty array.
running_sum = 0
nums2 = []

# Use while loop get user input
while True:
    
    num2 = int(input("Please enter a number, or a negative to exit: "))
    if num2 < 0:
        break
    nums2.append(num2)

# Use function average and print result.

for num in nums2:
    running_sum += num

average_num2 = average(running_sum,len(nums2))

print(f"average: {average_num2}")
