# In graphs, breadth first search (BFS) can be used to determine the shortest path, closest nodes, etc.
#   E.g., BFS is used in Google Maps to get similar recommendations, searching things near me, etc.

# Pros:
#   1. Shortest path
#   2. Finding the closest nodes
# Cons:
#   1. More memory to store descendant nodes/vertices.

# One downside with finding the shortest path with BFS is that it can't be used with weighted graphs (e.g., Google Maps)
# Hence, we have the below algorithms to get the shortest path in a weighted graph.
#   1. Dijkstra algorithm
#   2. Bellman-Ford algorithm
#
#   - Bellman-Ford algorithm is more capable/effective at solving the shorted path since it can accommodate
#     negative weights in a graph.
#   - However, it's relatively slower than Dijkstra's algorithm in time complexity. The worst
#     case time complexity is O(n^2).
#   - Hence, if there are no negative weights then Dijkstra's algorithm is preferred over Bellman-Ford algorithm.
