'''
8/10
dbrunk
implement linear and binary search to sort 
and retrieve desired value
'''

'''
version 1
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8]
def linear_search(num_list, value):
    # value = num_list[0]
    for item in num_list:
        if item == value:
            # value = item
            return item

index = nums.index(linear_search(nums, 7))
# print(nums, index)

# ---------------------------------------------------
'''
version 2
'''

nums2 = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_search(num_list2, value):
    first = 0
    last = len(num_list2) -1
    target = value

    while first <= last and not target:
        mid = (first + last) // 2
        if num_list2[mid] == target:
            target = True
        else:
            if value < num_list2[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return target
    # print(last)

index = nums2.index(binary_search(nums2, 7))
print(nums2, index)
# binary_search(nums2, 5)
