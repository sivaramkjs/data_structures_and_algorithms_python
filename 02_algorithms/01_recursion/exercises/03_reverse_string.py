def reverse(s, index=None):
    # O(n^2) due to the fact that strings are immutable and each recursion creates a new reverse substring
    if index is None:
        index = len(s) - 1

    if index < 1:
        return s[index]

    return s[index] + reverse(s, index - 1)


def reverse_optimized(s, index=None, reversed_str=None):
    # O(n)
    # Interesting fact: Although this is a liner time algorithm, it would be consistently slower than above "reverse" with O(n^2) time.
    #   This is due to under the hood Python string concatenation optimizations compared to list append, resizing operations and the final join "n" chars.
    if index is None:
        index = len(s) - 1

    if reversed_str is None:
        reversed_str = []

    if index < 0:
        return ''

    reversed_str.append(s[index])
    reverse_optimized(s, index - 1, reversed_str)
    return ''.join(reversed_str)


print(reverse("My name is Bob123"))
print(reverse("hello"))

print(reverse_optimized("My name is Bob123"))
print(reverse_optimized("hello"))

# from timeit import Timer
#
# print(
#     f'{Timer(stmt='reverse("My name is Bob123")', globals={'reverse': reverse}).timeit(10000):.4f}')
#
# print(
#     f'{Timer(stmt='reverse_optimized("My name is Bob123")', globals={'reverse_optimized': reverse_optimized}).timeit(10000):.4f}')
