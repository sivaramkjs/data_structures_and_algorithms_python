##### Problem Statement:

Given 2 arrays, write a function to check if two arrays contain any common items and return true or false
**Example 1:**

`arr1 = ['a', 'b', 'c', 'x']`

`arr2 = ['y', 'z', 'i']`

`return false`

**Example 2:**

`arr1 = ['a', 'b', 'c', 'x']`

`arr2 = ['y', 'z', 'x']`

`return true`

## Problem-Solving Approach:

### Step 1: Write down all the key points/presumptions (e.g., input, output) which are already clear from the problem statement

1. We should expect 2 array params as input.
2. Function output should be either true or false.

### Step 2: Ask Clarifying Questions and get all the details to determine possible solutions

1. Can arrays be of different length? Can arrays be empty?
2. Would both arrays contain same data type items? and only characters or any other data type items like numbers,
   floats, etc.?
3. If only characters then should we do a case-sensitive/insensitive comparison?
4. Are we looking for only the first match?
5. Are the inputs always be arrays? or any other types?

###### [Optional]

6. In case of numbers, are they sorted? can there be floats/negative numbers?
7. How large can the input be? Whether it is in-memory or from file?
8. What is more important? Time complexity or Space complexity?

### Step 3: Talk about all possible approaches, each approach pros and cons, and write down solution steps (Don't start writing code)

#### Step 3.1: Brute Force Approach:

1. Easiest solution would be to use two for loops to check if an item from array1 exists in the entire array2.
    1. (Write pseudocode/code if needed for better understanding)

```python
def contain_common_items_brute_force(arr1, arr2):
    for item1 in arr1:
        for item2 in arr2:
            if item1 == item2:
                return True

    return False
```

2. However, the **Time Complexity (Time): O(len(array1) * len(array2)) ≈ O(n^2)**
3. It's not the most efficient approach.

#### Step 3.2: Optimized Approach:

1. We can use a hash set to store the first array items (**Time:** O(len(array1)))
2. Loop through the second array (**Time:** O(len(array2))) and check if any item exists in the hash set (**Time:** O(
   1))
3. **Time Complexity: O(len(array1) + len(array2)) ≈ O(n)**
4. It's a more efficient approach.

#### [Optional] Step 3.3: Think about any edge cases and check if the decided approach works without any issues

### Step 4: Start writing the code after deciding the approach

```python
def contain_common_items(arr1, arr2):
    arr1_to_hash_set = set(arr1)

    for item in arr2:
        if item in arr1_to_hash_set:
            return True

    return False
```

### Step 5: Test code and think about error checks, edge cases, invalid/large inputs (empty arrays, no arguments, undefined/null, large arrays)

1. Walk through the final code with the small sample inputs and check if the code works
2. Check for edge cases. Try to think what can break the code

```python
contain_common_items(['a', 'b', 'c', 'x'], ['y', 'z', 'i'])

contain_common_items([], ['y', 'z', 'i'])

contain_common_items([], [])

contain_common_items([1, 2, 3], ['y', 'z', 'i'])

contain_common_items(None, ['y', 'z', 'i'])
```

#### Step 5.1: Discuss assumptions and safeguards

1. Ask the interviewer if we can make assumptions about the correct input i.e., always arrays, same data type arrays,
   etc.
2. Tell the interviewer about any safeguards that may be needed in case of invalid inputs

### Step 6: Look for any different approaches, performance improvements, readability improvements

1. Check if we can improve the code further. E.g., Space Complexity optimization
    1. In case of our example problem, below is **Space Complexity** for both approaches
        1. Brute force: **O(1)** -- since we are not creating any extra variables or data structures
        2. Optimized solution: **O(len(array1))** -- since we are creating a hash set of array1's length
2. Highlight any readability improvements. E.g., Organizing code into small modular functions, better names, etc.

### Step 7: Expect additional requirements or constraints to revise the final solution

1. Interviewer may ask any extension questions to test our thought process to handle the solution differently. E.g.,
    1. What if the input arrays are very large to fit into memory?
        1. We can use a divide-and-conquer approach to divide the input into fittable chunks and process chunk by chunk
    2. What if the input arrive as stream?
        1. We could possibly read the stream or convert the stream into concrete data structure and process the data
2. Handling async or parallel processing scenarios.
