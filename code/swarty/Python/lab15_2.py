'''
Part 2 - Binary Search
Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.

Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest.
Loop while low is less then high.
For each iteration, calculate a third index mid which is in the middle between low and high
If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop.
If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.
'''
from math import floor



def binary_search(nums, value):
    low=0
    high=len(nums)-1
    while low <= high:
        middle=floor((low+high)/2)
        if nums[middle]<value:
            low=middle+1
        elif nums[middle]>value:
            high=middle-1
        else:
            return middle
        print(low,middle,high)

#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 6)
print(index) # 5