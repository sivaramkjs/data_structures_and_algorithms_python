# A graph is a set of values that are related in a specific way.
# Each item is called a node or a vertex.
# Nodes/vertices are connected through links called "Edges".
# E.g.,
#      1 ⏤⏤⏤⏤ 2 (node)
#      \        / (edge)
#       3 ⏤⏤ 4

# They are highly useful to model or represent real world relationships.
#   E.g., Friendships, network, roads, etc.
# Tree is also a type of graph.

# Types of graphs:
#   1. Directed - Unidirectional (except in some cases). E.g., oneway street
#   2. Undirected - Bidirectional. E.g., highway between two cities
#   3. Weighted - Information in edges. E.g., Distance between cities
#   4. Unweighted - Information only in nodes. E.g., Friend names
#   5. Cyclic - Nodes/vertices are connected in a cycle.
#   6. Acyclic - No cycle between any nodes/vertices.

# One of the most commonly used graph type is DAG (Directed Acyclic Graph).

# A graph can be represented in 3 ways.
#      2 ⏤ 0
#    /  \
#   1 ⏤ 3
#
#   1. Edge list: All edges are represented as node value pairs with a third item representing weight in case of a weighted graph.
#       E.g., graph (array) = [[0, 2], [2, 3], [2, 1], [1, 3]]
#             weighted graph (array) = [[0, 2, 10], [2, 3, 11], [2, 1, 9], [1, 3, 5]]
#
#             graph (key-value pairs, key - edge index, value - edge nodes pair) = {
#                                           0: [0, 2],
#                                           1: [2, 3],
#                                           2: [2, 1],
#                                           3: [1, 3]
#                                       }
#
#             weighted graph (key-value pairs, key - edge index, value - edge nodes pair) = {
#                                                   0: [0, 2, 10],
#                                                   1: [2, 3, 11],
#                                                   2: [2, 1, 9],
#                                                   3: [1, 3, 5]
#                                                }
#
#   2. Adjacency list: Each entry represents all the adjacent nodes of a node.
#       E.g., graph (array) = [[2], [2, 3], [0, 1, 3], [1, 2]] -- Array index corresponds to the actual node value in this case.
#
#      1. In case of non-numeric or random number node values, we will use a key-value pair structure with node value as key and adjacent nodes list as value
#           E.g., graph (key-value pairs) = {
#                                               0: [2],
#                                               1: [2, 3],
#                                               2: [0, 1, 3],
#                                               3: [1, 2]
#                                           }
#
#       2. In case of a weighted graph, we will use a key-value pair structure with node value as key and adjacent node and weight pairs list as value
#                 weighted graph (key-value pairs) = {
#                                                       0: [[2, 10]],
#                                                       1: [[2, 9] , [3, 5]],
#                                                       2: [[0, 10], [1, 9], [3, 11]],
#                                                       3: [[1, 5], [2, 11]]
#                                                    }
#
#   3. Adjacency matrix:
#       1. Represents graph in a matrix structure as "nxn matrix" where n is number of nodes.
#       2. For an unweighted graph, each entry will be either 1 (connected) or 0 (unconnected) that represents node connections or edges.
#           E.g., graph (array, index corresponds to the actual node value in this case.) = [
#                               [0, 0, 1, 0], (index node value "0" connected to "2")
#                               [0, 0, 1, 1], (index node value "1" connected to "2", "3")
#                               [1, 1, 0, 1],
#                               [0, 1, 1, 0],
#                             ]
#
#           E.g., graph (key-value pair structure with node value as key and adjacency matrix row)  = {
#                               0: [0, 0, 1, 0],
#                               1: [0, 0, 1, 1],
#                               2: [1, 1, 0, 1],
#                               3: [0, 1, 1, 0],
#                             }
#       3. In case of a weighted graph, we will use actual edge weight in place of "1".
#           E.g., graph (key-value pair structure with node value as key and adjacency matrix row)  = {
#                               0: [0, 0, 10, 0],
#                               1: [0, 0, 9, 5],
#                               2: [10, 9, 0, 11],
#                               3: [0, 5, 11, 0],
#                             }
