# Merge sort uses divide and conquer (merge) approach.
# Divide:
#   1. Split the input list into smaller (equal) halves.
#   2. Stop when every smaller half has only one element.
# Sort and Merge:
#   1. Take each pair of smaller halves and merge them by placing smaller elements before the larger elements.
#   2. Stop when all halves are merged into the full list.

# Time Complexity: O(n log n)
#   Divide:
#    1. Splitting into smaller (equal) halves will form a binary tree structure with "n" elements at root node and "1" element at leaf nodes.
#    2. Hence, splitting stops when there is only one element i.e., n/2^k = 1, where "k" is the number of splits or in other words,
#       total work for divide operation.
#    3. So, k = log n
#   Sort and Merge:
#    1. Each merge will take O(n) work i.e.,
#       "n" merges of "1" elements -> n * 1
#       "n/2" merges of "2-pair" elements -> (n/2) * 2
#       ....
#       "2" merges of "n/2" elements -> 2 * (n/2)
#       "1" merges of "n" elements -> 1 * n
#   2. Hence, the total work for each merge is O(n).
#
#   Total Time Complexity = O(log n) levels * O(n) = O(n log n)
#
# Space Complexity: O(n)

# Algorithm:
#   1. Let the given input list "a".
#   2. Use recursion to split the input list into smaller lists recursively until each smaller list has only one element (base case).
#       1. Split list into left and right halves.
#           1. Compute the middle index of the current "a".
#           2. Set left = a[0:mid+1].
#           3. Set right = a[mid+1:].
#       2. Return when a smaller half has only one element.
#       3. Basically, this will split the initial left half first and then the initial right half recursively.
#   2. Sort and merge the left and right halves recursively and return the merged result.
#       1. This will start sorting and merging from the 1-element smallest halves and continue until the full list is merged.
#           1. Merge left and right.
#               1. Initialize two index pointers for left and right to "0".
#               2. left_index = 0, right_index = 0.
#               3. Compare a[left_index] and a[right_index].
#                   1. Add the smallest of two into a result list.
#                   2. Advance the index pointer of the smaller value.
#                       1. This will also ensure skipping already sorted elements in both halves and iterating only once (O(n)) through both combinedly.
#                   3. If both values are equal then add both elements into the result list and advance both pointers.
#               4. Repeat steps 2.1.1.1 - 2.1.1.3 until either half is exhausted.
#               5. Add the remaining elements from the non-exhausted half into the result list.
#       2. Basically, this will merge the initial left half first and then the initial right half recursively.


def merge_sort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    left = a[0:mid]
    right = a[mid:]

    return merge(
        merge_sort(left),
        merge_sort(right)
    )


def merge(left, right):
    left_index = right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        elif right[right_index] < left[left_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.extend([left[left_index], right[right_index]])
            left_index += 1
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


import random
from Utils.check_perf import check_performance

# s = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
s = [random.randrange(0, 100000) for _ in range(10000)]
print(check_performance(merge_sort, s))
