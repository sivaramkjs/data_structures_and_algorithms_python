# Quick sort also uses divide and conquer approach similar to merge sort.
# Pivot:
#   1. It divides the input using a randomly selected element called "pivot" from the input list.
#       1. Generally, first or last element is selected as pivot in order to maintain balanced partitions.
#   2. Once we select the pivot element, we will compare remaining elements with the pivot element and keep/move smaller
#      elements to its left and larger elements to its right until the pivot is moved to the middle index or appropriate
#      sorted position index in some cases (e.g., reverse sorted input list).

# Divide (Partition) and Sort:
#   1. Once the pivot is moved the appropriate mid-position, we will divide the list into two partitions excluding the
#      pivot element.
#   2. Repeat the pivot selection and sorting process for each partition recursively until all partitions are sorted
#      in-place.

# Generally, quick sort implementations use "Lomuto" or "Hoare" partition schemes for optimal performance.

# Time Complexity: O(n log n)
#   1. Balanced partitioning will result in a binary tree like structure with depth O(log n).
#       1. We can view it as "how many splits (levels) are required to complete the sorting" irrespective of the work
#          per level. Basically, any fixed splitting/partitioning will always result in a binary tree like structure.
#          E.g., Both good(1/2) split and bad(9/10) split will result in a binary tree like structure since they are fixed ratios
#                although with different logarithmic depths and different bases (base 2 and base 10).
#   2. Since each level compares at most "n" elements with the pivot, the work per level will be <= O(n).
#   3. Hence, the total work = O(n) [work per level] * O(log n) [total levels] = O(n log n).
#   4. In worst case scenario, this can be O(n^2) since the pivot may not divide input into balanced partitions. E.g., reverse sorted input list
#       1. As a result, pivot selection is a critical factor for the quick sort performance.

# Space Complexity: O(log n)
#   As we are doing an in-place sorting, there will be no additional space created. However, the recursion tree
#   will take up O(log n) stack space.

# Algorithm 1:
#   1. Let the given input list "a", left = 0, right = last index.
#   2. Select pivot and divide the list into smaller partitions recursively.
#       1. Select the last (right) index element in the list as the pivot.
#       2. Compare all remaining elements with the pivot starting from left and sort them.
#           1. Loop (i) through all remaining elements.
#               1. Compare a[i] with a[pivot].
#               2. If a[i] < a[pivot] then keep it as is and move to the next element.
#                   1. i = i+1
#               3. If a[i] > a[pivot] then move a[i] to the right side of the pivot in the list.
#                   1. temp = a[i]
#                   2. a[i] = a[pivot-1]
#                   3. a[pivot-1] = a[pivot]
#                   4. a[pivot] = temp
#                   5. pivot = pivot-1
#                   6. We will also not increment "i" in this case to compare the "pivot-1" element that we moved to the "i" index
#                      with the pivot as it could be smaller or larger than pivot and needs to be sorted.
#                      This will lead to proper left and right sorted partitions around the pivot properly.
#               4. Repeat steps 3.1.1-3.1.3 until i < pivot to stop when all elements are properly sorted around pivot.
#           2. When the loop ends, the pivot reaches the appropriate mid-index.
#           3. Divide the list into two smaller partitions, left and right, excluding the pivot element.
#               1. left partition = left, pivot-1
#               2. right partition = pivot+1, right
#   3. Repeat step 2 recursively for each smaller partition until left < right i.e., when pivot reaches the left-most position,
#      which means the entire partition has been sorted.


def quick_sort(a, left, right):
    if not left < right:  # stop when pivot reaches the left-most position, which means the entire partition has been sorted.
        return

    pivot = right
    i = left

    while i < pivot:
        if a[i] > a[pivot]:
            a[i], a[pivot - 1], a[pivot] = a[pivot - 1], a[pivot], a[i]
            pivot = pivot - 1
            # Notice that we are not incrementing the "i" in this case. This is because we will need to compare the "pivot-1" element
            # that we now moved to the "i" index with the pivot as it could be smaller or larger than pivot and needs to be sorted again.
            # This will lead to proper left and right sorted partitions around the pivot.
        else:
            # If a[i] is already smaller than the pivot then it's already positioned to left of pivot. Hence, we can move
            # to the next element.
            i += 1

    quick_sort(a, left, pivot - 1)
    quick_sort(a, pivot + 1, right)


