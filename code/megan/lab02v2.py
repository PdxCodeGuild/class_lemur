nums = []

user_input = input("Please enter a number: ")

nums.append(int(user_input))

while True:
    more_input = input('Please enter another number, or \'done\' to exit: ')

    if more_input == 'done':
        break

    nums.append(int(more_input))  
    
    print(nums)

print(sum(nums))
print(sum(nums) / len(nums))

