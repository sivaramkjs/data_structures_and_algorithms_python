# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Presumptions:
# 1. Input is array of numbers.
# 2. Output is a number equal to the sum of all elements in the largest subarray.
# 3. Subarray can be either less length or same length of the input array

# Clarifications:
# 1. Can input array be empty? If so then what should be output in this case? - yes and "0"
# 2. Does it contain only integers (positive/negative) or floats as well? - only integers (positive/negative)
#   1. In case of all negative integers, can output be negative? - yes
# 3. Only sequential subarrays in the original index order? or random subarrays? - sequential subarrays
# 4. Is the input array sorted? - Maybe not relevant

# Brute-force approach:
# 1. Use two nested loops through the input array; Set max_sum = nums[0]
# 2. Loop through all elements in the outer loop one by one; Compare the outer element and max_sum and set max_sum to the largest value; Set current_sum = outer element
# 3. Loop through the remaining elements except outer element in the inner loop.
# 4. Add current_sum and inner element, compare max_sum and current_sum and set max_sum to the largest value.
# 5. Advance the inner loop to the next element and repeat steps 3-5
# 6. Advance the outer loop to the next element.
# 7. Repeat steps 2-6 until the outer loop is exhausted.
# 8. Return the final max sum.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# def max_sub_array_brute_force(nums):
#     max_sum = nums[0]
#     for i in range(len(nums)):
#         max_sum = max(max_sum, nums[i])
#         current_sum = nums[i]
#         for j in range(i + 1, len(nums)):
#             current_sum += nums[j]
#             max_sum = max(current_sum, max_sum)
#
#     return max_sum

# print(max_sub_array_brute_force([1]))
# print(max_sub_array_brute_force([1, 2]))
# print(max_sub_array_brute_force([-1, 0, -2]))
# print(max_sub_array_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_sub_array_brute_force([5, 4, -1, 7, 8]))

# Two pointers approach:
# def find_largest_sub_array_sum_1(nums):
#     if not nums:
#         return 0
#     if len(nums) == 1:
#         return nums[0]
#
#     i, j = 0, 1
#     largest_subarray_sum = nums[i]
#     current_sum = nums[i]
#
#     while i < len(nums):
#         largest_subarray_sum = max(largest_subarray_sum, current_sum)
#
#         if j < len(nums):
#             current_sum += nums[j]
#             largest_subarray_sum = max(largest_subarray_sum, current_sum)
#
#         if j < len(nums) - 1:
#             j += 1
#         else:
#             i += 1
#             if i < len(nums):
#                 current_sum = nums[i]
#                 j = i + 1
#
#     return largest_subarray_sum

# Optimized approach:
# 1. Create a new array to store largest sub array sums until an index i, largest_sub_array_sum_until_index = []
# 2. Initialize max_sum = nums[0] and largest_sub_array_sum_until_index[0] = nums[0]
# 3. Loop through all remaining elements except first element.
# 4. Add previous largest sub array sum until current index (largest_sub_array_sum_until_index[i-1]) and current element.
# 5. Get the largest value between result from step 4 and current element.
#   1. Basically, this step will either continue the previous sub array (largest_sub_array_sum_until_index[i-1] > current element) or reset the sub array to the current element index (largest_sub_array_sum_until_index[i-1] < current element)
# 6. Set the current index's largest subarray sum (largest_sub_array_sum_until_index[i]) to the result from step 5.
# 7. Set max_sum to the largest of max_sum and current index's largest subarray sum from step 6.
# 8. Repeat 3-4 until the loop finishes.
# 9. Return the max_sum.
# Time Complexity: O(n)
# Space Complexity: O(n)


# def find_largest_sub_array_sum_2(nums):
#     largest_sub_array_sum_until_index = [nums[0]]
#     max_sum = nums[0]
#
#     for i in range(1, len(nums)):
#         largest_sub_array_sum_until_index.append(max(largest_sub_array_sum_until_index[i - 1] + nums[i], nums[i]))
#
#         max_sum = max(max_sum, largest_sub_array_sum_until_index[i])
#
#     return max_sum


def find_largest_sub_array_sum(nums):
    largest_sub_array_sum_until_current_index = max_sum = nums[0]

    for i in range(1, len(nums)):
        largest_sub_array_sum_until_current_index = max(largest_sub_array_sum_until_current_index + nums[i], nums[i])

        max_sum = max(max_sum, largest_sub_array_sum_until_current_index)

    return max_sum


# [3, -1, 2, 4]

print(find_largest_sub_array_sum([1]))
print(find_largest_sub_array_sum([1, 2]))
print(find_largest_sub_array_sum([-1, 0, -2]))
print(find_largest_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(find_largest_sub_array_sum([5, 4, -1, 7, 8]))
