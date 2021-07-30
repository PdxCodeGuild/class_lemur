# #version1
nums = [1, 2, 3, 4, 5]
x = 0
for num in nums:
    x += num
print(x)
average = x / len(nums)
print(average)

#version2
nums = []
done = False
while done == False:
    user_input = input("enter a number, or 'done': ")
    if user_input != 'done':
        nums.append(int(user_input))
    else:
        done = True
        break
sum = 0
for num in nums:
    sum += num
print(f"The sum of the numbers is {sum}")
average = sum / len(nums)
print(f"The average of the numbers is {average}")


        



