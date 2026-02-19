# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return -1

# Bonus... What if we had this:
#  [2,5,5,2,3,5,1,2,4]
#  return 5 because the pairs are before 2,2

# Presumptions:
# 1. Input is an array
# 2. Output is a number

# Clarifications:
# 1. Can the input array be empty? If so, what should be the output? - yes, -1
# 2. What data types are possible in the input? Only positive integers or negatives also or floats or strings/characters? - only positive integers
# 3. If array doesn't contain duplicates then what should be the output? -1

# Brute-force approach:
# 1. Set current_recurring_index = len(array) to find the first recurring element in case of nested pairs of recurring elements. E.g., '5' in [2, 5, 5, 2]
# 2. Use nested loops.
# 3. Outer loop through each element in the array.
# 4. Inner loop through subsequent elements after the outer loop element.
# 5. Compare outer loop element to all the inner loop elements.
# 6. If we find an inner element equal to outer element,
#   1. Check if the inner element index is less than the current_recurring_index.
#   2. If so then set current_recurring_index = inner element index.
#   3. This will ensure finding the first recurring element by using the lowest index among all recurring elements in case of nested pairs of recurring elements.
#       1. E.g., '5' in [2, 5, 5, 2]
# 7. Continue with the next outer loop element.
# 8. Repeat steps 2-7.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_first_recurring_element_brute_force(array):
    if not array:
        return -1

    current_recurring_index = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                if j < current_recurring_index:
                    current_recurring_index = j
    return array[current_recurring_index] if current_recurring_index < len(array) else -1


print(find_first_recurring_element_brute_force([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(find_first_recurring_element_brute_force([]))
print(find_first_recurring_element_brute_force([2]))
print(find_first_recurring_element_brute_force([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(find_first_recurring_element_brute_force([2, 3, 4, 5]))

# This will incorrectly return '2' using the above brute-force approach without "max_recurring_index" logic
print(find_first_recurring_element_brute_force([2, 5, 5, 2, 3, 5, 1, 2, 4]))


# Optimized approach:
# 1. Create an empty hash set.
# 2. Loop through each element.
# 3. Check if the current element already present in hash set.
# 4. If present then we found the first recurrence, return the current element else add the element into set.
# 5. Repeat steps 2-5
# Time Complexity: O(n)
# Space Complexity: O(n)

def find_first_recurring_element(array):
    visited_elements = set()

    for element in array:
        if element in visited_elements:
            return element
        else:
            visited_elements.add(element)

    return -1

# print(find_first_recurring_element([2, 5, 1, 2, 3, 5, 1, 2, 4]))
# print(find_first_recurring_element([]))
# print(find_first_recurring_element([2]))
# print(find_first_recurring_element([2, 1, 1, 2, 3, 5, 1, 2, 4]))
# print(find_first_recurring_element([2, 3, 4, 5]))
# print(find_first_recurring_element([2, 5, 5, 2, 3, 5, 1, 2, 4]))
