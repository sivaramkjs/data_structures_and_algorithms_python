# In Python, there is no built-in array data structure (like Java, C#).
# We normally use "list" for this purpose. There is also "array" module to create only efficient numeric arrays
# Unlike traditional arrays, list doesn't store items in contiguous memory locations rather store only
# pointers in the contiguous memory locations. These pointers then dereference actual values in the
# scattered memory locations. Due to this reason, lists are not efficient for bulk numeric operations (e.g., sum)
# For simplicity, we will just use list type for array operations in this.

# Type of arrays:
# Static - Fixed size array
# Dynamic - Dynamically growing size array (list, array module, NumPy array)

nums = [1, 2, 3, 6, 4]

print(nums[1])  # access - O(1)

# push/append at the end
# O(1) - Appending an item within the existing list's memory size
# O(n) - When we need to increase list size after the current size is exhausted since we will need to copy all items from old array to new array with bigger size
nums.append(5)

nums.insert(2, 9)  # insert at random index - O(n) due to rearranging the items at all indices

print(nums.pop())  # pop last - O(1)

print(nums.pop(2))  # pop random - O(n) due to rearranging the items at all indices
nums.remove(2)  # remove - O(n) due to searching and then rearranging the items

print(nums)
