# Class Lemur Day Course
# Lab 14, Searching and Sorting
# Scott Cormack
# Python 3.9.6

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Part 1 - Linear Search

def lin_search(numbers, num):
    for i in range(len(numbers)):
        if numbers[i] == num:
            print(f'Your number was found at index {numbers.index(i)}.')
            break
    
lin_search(nums, 6)

# Part 2 - Binary Search
def bin_search(numbers, num):
    low = 0
    mid = 0
    high = len(numbers) - 1
    while high >= low:
        mid = (high + low) // 2
        if numbers[mid] < num:
           low = mid + 1
        elif numbers[mid] > num:
           high = mid -1
        else:
            print(f'Your number was found at index {numbers.index(mid)}.')
            break


bin_search(nums, 6)