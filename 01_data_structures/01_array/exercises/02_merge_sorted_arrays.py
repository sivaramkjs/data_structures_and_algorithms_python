# Given two sorted arrays, merge the two arrays into one sorted array
# Example:
# sorted_array1 = [0, 3, 4, 31]
# sorted_array2 = [4, 6, 30]

# output = [0, 3, 4, 4, 6, 30, 31]

# Presumptions:
# 1. Input is two separate sorted arrays
# 2. Output is one sorted array

# Clarifications:
# 1. Can either array be empty? Can they be of different lengths? - yes
#   1. If both are empty then what should be the output? - empty array
# 2. Are they always numeric arrays? If so, can there be floats? only integers? negative integers? - only integers with negatives
#   1. Can there be repeated numbers? - yes

# Brute-force approach:
# 1. Loop through array2, and find each array2 element's insertion position in array1 by finding same or greater element in the array1 using linear search.
# 2. Insert array2 element in the array1 at position before same or greater element.
# Time Complexity: O(n * (m + m)) ≈ O(n^2)
# Space Complexity: O(1) (since reusing the input array)

# Optimized approach 1:
# 1. Since arrays are sorted, we can use binary search instead of linear search.
# 2. Insert array2 element in the array1 at position before same or greater element.
# Time Complexity: O(n * (log m + m)) ≈ O(n^2)
# Space Complexity: O(1) (since reusing the input array)

# Optimized approach 2:
# 1. Create a new result array.
# 2. Take two pointers i and j pointing to starting indices of each array.
# 3. Iterate until either array has elements left.
# 4. Compare elements at both indices and append the smallest pointer element to the result array.
# 5. Move the smallest element pointer to next index and compare it with the current large pointer element.
# 6. Repeat the process until finding an equal or larger element than the current large pointer element.
# 7. Once we find an equal or larger element than the current large pointer element,
#   1. In case of equal,
#       1. Append both current smallest and largest pointer elements to the result array.
#       2. Move both current smallest and largest element pointers to next indices and repeat steps 4 - 7
# 8. Once either of arrays was exhausted, copy the remaining elements from the non-exhausted array into the result array.
# Time Complexity: O(n | m) ≈ O(n)
# Space Complexity: O(n + m)

def merge_sorted_arrays(array1, array2):
    if not array1 and not array2:
        return []
    elif not array1:
        return array2
    elif not array2:
        return array1

    i, j = 0, 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            result.append(array2[j])
            j += 1
        else:
            result.extend([array1[i], array2[j]])
            i, j = i + 1, j + 1

    if i < len(array1):
        result.extend(array1[i:])
    elif j < len(array2):
        result.extend(array2[i:])

    return result


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
print(merge_sorted_arrays([1, 3, 5, 7], [0, 2, 4, 6, 8, 10]))
print(merge_sorted_arrays([1, 3, 5, 7], [1, 3, 5, 7]))
print(merge_sorted_arrays([1, 3, 5, 7], []))
print(merge_sorted_arrays([], [4, 6, 30]))
print(merge_sorted_arrays([], []))
# print(merge_sorted_arrays(['a'], ['A', 'b']))
