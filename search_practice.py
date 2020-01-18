"""
#!/bin/python3

import math
import os
import random
import re
import sys
# save while checking membership
# in discussion: duplicated prices
# probably in C, Java, searching: binary search
# in python, just check membership
# hashmap: value: index: enumerate dict


def icecreamParlor(m, arr):
    seen = dict()
    for i, price in enumerate(arr):
        if m - price in seen:
            indexes = [seen[m - price] + 1, i + 1]
            return sorted(indexes)
        seen[price] = i


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        print(' '.join(map(str, result)))
"""


"""
# may also use subtraction for Counter: for each key: subtract frequency
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def missingNumbers(arr, brr):
    missing_freq = Counter(arr)
    orig_freq = Counter(brr)
    return sorted(num for num in orig_freq if orig_freq[num] != missing_freq.get(num, 0))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    print(result)
"""

"""
# The sum to the left of this element == the sum to the right of this element
# didn't use two variables left_sum right_sum and update them
# math trick

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.


def balancedSums(arr):
    total = sum(arr)
    so_far = 0
    for i in arr:
        if total - i == 2 * so_far:
            return "YES"
        so_far += i
    return "NO"


if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)
"""

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.


def connectedCell(matrix):
    # dfs
    visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                area = dfs_visit(i, j, matrix, visited, 0)
                if area > max_area:
                    max_area = area
    return max_area


def dfs_visit(i, j, matrix, visited, area):
    visited[i][j] = 1
    area += 1
    neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    for dr, dc in neighbors:
        if 0 <= i + dr < len(matrix) and 0 <= j + dc < len(matrix[0]) and visited[i + dr][j + dc] == 0 and matrix[i + dr][j + dc] == 1\:
            # update total steps after a branch, quite wierd. accumulate branch by branch
            area = dfs_visit(i + dr, j + dc, matrix, visited, area)
    return area
/l

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    result = connectedCell(matrix)
    print(result)
"""

