# In graphs, breadth first search (BFS) can be used to determine the shortest path, closest nodes, etc.
#   E.g., BFS is used in Google Maps to get similar recommendations, searching things near me, etc.

# Pros:
#   1. Shortest path
#   2. Finding the closest nodes
# Cons:
#   1. More memory to store descendant nodes/vertices.

# One downside with finding the shortest path with BFS is that it can't be used with weighted graphs (e.g., Google Maps)
# Hence, we have the below algorithms to get the shortest path in a weighted graph.
#   1. Dijkstra's algorithm
#   2. Bellman-Ford algorithm
#
#   - Bellman-Ford algorithm is more capable/effective at solving the shorted path since it can accommodate
#     negative weights in a graph.
#   - However, it's relatively slower than Dijkstra's algorithm in time complexity. The worst
#     case time complexity is O(n^2).
#   - Hence, if there are no negative weights then Dijkstra's algorithm is preferred over Bellman-Ford algorithm.

# Algorithm (Adjacency list):
#   1. Start at a source vertex 'a'.
#   2. Initialize vertices_to_traverse = queue([a]), visited_vertices = set().
#   3. Traverse all immediate neighbours of 'a' and check if a neighbour has been already visited.
#       1. If not in visited_vertices then add it to the 'vertices_to_traverse' in the order of traversal to traverse them next as
#          required in BFS.
#       2. If already in visited_vertices then skip adding to the 'vertices_to_traverse' to avoid duplication of pending vertices to traverse.
#   4. Repeat step 3 until all vertices are visited.

# Time Complexity:
#   - Although, for every vertex, we are having a nested loop to iterate over all its neighbours, the nested loop is
#     dependent on the outer iteration and can run variable number of times for each vertex. Hence, the total work will
#     be calculated as follows:
#       - Total outer loop work: O(number of vertices) = O(V)
#       - Total inner loop work (for all outer iterations):
#           O(degree of each vertex) = O(outgoing and incoming edges of each vertex) = O(Total number of edges overall)
#               = O(E) for directed graph or O(2E) for undirected graph
#               ≈ O(E)
#   - Total work = O(V) + O(E) = O(V+E)

# Space Complexity: O(V) + O(V) = O(V)

from collections import deque
from CustomDataStructures.custom_graph import CustomGraph


def graph_bfs(graph: CustomGraph, source_vertex):
    vertices_to_traverse = deque([source_vertex])
    visited_vertices = {source_vertex}
    traversal_path = {}

    while len(vertices_to_traverse) > 0:
        current_vertex = vertices_to_traverse.popleft()
        traversal_path[current_vertex] = set()

        vertex_neighbours = graph.adjacency_list.get(current_vertex, [])
        for vertex_neighbour in vertex_neighbours:
            traversal_path[current_vertex].add(vertex_neighbour)

            if not vertex_neighbour in visited_vertices:
                visited_vertices.add(vertex_neighbour)
                vertices_to_traverse.append(vertex_neighbour)

    return traversal_path


g = CustomGraph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_edge('3', '1')
g.add_edge('1', '3')
g.add_edge('3', '4')
g.add_edge('4', '2')
g.add_edge('4', '5')
g.add_edge('1', '2')
g.add_edge('1', '0')
g.add_edge('0', '2')
g.add_edge('6', '5')

print(graph_bfs(g, '0'))
