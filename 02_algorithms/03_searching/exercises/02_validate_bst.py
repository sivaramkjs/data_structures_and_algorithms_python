from collections import deque


# Given the root of a binary tree, determine if it is a valid binary search tree (BST).


# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# def validate_bst(root):
#     parent_index = 0
#     left_index = 1
#     right_index = 2
#
#     while right_index < len(root):
#         current_node = root[parent_index]
#         left_child = root[left_index]
#         right_child = root[right_index]
#
#         if left_child and left_child > current_node:
#             return False
#
#         if right_child and right_child < current_node:
#             return False
#
#         parent_index = parent_index + 1
#         left_index = left_index + 2
#         right_index = right_index + 2
#
#     return True


# print(validate_bst([2, 1, 3]))
# print(validate_bst([5, 1, 8, None, None, 6, 9]))


def validate_bst_bfs(root):  # This validates only local immediate parent ordering
    previous_level_nodes = deque([root])

    while len(previous_level_nodes) > 0:
        node = previous_level_nodes.popleft()
        if node.left:
            if node.left.val < node.val:
                previous_level_nodes.append(node.left)
            else:
                return False

        if node.right:
            if node.right.val > node.val:
                previous_level_nodes.append(node.right)
            else:
                return False

    return True


# Min/Max Algorithm:
#   1. Start with the root node.
#   2. Use DFS preorder traversal to traverse the nodes by using min and max values as a range to check a
#      specific node validity within the BST.
#   3. Initialize node = root, current_min = -inf, current_max = +inf.
#   4. If it's not a valid node then return True since it doesn't violate/affect BST ordering.
#   5. If it's a valid node then,
#       1. If the node's value is not within the current_min and current_max range then return False as it's violating the BST
#          ordering.
#       2. This works as below.
#           1. At every node, for the left subtree, we will set the current_max to the current node i.e., every node in
#              the left subtree must be less than its parent and all previous nodes.
#           2. At every node, for the right subtree, we will set the current_min to the current node i.e., every node in
#              the right subtree must be greater than its parent and all previous nodes.
#           3. It ensures the global ordering instead of local immediate parent ordering as below.
#               1. When we start with the root node,
#                   1. Its left subtree must be within the range (-inf, root). Within the root's left subtree,
#                       1. This range will be (parent, root) for every node's right child, which ensures that
#                          "every right child node > its parent and < root".
#                       2. This range will be (right child's parent, right child) for every left child of right child's subtree,
#                          which ensures that "every right child's left child > right child's parent and < right child".
#                   2. Its right subtree must be within the range (root, +inf). Within the root's right subtree,
#                       1. This range will be (root, parent) for every node's left child, which ensures that
#                          "every left child node > root and < its parent".
#                       2. This range will be (left child, left child's parent) for every right child of left child's subtree,
#                          which ensures that "every left child's right child > left child and < left child's parent".
#   6. Otherwise, return true after all recursions.

def validate_bst_dfs_min_max(node, current_min=float('-inf'), current_max=float('+inf')):
    if not node:  # null
        return True

    if not node.val > current_min or not node.val < current_max:
        return False

    return (validate_bst_dfs_min_max(node.left, current_min, node.val) and
            validate_bst_dfs_min_max(node.right, node.val, current_max))


# Inorder Algorithm:
#   1. Start with the root node.
#   2. Use DFS inorder traversal to traverse all elements in the ascending sorted order from left to node to right.
#   3. Initialize node = root, prev_node_val = []
#   4. If the current node is not valid then return true as we would have reached the null node (null child of a leaf node),
#      and it doesn't affect/violate the BST ordering.
#   5. Perform an inorder traversal,
#       1. Traverse from root to the left-most leaf node recursively.
#       2. Since there are no children for leaf, it will recursively traverse back to the leaf's parent node.
#       3. Now, traverse from parent node to the right-most leaf node recursively.
#       4. At each node during the traversal,
#           1. Compare the current node's value with the prev_node_val[0].
#               1. If "current node < prev_node_val[0]" then return false as it's violating the BST inorder ascending
#                  sorted order from left to node to right and stop the traversal.
#               2. Else, Set "prev_node_val[0] = current node" and continue the traversal.

def validate_bst_dfs_inorder(node, prev_node_val):
    if not node:
        return True

    is_valid = validate_bst_dfs_inorder(node.left, prev_node_val)
    if not is_valid:
        return False

    if prev_node_val and not node.val > prev_node_val.pop():
        return False

    prev_node_val.append(node.val)

    return validate_bst_dfs_inorder(node.right, prev_node_val)
