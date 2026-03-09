# Recursion is a concept in which a function will call itself within its own function body.
#   E.g., def hello():
#           hello()
#   1. It's useful when a task involves subtasks with same task processing steps.
#       E.g., Listing all files within a file system folder having sub-folders.
#   2. However, there are some downsides of using recursion naively.
#       1. It can cause call stack overflow if not handled properly.
#       2. Each recursive call instance needs to be held in memory until recursion ends. This could result in high memory usage.
#
#   3. There are standard steps to handle the downsides of recursion.
#
#   4. Every recursive function should have a "base case" and a "recursive case".
#       1. Base case - The case that stops further recursion.
#       2. Recursive case - The case that continue the recursion.
#   5. Ideally, a recursive function should follow the below steps:
#       1. Identify a base case.
#       2. Identify a recursive case.
#       3. Return from base case to end the recursion.
#       4. Return from the recursive case to exit the function.

# Recursion Pros:
#   1. DRY principle by not repeating logic in a loop
#   2. Readability
# Cons:
#   1. Large memory stack (although it can be optimized with Tail-recursive Call Optimization (TCO) in some languages such as JavaScript)


# Recursion vs Iterative:
#   1. Anything that can be solved using recursion can also be solved using iterative approach.
#   2. Recursion is particularly useful when we don't know the number of iterations or depth/breadth of a data structure. E.g., Tree/Graph traversal.

# When should we use recursion:
#   1. When a problem can be divided into subproblems, and each subproblem is identical in nature.
#   2. Divide and Conquer using recursion.
#   E.g., Tree/Graph traversal, some sorting algorithms.
