"""
# Dijkstra's shortest path algorithm (Single Source Shortest path):
#   1. It is used to find the shortest path between a source node/vertex and other nodes/vertices in a non-negative
#      weighted graph.
#   2. It works by selecting a starting source node and computing the distance/cost to visit each other node from it.
#   3. Initially, it marks all nodes as "unvisited" and assigns traversal distance/cost for all nodes from the source node
#      in the graph as below.
#       1. Assigns "0" to itself.
#       2. Assigns "infinity" to all other nodes since the traversal cost is not known yet.
#   4. It selects the next unvisited node with the lowest traversal cost from the unvisited nodes list.
#       1. At start, this will be the source node with "0" cost.
#   5. It will then traverse to all neighbours of the selected node and computes the traversal cost to those
#      nodes from it using the below formula.
#       1. Traversal cost/distance = (selected node cost from source node) + (edge weight between selected node and neighbour node)
#   6. It will then compare this new traversal cost to the current traversal cost assigned to the neighbour node.
#       1. If the new cost is greater than current cost then it will skip the update as the current cost is already shortest.
#       2. Otherwise, it will update the traversal cost of the neighbour node to the new shortest/lowest cost.
#       3. This process is called "Relaxation" of edges/vertices.
#   7. After visiting all neighbours of the selected node, marks it as visited and never revisits the same node. Hence,
#      this is a "greedy" algorithm i.e., rarely it may result in suboptimal solution.
#   8. Repeats steps 4-7 until all nodes are visited.

# Time Complexity:
#   1. For Dijkstra's algorithm, it depends on which data structure we use to store the unvisited nodes with cost.
#   2. This is because, we will need to visit/traverse all nodes at most. For each (node) iteration, we will need to find
#      the next unvisited node with the lowest cost to continue the traversal.
#
#   "V" - Total number of vertices/nodes
#   "E" - Total number of edges
#
#   Storing unvisited nodes in an array:
#       1. Finding the next unvisited node with the lowest cost will require iterating through all nodes to check
#          whether already visited or not and find an unvisited node with the lowest cost.
#           1. Total work for finding the next unvisited node:
#                   Number of (vertices) iterations * work for finding the next unvisited node = O(V * V) = O(V^2)
#       2. After finding the unvisited node, we will need to visit all its neighbours and may update their costs.
#           1. Total work for visiting all neighbours = O(number of edges overall) = O(E)
#           2. Total work for updating each neighbour's cost in array = O(1)
#       3. Total time complexity = O(V^2) + O(E) ≈ O(V^2)
#
#   Storing unvisited nodes in a binary min heap (priority queue):
#       1. We can use min heap to always contain the next unvisited node with the lowest cost at the top.
#       2. Total work for building the min heap = O(V)
#       3. Total work for finding the next unvisited node:
#           1. Extract top item from min heap + heapify new top = O(1) + O(log V) ≈ O(log V)
#           2. Number of (vertices) iterations * work for finding the next unvisited node = O(V log V)
#       4. After finding the unvisited node, we will need to visit all its neighbours and may update their costs.
#           1. Total work for visiting all neighbours = O(number of edges overall) = O(E)
#           2. Total work for updating each neighbour's cost:
#               1. After updating a node's cost, we will need to heapify the min heap from the node to the top similar to
#                  inserting a new item into the heap. This is because we will update the cost only if the new value is
#                  less than the current value in which case the new value must be already less than the node's children
#                  in the min heap.
#                   1. Total work for up-heapify (sift-up) = O(log V)
#           3. Total work for visiting all neighbours and updating each neighbour's cost = O(E * log V) = O(E log V)
#       3. Total time complexity = O(V) + O(V log V) + O(E log V) ≈ O((V+E) log V))
#
#   3. We can further optimize this to "O(E + V log V)" using Fibonacci heap, but it's highly complicated to implement.

# Space Complexity:
#   We will need to store all unvisited vertices data ≈ O(V)

# Algorithm:
#   1. Start at a source node 'a'.
#   2. Initialize unvisited_nodes = min_heap(), node_traversal_costs = {}.
#   3. Mark all nodes as "unvisited" and assigns traversal cost for all nodes from the source node as below.
#       1. Assigns "0" to itself.
#       2. Assigns "infinity" to all other nodes since the traversal cost is not known yet.
#   4. Build min_heap with heap property as each node's traversal cost from 'a'.
#   5. Loop through nodes until the heap is empty.
#       1. Extract the next unvisited node with the lowest traversal cost, from the unvisited_nodes heap. Set it as current_node.
#       2. Traverse all its neighbours and update their cost.
#           1. For each neighbour, compute the new traversal cost as below.
#               1. new_traversal_cost = current_node.traversal_cost + neighbour_edge_weight
#           2. Compare new_traversal_cost with neighbour_traversal_cost.
#               1. If new_traversal_cost > neighbour_traversal_cost then skip update and move to the next neighbour.
#               2. If new_traversal_cost < neighbour_traversal_cost then update the neighbour_traversal_cost to the
#                  new_traversal_cost in the "node_traversal_costs".
#                   1. For this update, we will simply push a new entry into the heap with the updated cost instead of updating
#                      the old entry arbitrarily inside the heap. Otherwise, we will need to find the position of the
#                      neighbour in order to up-heapify from its position to the root of the heap. This lookup will take
#                      "O(V)" time and complex to implement. Hence, despite needing an extra memory to store additional
#                      old/stale entries (maximum "E" for all edges), pushing a new entry and extracting the top will be
#                      simpler to implement and still runs in O((V+E) log V) time.
#                   2. Up-heapify from the new (last) index to the root in the unvisited_nodes heap.
#           3. After visiting all neighbours, add the current_node to visited_nodes.
"""

