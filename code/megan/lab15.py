'''Part One: Linear Search'''


# def linear_search(nums, value):
#     for i in range(len(nums)):
#         if nums[i] == value:
#             return i

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 7)
# print(index)



'''Part Two: Binary Search'''


def binary_search(nums, value):
    nums.sort()

    low = 0
    high = len(nums) - 1

    while low < high:

        mid = (high + low) // 2

        for i in range(len(nums)):

            if nums[mid] == value:
                return mid

            elif value < mid:
                high = mid - 1

            elif value > mid:
                low = mid + 1
                

nums = [1, 2, 3, 4, 5, 6, 7, 8]

index = binary_search(nums, 7)
print(index)