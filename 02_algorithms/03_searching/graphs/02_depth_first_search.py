# In graphs, depth first search (DFS) can be used to check if a path exits between nodes/vertices.
#   E.g., Finding an entry/exit in a maze/puzzle, finding if a route exists in Google Maps, etc.

# Pros:
#   1. Less memory since there is no need to store descendants.
#   2. Check if a path exists between nodes/vertices.
# Cons:
#   1. Can get slow if the graph is too deep.

# Algorithm (Adjacency list):
#   1. Start with a source vertex 'a'.
#   2. Initialize visited_vertices = set().
#   3. Add 'a' to the visited_vertices.
#   4. Traverse to immediate neighbours of 'a' one by one and continue to the deepest descendant in the path recursively.
#       1. Check if a neighbour has been already visited.
#       2. If it's already in visited_vertices then move to the next neighbour.
#       3. If it's not in visited_vertices then add it to the visited_vertices and traverse to the next descendant recursively.
#       4. Stop when there are no more descendants to visit.
#   5. Repeat step 4 until all vertices are visited.

# Time Complexity:
#   - We will do one recursive call for each vertex. So, total recursions: O(V).
#   - In each recursion, we will traverse all immediate neighbours of a vertex by depth. Since the number of neighbours
#     depend on and varies for each vertex, the total work for all recursions will be:
#       O(degree of each vertex) = O(outgoing and incoming edges of each vertex) = O(Total number of edges overall)
#               = O(E) for directed graph or O(2E) for undirected graph
#               ≈ O(E)
#   - Total work = O(V) + O(E) = O(V+E)

# Space Complexity: O(V)

from CustomDataStructures.custom_graph import CustomGraph


def graph_dfs(graph: CustomGraph, vertex, visited_vertices, traverse_path):
    visited_vertices.add(vertex)

    vertex_neighbours = graph.adjacency_list.get(vertex, [])
    for vertex_neighbour in vertex_neighbours:
        traverse_path.append(vertex)
        traverse_path.append(vertex_neighbour)

        if not vertex_neighbour in visited_vertices:
            graph_dfs(graph, vertex_neighbour, visited_vertices, traverse_path)

    return traverse_path


g = CustomGraph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_directed_edge('0', '1')
g.add_directed_edge('1', '2')
g.add_directed_edge('2', '3')
g.add_directed_edge('3', '4')
g.add_directed_edge('4', '5')
g.add_directed_edge('0', '2')
g.add_directed_edge('2', '4')
g.add_directed_edge('5', '6')
g.add_directed_edge('6', '2')

print(graph_dfs(g, '0', set(), []))
