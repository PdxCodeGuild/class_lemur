#-----------------------------------------------------------------------------------------------------------
# Linear Search
#-----------------------------------------------------------------------------------------------------------
def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return "Did not find value in list"


nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 87)
print(index)

#-----------------------------------------------------------------------------------------------------------
# Binary Search
#-----------------------------------------------------------------------------------------------------------
def binary_search(nums, value):
    nums.sort()
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return "Did not find value in list"

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 7)
print(index) 

#-----------------------------------------------------------------------------------------------------------
# Bubble Sort
#-----------------------------------------------------------------------------------------------------------

def bubble_sort(list_of_items):
    list_length = len(list_of_items)
    swapped = True
    while swapped is True:
        swapped = False
        for i in range(1,list_length):
            if list_of_items[i-1] > list_of_items[i]:
                list_of_items[i-1], list_of_items[i] = list_of_items[i], list_of_items[i-1]
                swapped = True
    return list_of_items


list_of_items = [5,4,2,7,8,2,3]
print(bubble_sort(list_of_items))

#-----------------------------------------------------------------------------------------------------------
# Insertion Sort
#-----------------------------------------------------------------------------------------------------------

def insertion_sort(list_of_items):
    i = 1
    while i < len(list_of_items):
        j = i
        while j > 0 and list_of_items[j-1] > list_of_items[j]:
            list_of_items[j], list_of_items[j-1] = list_of_items[j-1], list_of_items[j]
            j -= 1
        i += 1
    return list_of_items

list_of_items = [5,4,2,7,8,2,3]
print(insertion_sort(list_of_items))

#-----------------------------------------------------------------------------------------------------------
# Quick Sort
#-----------------------------------------------------------------------------------------------------------

def quicksort(items_list):
    quicksort_recursion(items_list, 0, len(items_list) - 1)
    return items_list

def quicksort_recursion(items_list, low, high):
    if low < high:
        pivot = partition(items_list, low, high)
        quicksort_recursion(items_list, low, pivot)
        quicksort_recursion(items_list, pivot + 1, high)

def partition(items_list, low, high):
    pivot = items_list[(high+low)//2]
    i = low 
    j = high
    while True:
        while items_list[i] < pivot:
            i += 1 
        while items_list[j] > pivot:
            j -= 1
        if i >= j:
            return j
        items_list[i], items_list[j] = items_list[j], items_list[i]

list_of_items = [15,40,25,77,89,2,35,52]
print(quicksort(list_of_items))
