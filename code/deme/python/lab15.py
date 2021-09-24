import math
nums = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(nums, number):
    for i, num in enumerate(nums):
        if num == number:
            return i

print(linear_search(nums, 7))

def binary_search(nums):
    # nums.sort()
    low = 0
    high = len(nums) - 1
    target_num = int(input("Enter a number: "))

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target_num:
            print(mid)
            break
        elif nums[mid] > target_num:
            high = mid - 1
            print(f"The new high is {high}")
        elif nums[mid] < target_num: 
            low = mid + 1
            print(f"The new low is {mid}")

binary_search(nums)