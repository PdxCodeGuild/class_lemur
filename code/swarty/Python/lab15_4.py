'''Lab 15 David Swartwood
Part 4 - Insertion Sort (optional)
Implement insertion sort, which like bubble sort is also O(n^2),
but is efficient at placing new values into an already-sorted list.
'''

def insert_sort(nums):
    i=1
    while i<len(nums):
        j=i
        while j > 0 and nums[j-1] > nums[j]:
            fore=nums[j-1]
            nums[j-1]=nums[j]
            nums[j]=fore
            j-=1
        i+=1
    return nums

nums=[54,2,5,12,14,82,16]
        

            
print(insert_sort(nums))