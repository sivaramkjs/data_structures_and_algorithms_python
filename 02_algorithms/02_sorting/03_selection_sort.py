# Sorts data by finding the "smallest value" in the input and move it to the beginning of the input sequentially.

# Time Complexity: O(n^2)
# Space Complexity: O(1) [in-place sort, no extra storage]


# Algorithm:
#   1. Let the given input array "a".
#   2. Loop through all elements as we will need to sort all elements.
#       1. Initialize current_smallest_index = i
#       2. For each outer iteration i, loop (j = i+1) through all elements after the current_smallest_index in a nested loop.
#           1. Compare a[current_smallest_index] and a[j].
#           2. if a[j] < a[current_smallest_index] then update current_smallest_index = j
#           3. Repeat steps 2.1.1-2.1.3 until the loop ends.
#       3. Swap a[i] with a[current_smallest_index]
#       4. Repeat steps 2.1-2.4 until the loop ends.

def selection_sort(a):
    for i in range(len(a)):
        current_smallest_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[current_smallest_index]:
                current_smallest_index = j
        a[i], a[current_smallest_index] = a[current_smallest_index], a[i]


import random
from Utils.check_perf import check_performance

# s = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
s = [random.randrange(0, 100000) for _ in range(10000)]
check_performance(selection_sort, s)
print(s)
