import math


def main():
    test_list = [5, 4, 3, 2, 1]

    def linear_search(value):
        for i in range(len(test_list)):
            if value in test_list:
                return test_list[i]
            else:
                return -1

    print(f'linear search index {linear_search(3)}')

    def binary_search(test_list, length_of_list, value):
        low = 0
        high = length_of_list - 1
        while low <= high:
            middle = math.floor((low + high) / 2)
            if test_list[middle] < value:
                low = middle + 1
            elif test_list[middle] > value:
                high = middle - 1
            else:
                return middle
        return -1

    print(f'binary search index {binary_search(test_list, len(test_list), 4)}')

    def bubble_sort(test_list):
        length = len(test_list)
        made_swap = True
        while made_swap is True:
            made_swap = False
            for i in range(1, length):
                if test_list[i - 1] > test_list[i]:
                    temp = test_list[i]
                    test_list[i] = test_list[i - 1]
                    test_list[i - 1] = temp
                    made_swap = True
        return test_list

    new_list = bubble_sort(test_list)
    print(new_list)

    def insertion_sort(test_list):
        i = 1
        while i < len(test_list):
            j = i
            while j > 0 and test_list[j - 1] and test_list[j]:
                temp = test_list[j]
                test_list[j] = test_list[j - 1]
                test_list[j - 1] = temp
                j -= 1
            i += 1
        return(test_list)

    test_list = [5, 4, 3, 2, 1]
    print(insertion_sort(test_list))

    def quicksort(test_list):
        quicksort_recursive(test_list, 0, len(test_list) - 1)
        return(test_list)

    def quicksort_recursive(test_list, low, high):
        if low < high:
            pivot = quicksort_partition(test_list, low, high)
            quicksort_recursive(test_list, low, pivot)
            quicksort_recursive(test_list, pivot + 1, high)

    def quicksort_partition(test_list, low, high):
        pivot = test_list[math.floor(low + (high - low) / 2)]
        i = low
        j = high
        while True:
            while test_list[i] < pivot:
                i += 1
            while test_list[j] > pivot:
                j -= 1
            if i >= j:
                return j
            temp = test_list[j]
            test_list[j] = test_list[i]
            test_list[i] = temp

    test_list = [5, 6, 3, 2, 4, 1]
    print(quicksort(test_list))


main()
