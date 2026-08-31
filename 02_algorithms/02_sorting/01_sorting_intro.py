# Sorting doesn't matter much in case of small data inputs as a language builtin sort function can sort without any issues.
# However, when the input data gets larger and larger, the sorting algorithm selection becomes more important to save operation time and costs since a builtin sort function may not be efficient for all types of input data.
# Additionally, when we are using a builtin sort function, it is important to know how it sorts data as sometimes it may result in unexpected behaviour.
#   E.g., sort() function in JavaScript - converts each input element into a string and compare them using character Unicode values. As a result, numbers are sorted as per their string equivalents. Hence, it requires to provide a comparison function to compare different types of data.

# Most commonly used sorting algorithms:
#   1. Bubble sort
#   2. Insertion sort
#   3. Selection sort
#   4. Merge sort
#   5. Quick sort
#   6. Heap sort

# Stable vs Unstable sorting algorithms:
#   1. A sorting algorithm is called "stable" if it preserves the input order of equal keys in the sorted output, otherwise called "unstable".
#       E.g., input: [apple, stop, ball, steel]
#             If we sort this list by first letter of each element then,
#
#             Stable sorting algorithm output: [apple, ball, stop, steel]
#             Unstable sorting algorithm output: [apple, ball, steel, stop] or [apple, ball, stop, steel]
#
#             Notice the elements starting with the same letter in both outputs.
#   2. Basically, an unstable sorting algorithm doesn't guarantee the same input order of equal keys in the output.
#   3. Stable sorting algorithms: IBM [Insertion, Bubble, Merge], etc.
#   4. Unstable sorting algorithms: Heap, Selection, Quick, etc.

# Which sorting algorithm is best?
#   Bubble/Selection sort - We almost never use these except for academic purposes due to their high time complexity.
#   Insertion sort - Small input and mostly sorted data.
#   Merge sort - One of the most used due to its consistent time complexity in all cases.
#   Quick sort - Fastest and preferred except in its worst case scenario. Used over merge sort when there are space
#                constraints. However, if the pivot is not properly selected then it would result in poor performance.
#   Heap sort - Used over merge/quick sort when there is a strict memory constraint. Generally slower than merge/quick sort.

# Can we beat O(n log n) time complexity with any sorting algorithms?
#   While mathematically it would be impossible, we can optimize by skipping comparisons. This is called "Non-comparison based sort".
#
# Non-comparison based sort algorithms:
#       1. Counting sort
#       2. Radix sort
#       3. Bucket sort
#   - These actually use either binary or other structural representation (digits, ranges, buckets) of the element to sort them.
#     However, due to the nature of such sorting mechanisms, these work only with a fixed-length range of integers data.
#   - In those limited data cases, they could outperform comparison sort algorithms like merge/quick sort.
