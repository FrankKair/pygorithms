#!/usr/bin/env python3


# Time: O(n^2)
# Space: O(1)
def selection_sort_in_place(list):
    for i in range(0, len(list) - 1):
        minimum = i
        for j in range(i + 1, len(list)):
            if list[minimum] > list[j]:
                minimum = j
        temp = list[i]
        list[i] = list[minimum]
        list[minimum] = temp


# Time: O(n^2)
# Space: O(n)
def selection_sort(list):
    list = list
    for i in range(0, len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp
    return list


# Examples
list_to_sort = [2, 7, 4, 1, 5, 3]
selection_sort_in_place(list_to_sort)
print(list_to_sort)

sorted_list = selection_sort([2, 7, 4, 1, 5, 3])
print(sorted_list)
