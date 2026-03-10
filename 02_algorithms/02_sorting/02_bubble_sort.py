# Sorts by bubbling up the "largest value" in iterations.
# One of the simplest sorting algorithm but also one of the least efficient.

# Time Complexity: O(n^2)
# Space Complexity: O(1) [in-place sort, no extra storage]

# Algorithm 1:
#   1. Loop through the length of the input array as we will need to sort all elements.
#       1. For each outer iteration i, loop (j) through all elements until last element in a nested loop.
#           1. if a[j] > a[j+1] then swap a[j] and a[j+1].

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


# Algorithm 2 (slightly faster due to the nested loop condition optimization based on previously sorted upper index position, which reduces nested loop iterations):
#   1. (For an input array "a") Initialize three index pointers: first to 0, second to 1 and sorted_until_index = len(a)
#   2. While sorted_until_index > 0 (if the sorted_until_index is "0" then end the loop as we already sorted until the 1st element)
#       1. While second < sorted_until_index
#           1. Compare elements at a[first] and a[second] indices.
#           2. If a[first] > a[second] then swap a[first] and a[second].
#           3. Increment first and second by 1.
#           4. Repeat steps 2.1.1-2.1.4
#       2. Reset pointers to 0 and 1 then repeat steps 2.1-2.2

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort_while_loop(a):
    first, second, sorted_until_index = 0, 1, len(a)

    while sorted_until_index > 0:
        while second < sorted_until_index:
            if a[first] > a[second]:
                a[second], a[first] = a[first], a[second]
            first = second
            second += 1
        first, second = 0, 1
        sorted_until_index -= 1


import random
from Utils.check_perf import check_performance

# s = [6, 5, 3, 1, 8, 7, 2, 4]
s = [random.randrange(1, 1000000) for _ in range(10000)]
s1 = s[:]
check_performance(bubble_sort, s)
print(s)
check_performance(bubble_sort_while_loop, s1)
print(s1)
# s1.sort()
# print(s1)
