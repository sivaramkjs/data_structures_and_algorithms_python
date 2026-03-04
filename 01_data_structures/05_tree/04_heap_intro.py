# Heap is a tree data structure mostly used for comparison operations.
# Binary Heap:
#   1. Most commonly used heap data structure and based on a complete binary tree.
#   2. Less ordered than a BST
#   3. There are two types.
#       1. Max Heap - Nodes in descending order from root
#       2. Min Heap - Nodes in ascending order from root
#   4. There is no specific left and right subtree ordering similar to BST.
#   5. Time Complexity:
#       1. Lookup - O(n) since we will need to traverse to the desired node in a random order.
#       2. Insert - O(log n)
#       3. Delete - O(log n)
#   E.g.,
#       Max Heap:
#               101
#             /   \
#           77    33
#         /  \
#       2     5
#     Get all nodes greater than 33 will just need traversing until 33 node. Imagine the same operation using a BST, where we need to traverse entire right subtree of 33 node.
#   6. Memory heap and heap data structure are not same.
#   7. Since it is left to right node insertion, heap doesn't need rebalancing like in BST.

# Pros:
#   1. Better than O(n) operations
#   2. Priority based processing/Comparison
#   3. Fast insert (despite some bubble up insertion to swap nodes as per priority)

# Cons:
#   1. Slower lookup

# Priority Queue:
#   1. A binary heap data structure that stores data in a priority order and process it based on priority.
#   2. Not same as normal Queue data structure.
#   E.g., Prioritizing patients at emergency, Boarding business class and economy passengers.
