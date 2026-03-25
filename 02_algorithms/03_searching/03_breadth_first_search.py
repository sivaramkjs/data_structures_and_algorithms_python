from collections import deque
from CustomDataStructures.custom_binary_search_tree import CustomBinarySearchTree


# Algorithm:
#   1. Initialize bfs_result = [].
#   2. Use a queue data structure to keep track of the all nodes in each level from left to right in order to traverse
#      their children in the next level.
#       1. Queue will be ideal in this case to track all previous level nodes from left to right in the order they are
#          traversed (breadth first) and also dequeue them in the same order for the next level traversal.
#   3. Initialize the queue (previous_level_nodes) with the root node.
#   4. Loop until queue has at least one item.
#       1. Set current_node = first item from the queue.
#       2. If current_node has left child,
#           1. Add it to the "previous_level_nodes" queue.
#           2. Add it to the "bfs_result".
#       3. If current_node has right child,
#           1. Add it to the "previous_level_nodes" queue.
#           2. Add it to the "bfs_result".
#       4. Repeat steps 4.1-4.4 until loop ends
#   5. Return bfs_result.

def breadth_first_search(data: CustomBinarySearchTree):
    bfs_result = []
    previous_level_nodes = deque([data.root])

    while len(previous_level_nodes) > 0:
        current_node = previous_level_nodes.popleft()
        bfs_result.append(current_node.value)
        if current_node.left:
            previous_level_nodes.append(current_node.left)
        if current_node.right:
            previous_level_nodes.append(current_node.right)

    return bfs_result


def breadth_first_search_recursive(previous_level_nodes, bfs_result):
    if len(previous_level_nodes) == 0:
        return bfs_result

    # Since we are using a queue, the insertion and removal order will be FIFO. Hence, appending only the current node
    # value (left and right successively in each recursion) will result in the expected left to right order of nodes
    # for each level.
    current_node = previous_level_nodes.popleft()
    bfs_result.append(current_node.value)
    if current_node.left:
        previous_level_nodes.append(current_node.left)
    if current_node.right:
        previous_level_nodes.append(current_node.right)

    return breadth_first_search_recursive(previous_level_nodes, bfs_result)


bst = CustomBinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(1)
bst.insert(15)

print(breadth_first_search(bst))
print(breadth_first_search_recursive(deque([bst.root]), []))
