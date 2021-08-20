# Class Lemur Day Course
# Lab 15, Searching and Sorting
# Scott Cormack
# Python 3.9.6

import math

nums = [12, 13, 16, 24, 78, 89, 90, 99]

# Part 1 - Linear Search

def lin_search(numbers, num):
    for i in range(len(numbers)):
        if numbers[i] == num:
            print(f'Your number was found at index {i}.')
            break
    
lin_search(nums, 99)

# Part 2 - Binary Search
def bin_search(numbers, num):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = math.floor((high + low) / 2)
        if numbers[mid] < num:
           low = mid + 1
        elif numbers[mid] > num:
           high = mid - 1
        else:
            print(f'Your number was found at index {mid}.')
            break

bin_search(nums, 99)