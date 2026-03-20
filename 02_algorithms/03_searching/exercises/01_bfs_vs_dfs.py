# If you know a solution is not far from the root of the tree:
#   BFS due to traversing closest nodes first

# If the tree is very deep and solutions are rare:
#   BFS as DFS can be too slow due to high depth (recursion)

# If the tree is very wide:
#   DFS as it would be faster due to the low depth and BFS would need more memory

# If solutions are frequent but located deep in the tree:
#   DFS

# Determining whether a path exists between two nodes:
#   DFS as it's more like checking for two connected nodes through edges which implies depth and BFS could be slow (and can have
#   additional overhead of remembering all the previous ancestor nodes of a specific path)

# Finding the shortest path:
#   BFS due to traversing closest nodes first
