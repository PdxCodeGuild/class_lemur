'''
create an average of numbers
copied code from lab
'''

# nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# # for num in nums:
# #     print(num)

# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])

# run_sum = sum(nums) #/ len(nums)

# print(run_sum)

# -------------------------------------------------------------------------

nums = []

# print(type(user_num))
# print(nums)


i = True

while i == True :
    user_num = input('input a number or type "done": ') 
    
    if user_num == 'done':
        print(sum(nums) / len(nums))
        break
    
    user_num = int(user_num)
    nums.append(user_num)
    print(nums)



