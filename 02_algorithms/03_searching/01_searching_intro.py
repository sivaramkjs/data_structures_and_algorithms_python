# Search is one of the most used functions in both real-world and computer.
# There are different types of searches:

#   Linear search:
#       - Sequentially finding an item in a list.
#       - Best case time complexity - O(1) [desired item is the 1st item]
#       - Worst case time complexity - O(n) [desired item is either the last item or item doesn't exist]

#   Binary search:
#       - Searching through sorted data using divide and conquer. E.g., Sorted array, Binary search tree, etc.
#       - Worst case time complexity - O(log n)

#   Traversal:
#       - Finding a node or visiting every node in a tree/graph.
#       - Worst case time complexity - O(n) since we will need to visit all nodes
#       - There are two types of traversal:
#           - Breadth First Search (BFS)
#           - Depth First Search (DFS)
#       Breadth First Search (BFS):
#           - Traversing from root node to all other nodes from left to right (breadth) at each level.
#           - It used additional memory to store all the children of each node at every level to traverse from left to
#             right in the next level.
#           E.g., Traversal steps (s)
#               9
#           s1/ s2\
#           6     12
#       s3/ s4\ s5/ s6\
#       1     4 34    45
#
#       Depth First Search (DFS):
#           - Traversing from root node to the deepest left leaf node and then traversing back to the nearest ancestor/parent
#             node of the deepest traversed node and then similar traversing to the other unvisited child subtrees of the ancestor/parent.
#           - Repeating this traversal process until all nodes are visited from the deepest left to the deepest right subtrees in order.
#           - It used less memory than BFS since it needs to store less data (only the nearest ancestor/parent) during traversal.
#           E.g., Traversal steps (s)
#               9
#           s1/ s4\
#           6     12
#       s2/ s3\ s5/ s6\
#       1     4 34    45
#
#       BFS vs DFS:
#           BFS:
#               Pros:
#                   Shortest path between a source node and other reachable nodes since we always start with root node
#                   and search the closest nodes first and then further nodes. This will be most apparent in case of graph traversal.
#               Cons:
#                   More memory to store additional data at each level.
#
#           DFS:
#               Pros:
#                   1. Less memory to store additional data at each level.
#                   2. Useful to check path existence (in case of graphs).
#
#               Cons:
#                   Can get slow if a tree/graph is huge.
