# DFS can be implemented in 3 ways:
#   1. Inorder
#   2. Preorder
#   3. Postorder

# Inorder (Left -> Parent -> Right):
#   1. All elements will be visited in order from left to parent to right nodes.
#   2. Especially useful in case of binary search trees ot traverse all elements in a sorted order.
#       E.g.,
#               9
#             /  \
#           4     20
#         /  \   /  \
#        1    6 15   170
#
#     dfs_inorder = [1, 4, 6, 9, 15, 20, 170] --> sorted order

# Preorder (Parent -> Left -> Right) [Top-down traversal]:
#   1. Visit parent before children from parent to left to right nodes.
#   2. Useful to rebuild the original tree from DFS traversal result.
#       E.g.,
#               9
#             /  \
#           4     20
#         /  \   /  \
#        1    6 15   170
#
#     dfs_preorder = [9, 4, 1, 6, 20, 15, 170]

# Postorder (Left -> Right -> Parent) [Bottom-up traversal]:
#   1. Visit children before parent from left to right to parent nodes.
#   2. Useful in cases where children needs to be processed before parent. E.g., deleting/freeing a tree bottom-up
#       E.g.,
#               9
#             /  \
#           4     20
#         /  \   /  \
#        1    6 15   170
#
#     dfs_postorder = [1, 6, 4, 15, 170, 20, 9]

from CustomDataStructures.custom_binary_search_tree import CustomBinarySearchTree

bst = CustomBinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(1)
bst.insert(15)


# Inorder Implementation:
# Algorithm: (Visits left child and parent and then right child)
#   1. Start with the root node and dfs_inorder_result = [].
#   2. Traverse to the left-most leaf node recursively.
#   3. Once we reach the leaf node then add the left-most leaf node to the "dfs_inorder_result".
#   4. Since there are no children for leaf node, it will recursively traverse back to the node (parent) and
#      add it to the "dfs_inorder_result".
#   5. Now, traverse to the right-most leaf node recursively, which will implicitly repeat steps 2-3 and add all the
#      leaf nodes to the result.
#   6. Return the dfs_inorder_result.

def dfs_inorder(node, dfs_inorder_result):
    # print(node.value)
    if node.left:
        dfs_inorder(node.left, dfs_inorder_result)

    dfs_inorder_result.append(node.value)

    if node.right:
        dfs_inorder(node.right, dfs_inorder_result)

    return dfs_inorder_result


print(dfs_inorder(bst.root, []))


# Preorder Implementation:
# Algorithm: (Visits parent first and then children)
#   1. Start with the root node and dfs_preorder_result = [].
#   2. Add the node (parent) first to the "dfs_preorder_result".
#   3. Traverse to the left-most leaf node recursively.
#   4. Now, traverse to the right-most leaf node recursively.
#   5. Return the dfs_preorder_result.

def dfs_preorder(node, dfs_preorder_result):
    # print(node.value)
    dfs_preorder_result.append(node.value)
    if node.left:
        dfs_preorder(node.left, dfs_preorder_result)

    if node.right:
        dfs_preorder(node.right, dfs_preorder_result)

    return dfs_preorder_result


print(dfs_preorder(bst.root, []))


# Postorder Implementation:
# Algorithm: (Visits children first and then parent)
#   1. Start with the root node and dfs_postorder_result = [].
#   2. Traverse to the left-most leaf node recursively.
#   3. Once we reach the leaf node then add the left-most leaf node to the "dfs_postorder_result".
#   4. Now, traverse to the right-most leaf node recursively.
#   5. Once we reach the leaf node then add the right-most leaf node to the "dfs_postorder_result".
#   6. After visiting children, it will recursively traverse back to the node (parent) and add it to the "dfs_postorder_result".
#   5. Return the dfs_postorder_result.

def dfs_postorder(node, dfs_postorder_result):
    # print(node.value)
    if node.left:
        dfs_postorder(node.left, dfs_postorder_result)

    if node.right:
        dfs_postorder(node.right, dfs_postorder_result)

    dfs_postorder_result.append(node.value)

    return dfs_postorder_result


print(dfs_postorder(bst.root, []))
