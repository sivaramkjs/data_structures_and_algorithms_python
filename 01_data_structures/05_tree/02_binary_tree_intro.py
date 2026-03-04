# A tree with:
#   1. Each node containing 0 to 2 (or at most 2) child nodes.
#   2. Each child node can have only one parent node.

# Full binary tree:
#    A binary tree with each node having either 0 or 2 child nodes (no node with exactly 1 child).
#
# Complete binary tree:
#   A binary tree where all level are completely filled except the last level, which are filled from as left as possible.
#
# Perfect binary tree:
#   1. A full binary tree with all leaf nodes are at same depth (level), so completely filled at every level.
#   2. It has two properties:
#       1. Number of total nodes at each level = 2 * (total nodes at its previous level)
#       2. Number of total nodes at each level = (number of total nodes at all previous levels) + 1, i.e., almost half of all nodes are at leaf level

#   O(log n) Time Complexity:
#       Number of nodes at each level = 2^h (h - max depth/number of levels of the tree)
#       E.g., Level 0: 2^0 = 1
#             Level 1: 2^1 = 2
#             Level 2: 2^2 = 4
#             Level 3: 2^3 = 8
#
#       Total number of nodes in a perfect binary tree = 2^h - 1 (h - max depth/number of levels of the tree). This is due to the fact that the number of nodes at each level is a multiple of 2 except the root.
#       E.g., For a tree with 3 levels (0-2): 2^3 - 1 = 7

#       Total nodes (n) = 2^h - 1 ≈ 2^h (h - max depth. In the context of DSA, it can also be interpreted as "max number of steps" from root to reach a desired node)
#       n = 2^h
#       log n = h
#   This will lead us to "Binary search tree (BST)"

# Binary Search Tree (BST):
#   1. All values "greater than" the root will be on the "right side" of the tree.
#   2. All values "less than" the root will be on the "left side" of the tree.
#   3. Each subtree will also follow the same structure.
#   4. While full/perfect binary trees describe shape, BST describes value ordering. Hence, BST can be any binary tree.

# Unbalanced BST:
#               10
#             /   \
#           9     11
#         /
#       7
#      /
#     6
#   /
#  5
#   Long linked list like structure
#   lookup - O(n)
#   insert/remove - O(n)

# Balanced BST:
#               10
#             /   \
#           9     11
#         /
#       7
#   Mostly balanced structure on both sides
#   lookup - O(log n)
#   insert/remove - O(log n)


# BST Pros:
# Better than O(n)
# Ordered
# Flexible size

# BST Cons:
# No O(1) operations

# BST vs Arrays:
# lookup: O(log n) vs O(n)
# insert/remove: O(log n) vs O(n)

# BST vs Hash Map:
# lookup: O(log n) vs O(1)
# insert/remove: O(log n) vs O(1)
# Hash map doesn't have hierarchical structure. E.g., parent/child, file system


# Self-balancing BST types:
# 1. AVL tree
# 2. RED-BLACK tree
