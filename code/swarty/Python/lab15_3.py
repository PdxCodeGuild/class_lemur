'''Lab 15 David Swartwood
Part 3 - Bubble Sort (optional)
Bubble sort is one of the simplest and least efficient sorting algorithms.
We repeatedly loop over the list, comparing each number to the one next to it,
and swapping them if needed.
'''

def bubble_sort(nums):
    n=len(nums)
    check =0
    checker =1
    while checker != check:
        checker=check
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                fore=nums[i-1]
                nums[i-1]=nums[i]
                nums[i]=fore
                checker+=1
    return nums


nums=[54,2,5,12,14,82,16]
        

            
print(bubble_sort(nums))



