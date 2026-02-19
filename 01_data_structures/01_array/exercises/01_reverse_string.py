# Create a function that should reverse a string
# Example:
# s = 'My name is Bob'
# return 'boB si eman yM'
from time import perf_counter


# Presumptions:
# 1. Input is a string
# 2. Output is also a reversed string of the original string

# Clarifications:
# 1. Can input string contain numbers or special characters or spaces? If so then they should also be reversed as is in the output string?
#   1. Only alphanumeric string and should be reversed as is in the output
# 2. Can it be empty? null? single character length? What should be the output in case of empty/null?
#   1. Yes, it can be empty/null/single character. Output should be the same string in case of empty/null
# 3. Would it be in-memory or something else?
#   1. In-memory

# Brute-force approach:
# 1. Loop through all characters from end index, and create a new string by appending each character. However, since strings are immutable in python, this leads to O(n^2) time complexity as each iteration creates a completely new string.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Better than brute-force:
# 1. We can optimize by creating a list object from given string and swapping the characters at the opposite indices from the start to end in the list.
# Time Complexity: O(n + n/2 + n) ≈ O(n)
# Space Complexity: O(n)

# Optimized approach 1:
# 1. We can optimize by creating a new list object and appending characters from end to start index from given string.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimized approach 2:
# 1. Python slice operation is highly optimized in case of CPython which uses a new string buffer to copy all characters in reverse in one operation.
# Time Complexity: O(n)
# Space Complexity: O(1)


def reverse_string_brute_force(s):
    if not s or len(s) == 1:
        return s

    reversed_str = ''  # This is inefficient since strings are immutable as "reversed_str += s[i]" creates a new string everytime
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]

    return reversed_str


def reverse_string(s):
    if not s or len(s) == 1:
        return s

    return s[::-1]

    # reversed_list = []
    # for i in range(len(s) - 1, -1, -1):
    #     reversed_list.append(s[i])
    #
    # return ''.join(reversed_list)

    # str_list = list(s)
    # str_len = len(s)
    # end_index = str_len - 1
    # for i in range(str_len // 2):
    #     str_list[i], str_list[end_index - i] = str_list[end_index - i], str_list[i]
    #
    # return ''.join(str_list)


start = perf_counter()
print(reverse_string_brute_force(''))
print(reverse_string_brute_force('1'))
print(reverse_string_brute_force('hello'))
print(reverse_string_brute_force('My name is Bob123'))
print(reverse_string_brute_force('wall'))
end = perf_counter()
print(f'brute force: {end - start:0.7f}')

start1 = perf_counter()
print(reverse_string_brute_force(''))
print(reverse_string_brute_force('1'))
print(reverse_string('hello'))
print(reverse_string('My name is Bob123'))
print(reverse_string('wall'))
end1 = perf_counter()
print(f'list approach: {end1 - start1:0.7f}')
