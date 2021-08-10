'''Part One: Linear Search'''

# def linear_search(nums, value):
#     for i in range(len(nums)):
#         if nums[i] == value:
#             return i

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) 


'''Part Two: Binary Search'''

def binary_search(nums, value):

    low = 0
    high = len(nums)
    mid = int(len(nums) / 2)

    while low < high:

        for i in range(len(nums)):

            # nums.sort()

            if mid == value:
                return i

            elif value > mid:
                low = mid
                
            elif value < mid:
                high = mid
        

nums = [1, 2, 3, 4, 5, 6, 7, 8]

index = binary_search(nums, 6)
print(index)