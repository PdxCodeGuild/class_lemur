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
    length = len(numbers) - 1
    low = numbers[0]
    high = numbers[length]
    while numbers[low] <= numbers[high]:
        mid = ((numbers[low] + numbers[high]) // 2)
        if numbers[mid] < numbers[num]:
            numbers[low] = numbers[mid] + 1
        elif numbers[mid] > numbers[num]:
                numbers[high] = numbers[mid] - 1
        else:
            print(f'Your number was found at index {numbers.index(mid)}.')

bin_search(nums, 6)