# Given 2 arrays, write a function to check if two arrays contain any common items and return true or false
# Example 1:
#
# `arr1 = ['a', 'b', 'c', 'x']`
#
# `arr2 = ['y', 'z', 'i']`
#
# `return false`
#
# Example 2:
#
# `arr1 = ['a', 'b', 'c', 'x']`
#
# `arr2 = ['y', 'z', 'x']`
#
# `return true`

from time import perf_counter


def contain_common_items_brute_force(arr1, arr2):
    for item1 in arr1:
        for item2 in arr2:
            if item1 == item2:
                return True

    return False


def contain_common_items(arr1, arr2):
    arr1_to_hash_set = set(arr1)

    for item in arr2:
        if item in arr1_to_hash_set:
            return True

    return False


start = perf_counter()
print(contain_common_items_brute_force(['a', 'b', 'c', 'x'], ['y', 'z', 'i']))
end = perf_counter()
print(f'Took {end - start:.7f} secs')

start1 = perf_counter()
print(contain_common_items(['a', 'b', 'c', 'x'], ['y', 'z', 'x']))
end1 = perf_counter()
print(f'Took {end1 - start1:.7f} secs')

# print(contain_common_items([1, 2, 3], ['y', 'z', 'i']))
