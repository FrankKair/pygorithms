#!/usr/bin/env python3


# Time: O(n^2) with average O(n log n)
# Space: O(1)
def quicksort(array):
    def quicksort(array, left, right):
        if left >= right:
            return
        pivot = array[int((left + right) / 2)]
        index = partition(array, left, right, pivot)
        quicksort(array, left, index - 1)
        quicksort(array, index, right)

    def partition(array, left, right, pivot):
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                temp = array[left]
                array[left] = array[right]
                array[right] = temp
                left += 1
                right -= 1
        return left

    quicksort(array, 0, len(array) - 1)


l = [4, 8, 7, 1, 3, 6, 2, 9, 5]
quicksort(l)
print(l)
