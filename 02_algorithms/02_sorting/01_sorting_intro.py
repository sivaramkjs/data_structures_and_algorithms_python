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
