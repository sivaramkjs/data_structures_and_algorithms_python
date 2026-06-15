# Counting sort (also spelled count sort) is a non-comparison-based sorting algorithm that sorts elements by counting the frequency of each distinct value and using those counts to place elements in their correct sorted positions.

# How It Works
# 1. Find the maximum element in the input array
# 2. Create a count array of size max + 1, initialized to 0
# 3. Count frequencies: For each element, increment the count array at that index
# 4. Compute prefix sums (cumulative counts) to determine final positions
# 5. Build output array by traversing the input from end-to-start (for stability), placing each element at its calculated position
# 6. Decrement counts after placing each element

# | ---------------- | ------------------------------------------------------------------------------------------------ |
# | Time complexity  | O(n+k) where n = number of elements, k = range of input values                                   |
# | Space complexity | O(n+k) auxiliary space                                                                           |
# | Stable           | Yes — preserves relative order of equal elements                                                 |
# | Works on         | Non-negative integers including 0 (or values mapable to integers)                                            |
# | Best when        | Range k is small compared to n                                                                   |


def counting_sort(nums):
    print(nums)
    max_val = max(nums)
    count = [0] * (max_val + 1)
    # print(count)

    # Increase the count at each number's index in the count array.
    # The count array uses 1-based counts i.e., "the number of elements ≤ x", starting from "1". The total count for
    # each number indicates the end position of the number in the array. However, since we counted starting from "1",
    # this value will be identical to 1-based index instead of 0-based index.
    #   E.g., Input array: [4, 1, 2, 1]
    #           count[1] = 2
    #               Ending position is "2", however the base start value is "1" instead of "0" as in indexing
    #               Hence, in order to convert this for 0-based indexing, we will need to subtract "1" from this value.
    #               So, the 0-based position will be "1", and the index range will be [0, 1] instead of [1, 2]
    for num in nums:
        count[num] += 1
    # print(count)

    # prefix sums
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print(count)

    sorted_nums = [-1] * len(nums)
    # sort from end to start to retain the order in case of equal numbers
    # This is because the prefix sum value will indicate the end index (last occurrence) of the duplicate numbers. So,
    # processing from end will place the duplicates in the original order from end to start of the input array.
    for i in range(len(nums) - 1, -1, -1):
        # since values in count array are using 1-based index, convert it to 0-based index in the sorted array.
        sorted_index = count[nums[i]] - 1
        sorted_nums[sorted_index] = nums[i]
        count[nums[i]] -= 1

    return sorted_nums


print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
print(counting_sort([4, 2, 2, 0, 0, 8, 3, 3, 1]))
