"""
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    shifts = 0
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        # if compare from the beginning, need to move all the way to find position to insert
        # then move all elements after that position to the right.
        # However, only one comparision in while condition
        while j >= 0 and arr[j] > temp:
            # must have j >= 0. If arr[0] > temp, move arr[0] to position 1, j = -1. Exception.
            # set the condition in while loop
            arr[j + 1] = arr[j]
            shifts += 1
            j = j - 1
        arr[j + 1] = temp
    return shifts


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(insertionSort2(n, arr))
"""

"""
# counting sort, forget
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    frequency = [0 for _ in range(100)]
    for num in arr:
        frequency[num] += 1
    for i in range(1, len(frequency)):
        frequency[i] = frequency[i] + frequency[i - 1]
    result = [0 for _ in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        result[frequency[arr[i]] - 1] = arr[i]
        frequency[arr[i]] -= 1
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(' '.join(result))
"""

"""
#!/bin/python3

import math
import os
import random
import re
import sys


def quickSort(arr):
    pivot = arr[0]
    left, middle, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)
    return left + middle + right


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print(' '.join(map(str, result)))
"""

"""
# closest numbers
# don't need to store all differences and all pairs in a dictionary
#!/bin/python3
import math
import os
import random
import re
import sys


def closestNumbers(arr):
    sorted_arr = sorted(arr)
    min_difference = sorted_arr[1] - sorted_arr[0]
    result = []
    for i in range(2, len(sorted_arr)):
        if sorted_arr[i] - sorted_arr[i - 1] < min_difference:
            result.clear()
            result.append(sorted_arr[i - 1])
            result.append(sorted_arr[i])
            min_difference = sorted_arr[i] - sorted_arr[i - 1]
        elif sorted_arr[i] - sorted_arr[i - 1] == min_difference:
            result.append(sorted_arr[i - 1])
            result.append(sorted_arr[i])
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    print(result)
    print(' '.join(map(str, result)))
"""

"""
#!/bin/python3
# find median, find ith smallest element, use quickSelect, divide and conquer,
# expected run time O(n). Compared to quickSort: expected runtime: O(nlgn)
# index is for the whole string arr, ith smallest element is for substring arr[p: r + 1]
import math
import os
import random
import re
import sys
from random import randint


def randomized_partition(arr, p, r):
    # both ends index p and r inclusive in substring
    q = randint(p, r)
    # a random position value as pivot
    pivot = arr[q]
    arr[q] = arr[r]
    arr[r] = pivot
    # now, last position is the pivot, find the correct position the pivot should go
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i = i + 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[i + 1]
    arr[i + 1] = pivot
    arr[r] = temp
    return i + 1


def randomized_selection(arr, p, r, i):
    if p == r:
        return arr[p]
    # find i th smallest value in substring arr[p: r + 1]
    index_to_place_pivot = randomized_partition(arr, p, r)
    # pivot is the kth smallest element in substring
    k = index_to_place_pivot - p + 1
    if k == i:
        return arr[index_to_place_pivot]
    if i < k:
        return randomized_selection(arr, p, index_to_place_pivot - 1, i)
    return randomized_selection(arr, index_to_place_pivot + 1, r, i - k)


def findMedian(arr):
    return randomized_selection(arr, 0, len(arr) - 1, len(arr) // 2 + 1)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    print(result)
"""

"""
# The full counting sort
#!/bin/python3

import math
import os
import random
import re
import sys


def countSort(arr):
    frequency = [0 for _ in range(100)]
    for i in range(len(arr)):
        frequency[int(arr[i][0])] += 1
        if i < len(arr) // 2:
            arr[i][1] = '-'
    for i in range(1, len(frequency)):
        frequency[i] += frequency[i - 1]
    strings_list = ["" for _ in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        strings_list[frequency[int(arr[i][0])] - 1] = arr[i][1]
        frequency[int(arr[i][0])] -= 1
    print(' '.join(strings_list))


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
"""

