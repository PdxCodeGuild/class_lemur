'''Lab 15 David Swartwood
Part 5 - Quicksort (optional)
Quicksort is one of the most efficient sorting algorithms. 
It works by swapping elements on either side of a pivot value.
'''

from math import floor

def qsort(nums):
    lo=0
    hi=len(nums)-1
    for _ in range(2):
        if lo < hi:
            p=part(nums,lo,hi)
        if lo<p:
            p=part(nums, lo, p)
        if p+1<hi:
            p=part(nums,p+1,hi)
    return nums




def part(nums,lo,hi):
    pivot=nums[floor((hi+lo)/2)]
    i=lo
    j=hi
    while True:
        while nums[i]<pivot:
            i+=1
            
        while nums[j]>pivot:
            j-=1

        if i>=j:
            return j
            
        flip=nums[i]
        nums[i]=nums[j]
        nums[j]=flip





nums=[54,2,5,12,14,82,16]
        

            
print(qsort(nums))