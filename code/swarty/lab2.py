
"""
Lab 2 David Swartwood
We're going to average a list of numbers. Start with the following list, iterate through it, 
keeping a 'running sum', then divide that sum by the number of elements in that list. 
Remember len will give you the length of a list."""


nums = [5, 0, 8, 3, 4, 1, 6]
total=0
# loop over the elements
for num in nums:
    total += num
    print(num, total)
    
    

# loop over the indices
for i in range(len(nums)):
    print(nums[i])
    total += num
print(i+1)