def quick_sort_from_left(a, left, right):
    if not left < right:
        return

    pivot = left
    i = right

    while i > pivot:
        if a[i] < a[pivot]:
            a[i], a[pivot + 1], a[pivot] = a[pivot + 1], a[pivot], a[i]
            pivot = pivot + 1
        else:
            i -= 1

    quick_sort(a, left, pivot - 1)
    quick_sort(a, pivot + 1, right)


# Algorithm 2 (Hoare partition scheme using two pointers):
#   1. Let the given input list "a", left = 0, right = last index.
#   2. Select pivot as the last (can also be first) element of "a", pivot = right
#   3. Loop through elements using left and right pointers to sort elements from left to right and from right to left respectively
#      by moving both pointers inward towards each other.
#       1. Compare a[left] with pivot.
#           1. If a[left] < a[pivot] then a[left] is properly positioned left to pivot. So, increment left and move to the next element.
#           2. If a[left] >= a[pivot] then a[left] is not properly positioned right to pivot. So, stop here and
#              check if there is a corresponding a[right] waiting to be sorted.
#       2. Compare a[right] with pivot.
#           1. If a[right] > a[pivot] then a[right] is properly positioned right to pivot. So, decrement right and move to the previous element.
#           2. If a[right] <= a[pivot] then a[right] is not properly positioned left to pivot. So, stop here and
#              check if there is a corresponding a[left] waiting to be sorted.
#       3. When we have both left and right elements waiting to be sorted then swap them. This will properly position
#          them around the pivot in sorted order.
#           1. Increment left and right by 1 to move to the next and previous elements respectively.
#   4. Repeat step 3 until both left and right meet or cross each other.
#       1. If left >= right then stop the loop.
#   5. Partition around the right and repeat steps 2-4 recursively until left < right i.e., when pivot reaches the left-most position,
#      which means the entire partition has been sorted.
# Notes:
#   1. Hoare scheme includes pivot also into the comparison and thereby sorting it in the process unlike Lomuto's scheme,
#      which moves the pivot element to the boundary index after every pass.
#   2. While using this scheme, we will need to select the pivot properly i.e., left or right in order to avoid infinite recursion
#      error during partitions.
#       1. This is to satisfy the Hoare's invariants rule where left <= pivot and right >= pivot and each partition should
#          continuously shrink further.


def quick_sort_hoare_partition(a, left, right):
    if left >= right:
        return

    partition_index = hoare_partition_1(a, left, right)

    quick_sort_hoare_partition(a, left, partition_index)
    quick_sort_hoare_partition(a, partition_index + 1, right)


def hoare_partition(a, left, right):
    pivot = a[right]
    i = left
    j = right
    left_swap = False
    right_swap = False

    while i <= j:  # terminate when both pointers meet each other
        if not left_swap and a[i] < pivot:
            i += 1
        else:
            left_swap = True

        if not right_swap and a[j] > pivot:
            j -= 1
        else:
            right_swap = True

        if left_swap and right_swap:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
            left_swap = right_swap = False

    return j


def hoare_partition_1(a, left, right):
    pivot = a[right]
    i = left
    j = right

    while True:
        while i < right and a[i] < pivot:  # iterate until we found a left element > pivot to swap
            print(f'i: {i}, a[i]: {a[i]}')
            i += 1

        while j > left and a[j] > pivot:  # iterate until we found a right element < pivot to swap
            print(f'j: {j}, a[j]: {a[j]}')
            j -= 1

        # return when both pointers cross each other.
        # This is slightly different from "hoare_partition" function in which we are terminating the loop when the
        # pointers "meet" instead of crossing. This subtle difference is crucial especially when using Hoare's classic
        # nested while loops based implementation in order to shrink down the partitions properly and avoid infinite
        # recursion error. This is due to the fact that the pointers will naturally cross each other because of
        # continuous increment in a while loop.
        # E.g., [99, 44, 6, 0]
        #       pass 1: left=0, right=3, pivot=0, i=1, j=0  [0, 44, 6, 99]
        #           right recursion 1: left=1, right=3, pivot=99, i=4, j=2  [0, 44, 6, 99]
        #               left recursion 2: left=1, right=2, pivot=6, i=2, j=1  [0, 6, 44, 99]
        if j < i:
            return j

        # swap when both left and right needs to be sorted
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


import random
from Utils.check_perf import check_performance

# s = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
s = [random.randrange(0, 100000) for _ in range(10000)]
# s = sorted(s)
s1 = s.copy()
check_performance(quick_sort, s, 0, len(s) - 1)
check_performance(quick_sort_hoare_partition, s1, 0, len(s1) - 1)
print(s)
print(sorted(s1) == s)
