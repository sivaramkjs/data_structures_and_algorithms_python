# Given a sorted array of numbers, check if there exists a pair of numbers such that
# when added will be equal to the given sum and return true if such pair exists else false
from time import perf_counter


# Example 1:
# arr = [1, 2, 3, 9], sum = 8
# return false

# Example 2:
# arr = [1, 2, 4, 4], sum = 8
# return true


# Presumptions:
# 1. Input is sorted array of numbers
# 2. Output should be true or false
# 3. We are looking for only one/first pair that adds up to sum but not all pairs?

# Clarifications:
# 1. Would it be only integers? Can there be any float or negative numbers?
# 2. Can "sum" be negative or "0"?
# 3. Is it possible to have repeated numbers in the array?
# 4. Can we add the same number twice?


# Brute-force approach:
# 1. We can use two for loops and try to find a pair adds up to sum and return true if found else false
# Time Complexity: O(n^2)

# Optimized approach 1:
# 1. Since it's sorted, we can iterate through each item and find the required number for the sum using the binary search
# Time Complexity: O(n log n)

# Optimized approach 2:
# 1. Since it's sorted, the smallest number will be the first item and largest number will be the last item.
# 2. We can use a two pointer approach: "low" as smallest number index and "high" as highest number index
# 3. Add the two numbers.
#   1. If the added value is greater than the sum then we need to look for lower number than the current "high" to pair with the current "low" to check if it equals to sum. Hence, decrement the "high" by 1
#   2. If the added value is less than the sum then we need to look for higher number than the current "low" to pair with the current "high" to check if it equals to sum. Hence, increment the "low" by 1
# Time Complexity: O(n)

def find_pair_equal_to_sum_brute_force(sorted_arr, target_sum):
    for i, num1 in enumerate(sorted_arr):
        for num2 in sorted_arr[i + 1:]:
            if num1 + num2 == target_sum:
                return True

    return False


# print(find_pair_equal_to_sum_brute_force([1, 2, 3, 9], 8))
# print(find_pair_equal_to_sum_brute_force([1, 2, 4, 5], 8))


def find_pair_equal_to_sum(sorted_arr, target_sum):
    low, high = 0, len(sorted_arr) - 1

    while low < high:  # We can also use `for _ in range(len(sorted_arr) - 1):`
        current_sum = sorted_arr[low] + sorted_arr[high]
        if current_sum == target_sum:
            return True
        elif current_sum > target_sum:
            high -= 1
        else:
            low += 1

    return False


# print(find_pair_equal_to_sum([1, 2, 3, 9], 8))
# print(find_pair_equal_to_sum([1, 2, 4, 5], 8))


# Extension question 1: What if the array is not sorted?
# 1. We can sort the array and still use the above final solution. Time Complexity: O(n log n)
# 2. Can we do better?
#   1. We can check the difference between the current number and target sum.
#   2. Use an efficient lookup data structure (DS) to find the difference number. If not found then save the current number in the lookup and use it later with the matching pair.
#   3. For this purpose, we will need an efficient DS with faster lookup time. I think we can use hash set which has O(1) lookup speed. In Python, it would be "set".
# 3. We can also use an alternate solution by directly adding the difference value into the lookup. With this, we can directly check the current number exists in the lookup instead of computing the difference and check the difference number every time.
# Time Complexity: O(n)

def find_unsorted_pair_equal_to_sum(arr, target_sum):
    visited_nums = set()

    for num in arr:
        diff = target_sum - num
        if diff in visited_nums:
            return True
        else:
            visited_nums.add(num)

    return False


start = perf_counter()
print(find_unsorted_pair_equal_to_sum([9, 1, 3, 2], 8))
print(find_unsorted_pair_equal_to_sum([5, 1, 4, 4], 8))
end = perf_counter()
print(f'Took {end - start:.7f} secs')


def find_unsorted_pair_equal_to_sum_2(arr, target_sum):
    diff_values = set()

    for num in arr:
        if num in diff_values:
            return True
        else:
            diff_values.add(target_sum - num)

    return False


start1 = perf_counter()
print(find_unsorted_pair_equal_to_sum_2([9, 1, 3, 2], 8))
print(find_unsorted_pair_equal_to_sum_2([5, 1, 4, 4], 8))
end1 = perf_counter()
print(f'Took {end1 - start1:.7f} secs')

# import statistics
#
#
# def benchmark_properly(func, arr, target, iterations=10000):
#     times = []
#     for _ in range(iterations):
#         start2 = perf_counter()
#         func(arr, target)
#         end2 = perf_counter()
#         times.append(end2 - start2)
#
#     return f'{statistics.mean(times):0.7f}, {statistics.stdev(times):.7f}'
#
#
# print(benchmark_properly(find_unsorted_pair_equal_to_sum_2, [9, 1, 3, 2], 8))
# print(benchmark_properly(find_unsorted_pair_equal_to_sum, [9, 1, 3, 2], 8))