from CustomDataStructures.custom_weighted_graph import CustomWeightedGraph, GraphNode
import heapq
from itertools import count


def dijkstra_shortest_paths(graph: CustomWeightedGraph, source_node):
    node_traversal_costs, unvisited_nodes, counter = initialize_node_traversal_costs(graph, source_node)
    heapq.heapify(unvisited_nodes)

    while len(unvisited_nodes) > 0:
        current_node_cost, _, current_node = heapq.heappop(unvisited_nodes)
        # print(current_node.value)

        for edge in current_node.adjacency_list:
            new_traversal_cost_from_source = current_node_cost + edge.weight
            neighbour_node = edge.to_node

            # print(neighbour_node.value, new_traversal_cost_from_source)

            if new_traversal_cost_from_source < node_traversal_costs[neighbour_node.value]:
                node_traversal_costs[neighbour_node.value] = new_traversal_cost_from_source

                heapq.heappush(unvisited_nodes, (new_traversal_cost_from_source, next(counter), neighbour_node))

    return node_traversal_costs


def find_dijkstra_shortest_path(graph: CustomWeightedGraph, source_node, target_node):
    node_traversal_costs, unvisited_nodes, counter = initialize_node_traversal_costs(graph, source_node)
    heapq.heapify(unvisited_nodes)

    while len(unvisited_nodes) > 0:
        current_node_cost, _, current_node = heapq.heappop(unvisited_nodes)
        # print(current_node.value)
        """
        # 1. Return the target_node cost when we extract it from the heap.
        # 2. At this point, it will be having the cheapest cost from source_node since it is at the top of the heap.
        #    Additionally, all other paths after the target_node will be either equal or greater than the current cost.
        # 3. This is also due to the fact that any successive path's cost will be either
        #    "current target_node cost + next non-negative edge cost" or
        #    "other higher unvisited path (as target_node was smallest before it) cost + next 'non-negative' edge cost"
        # 4. This works as long as there are no negative edge costs.
        #       1. This is exactly why Dijkstra's algorithm can't guarantee the accurate outcome with negative weights.
        #
        # E.g., Consider the following paths from A to D.
        #           A--1-->B--3-->D
        #           A--1-->C--4-->E--1-->D
        #       Steps:
        #           1. {A: 0, B: ∞, C: ∞, D: ∞, E: ∞}
        #           2. After visiting B and C: {(A): 0, B: 1, C: 1, D: ∞, E: ∞}, ()-already extracted from heap
        #           3. Extract min: B
        #           4. After visiting D from B: {(A): 0, (B): 1, C: 1, D: 4, E: ∞}
        #           5. Extract min: C
        #           6. After visiting E from C: {(A): 0, (B): 1, (C): 1, D: 4, E: 5}
        #           7. Extract min: D
        #               1. This is the cheapest path to D compared to any other unvisited path costs in the heap.
        #               2. Any other path would be either equal or greater than this cost for any non-negative costs.
        #               3. This fails in case of negative weights. E.g., "E: -4"
        """
        if target_node == current_node.value:
            cost = node_traversal_costs[current_node.value]
            return cost if cost != float('+inf') else None

        for edge in current_node.adjacency_list:
            new_traversal_cost_from_source = current_node_cost + edge.weight
            neighbour_node = edge.to_node

            # print(neighbour_node.value, new_traversal_cost_from_source)

            if new_traversal_cost_from_source < node_traversal_costs[neighbour_node.value]:
                node_traversal_costs[neighbour_node.value] = new_traversal_cost_from_source

                heapq.heappush(unvisited_nodes, (new_traversal_cost_from_source, next(counter), neighbour_node))

    return None


def initialize_node_traversal_costs(graph: CustomWeightedGraph, source_node):
    costs = {}
    nodes = []
    counter = count()

    for value, node in graph.nodes.items():
        if value == source_node:
            costs[value] = 0
            # Since heapq doesn't allow a custom comparer function, passing tuple-list with key as 1st item,
            # unique counter value as 2nd item to server as tie-breaker for same 1st item for multiple tuples.
            nodes.append((0, next(counter), node))
        else:
            # Initialize all nodes except source node with '+inf' cost
            costs[value] = float('+inf')
            nodes.append((float('+inf'), next(counter), node))
    return costs, nodes, counter


g = CustomWeightedGraph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_directed_edge('1', '3', 12)
g.add_directed_edge('3', '4', 10)
g.add_directed_edge('4', '2', 13)
g.add_directed_edge('4', '5', 16)
g.add_directed_edge('1', '2', 20)
g.add_directed_edge('2', '1', 1)
g.add_directed_edge('0', '1', 7)
g.add_directed_edge('0', '2', 5)
g.add_directed_edge('6', '5', 11)

# print(dijkstra_shortest_paths(g, '0'))
print(find_dijkstra_shortest_path(g, '0', '1'))
