# Sorts by dividing the input array into a sorted and an unsorted subarrays.
# Starts with first element as sorted subarray and remaining n-1 elements as unsorted subarray.
# Compares each element in the unsorted subarray with the elements in the sorted subarray from right to left, and inserts the unsorted element into the appropriate position in the sorted subarray.
# This works well with small or nearly sorted arrays.

# Time Complexity: O(n^2) [can be O(n) in case of small or nearly sorted inputs]
# Space Complexity: O(1) [in-place sort, no extra storage]

# Algorithm:
#   1. Let the given input array "a".
#   2. Initialize sorted_until_index = 0
#   3. Loop (i = 1) through remaining elements.
#       1. Initialize insertion_index = sorted_until_index
#       2. For each outer iteration i, loop (j = sorted_until_index) through all elements in the sorted subarray from sorted_until_index to index "0" in a nested loop.
#           1. Find the appropriate sorted position for a[i] within the sorted subarray.
#               1. Compare a[i] and a[j].
#               2. If a[i] < a[j] then update insertion_index = j.
#               3. If a[i] >= a[j] then end the loop as we don't need to compare further.
#           2. Repeat steps 3.2.1 until the loop ends.
#       3. Shift all larger elements to one position right from the insertion index and insert a[i] at the insertion index.
#       4. Increment sorted_until_index by 1.
#       5. Repeat steps 3.1-3.4 until the loop ends.


def insertion_sort(a: list):
    sorted_until_index = 0
    for i in range(1, len(a)):
        insertion_index = i  # Assuming a[i] is already in the correct sorted position
        for j in range(sorted_until_index, -1, -1):
            if a[i] < a[j]:
                insertion_index = j
            elif a[i] >= a[j]:
                break
        if insertion_index != i:  # This check can be optional as it just avoids additional method invocation overhead
            shift_elements(a, insertion_index, i)
        sorted_until_index += 1


def shift_elements(a, insertion_index, end_index):
    # Interesting fact: Although, this would shift more elements during both insert and pop operations, this would be consistently faster
    #   than the below "shift_elements_manual" function due to under the hood Python list optimizations.
    a.insert(insertion_index, a.pop(end_index))


def shift_elements_manual(a, insertion_index, end_index):
    insertion_value = a[end_index]
    for i in range(end_index, insertion_index, -1):
        a[i] = a[i - 1]
    a[insertion_index] = insertion_value


import random
from Utils.check_perf import check_performance

# s = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
s = [random.randrange(0, 100000) for _ in range(10000)]
check_performance(insertion_sort, s)
print(s)
