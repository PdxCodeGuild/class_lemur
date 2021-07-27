
"""
Lab 2 David Swartwood
We're going to average a list of numbers. Start with the following list, iterate through it, 
keeping a 'running sum', then divide that sum by the number of elements in that list. 
Remember len will give you the length of a list."""

#nums = [5, 0, 8, 3, 4, 1, 6]
nums= []
while True:
    added=input("enter a number for the list (if done hit enter):  ")
    if added == "":
        break
    added = int(added)
    nums.append(added)
print(nums)


total=0
# loop over the elements
#for num in nums:
#    total += num
#    print(num, total)
    
    

# loop over the indices
for i in range(len(nums)):
#    print(nums[i])
    total += nums[i]
print(total/(i+1))