"""
# Lily's homework
#!/bin/python3
import math
import os
import random
import re
import sys
# can refer to the idea of quickSort, but quickSort is recursive, exceed max depth of recursion
# all distinct values in arr
# swap, no algor to get min swaps. Just go as normal. Refer to quickSort, where the number should be?
# Not very similar to quickSort
# Be careful when swapping, values and indices.
# Be careful to make copies, arr will be changed with in place swapping.


def compute_swaps(arr, target_arr, value_index):
    # dict: values: indexes
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != target_arr[i]:
            # Very similar to Student class, CS146 Programming 1.
            # Be careful with values and indexes when swapping!
            # first, record index to swap with
            target_index = value_index[target_arr[i]]
            # swap elements
            temp = arr[i]
            arr[i] = arr[target_index]
            arr[target_index] = temp
            swaps += 1
            # change indexes in map
            # already swapped, don't use arr[i], instead, use temp
            # element stored in arr[i] is target_arr[i]
            value_index[temp] = target_index
            value_index[target_arr[i]] = i
    return swaps


def lilysHomework(arr):
    # Why made a copy? in compute_swaps, it changes arr. In place swap.
    value_index = {}
    for i in range(len(arr)):
        value_index[arr[i]] = i
    asc_arr = sorted(arr)
    desc_arr = asc_arr[::-1]
    arr_copy = arr.copy()
    value_index_copy1 = value_index.copy()
    value_index_copy2 = value_index.copy()
    # Be careful! Using copies. After first funcall, both arr and value_index will be changed.
    swaps_asc = compute_swaps(arr, asc_arr, value_index_copy1)
    # Compare to the case: compare arr with sorted(arr)[::-1].
    # It is equivalent to compare arr[::-1] with sorted(arr[::-1])
    swaps_desc = compute_swaps(arr_copy, desc_arr, value_index_copy2)
    return min(swaps_asc, swaps_desc)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = lilysHomework(arr)
    print(result)
"""


#  Fraudulent Activity Notifications
#!/bin/python3

import math
import os
import random
import re
import sys


def activityNotifications(expenditure, d):
    sub_list = expenditure[:d]
    value_frequency_accum = [0 for _ in range(201)]
    for num in sub_list:
        value_frequency_accum[num] += 1
    for i in range(1, 201):
        value_frequency_accum[i] = value_frequency_accum[i - 1] + value_frequency_accum[i]
    sub_sorted = [0 for _ in range(d)]
    value_frequency_accum_copy = value_frequency_accum.copy()
    for i in range(d - 1, -1, -1):
        sub_sorted[value_frequency_accum_copy[sub_list[i]] - 1] = sub_list[i]
        value_frequency_accum_copy[sub_list[i]] -= 1
    if d % 2:
        sub_median = sub_sorted[d // 2]
    else:
        sub_median = (sub_sorted[d // 2] + sub_sorted[d // 2 - 1]) / 2
    notifications = 0
    if expenditure[d] >= 2 * sub_median:
        notifications += 1
    for i in range(d + 1, len(expenditure)):
        # delete expenditure[i - d - 1], add expenditure[i - 1]
        index_to_delete = value_frequency_accum[expenditure[i - d - 1]] - 1
        sub_sorted = sub_sorted[:index_to_delete] + sub_sorted[index_to_delete + 1:]
        for j in range(expenditure[i - d - 1], len(value_frequency_accum)):
            value_frequency_accum[j] -= 1
        for j in range(expenditure[i - 1], len(value_frequency_accum)):
            value_frequency_accum[j] += 1
        index_to_add = value_frequency_accum[expenditure[i - 1]] - 1
        sub_sorted = sub_sorted[:index_to_add] + [expenditure[i - 1]] + sub_sorted[index_to_add:]
        if d % 2:
            sub_median = sub_sorted[d // 2]
        else:
            sub_median = (sub_sorted[d // 2] + sub_sorted[d // 2 - 1]) / 2
        if expenditure[i] >= 2 * sub_median:
            notifications += 1
    return notifications


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(result)
