# Heap sort used max/min heap to sort the input by building a heap and continuously swapping max/min element with the last
# element and heapify the new root element. Repeats this process until all elements are sorted.
# Note: We will use max heap for this implementation.

# Build heap:
#   1. Build a max heap of the input list.

# Sort and Heapify:
#   1. Extract max (i.e., the first element in the heap) from the heap and swap it with the last element in the list.
#   2. Decrement the heap size to exclude the last element (which is the largest element) from max heapify.
#   3. Max heapify the new root node.

# Time Complexity:
#   1. Building heap - O(n log n)
#   2. Sort and heapify
#       1. We will need to do "n" swaps for all elements in the input.
#       2. Each heapify from root takes O(log n).
#       3. Hence, O(n * log n) = O(n log n).
#   3. Total: O(n log n) + O(n log n) ≈ O(n log n).

# Space Complexity:
#   1. Since it does in-place sort, it would be O(1).

# Algorithm:
#   1. Let the given input list "a".
#   2. Build a max heap of "a".
#   3. Loop through the length of input "a" to sort all elements.
#       1. Extract the max at the root i.e., a[0] and swap it with the last element i.e., a[len - 1].
#       2. Virtually decrement the heap size by 1 to exclude the last element (which is the largest in the current heap)
#          from max heapify.
#       3. Max heapify from the new root node.
#       4. Repeat steps 3.1 - 3.4 until the loop ends.

from custom_heap import CustomHeap


def heap_sort(a):
    heap = CustomHeap.build_max_heap(a)
    heap_size = len(heap)

    while heap_size > 0:  # Stop when there is only one element in the heap, which will be the smallest element
        a[0], a[heap_size - 1] = a[heap_size - 1], a[0]
        heap_size -= 1
        CustomHeap.max_heapify(heap, 0, heap_size)


import random
from Utils.check_perf import check_performance

# s = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
s = [random.randrange(0, 100000) for _ in range(10000)]
# s = sorted(s)
s1 = s.copy()
check_performance(heap_sort, s)
print(s)
print(sorted(s1) == s)
