from dataclasses import dataclass
from typing import Any


class CustomWeightedGraph:
    def __init__(self):
        self.no_of_nodes = 0
        self.nodes = dict[Any, GraphNode]()

    def add_vertex(self, value):
        node = self.nodes.get(value, False)
        if node == False:
            self.nodes[value] = GraphNode(value, [])
            self.no_of_nodes += 1

    def add_edge(self, node1_val, node2_val, weight):  # undirected graph
        try:
            node1 = self.nodes[node1_val]
            node2 = self.nodes[node2_val]
            node1_adjacency_list = node1.adjacency_list
            node2_adjacency_list = node2.adjacency_list
        except KeyError:
            raise ValueError("node1 or node2 doesn't exist")

        node1_adjacency_list.append(GraphEdge(node1, node2, weight))
        node2_adjacency_list.append(GraphEdge(node2, node1, weight))

    def add_directed_edge(self, node1_val, node2_val, weight):  # directed graph
        try:
            node1 = self.nodes[node1_val]
            node2 = self.nodes[node2_val]
            node1_adjacency_list = node1.adjacency_list
        except KeyError:
            raise ValueError("node1 or node2 doesn't exist")

        node1_adjacency_list.append(GraphEdge(node1, node2, weight))

    def show_node_connections(self):
        if not self.nodes:
            print('empty graph')
            return

        for node_val, node in self.nodes.items():
            node_connections = []
            if node:
                for adjacent_item in node.adjacency_list:
                    node_connections.append(f'[{adjacent_item.to_node.value}, {adjacent_item.weight}]')

                print(f'{node_val}-->{' '.join(node_connections)}')


@dataclass
class GraphNode:
    value: Any
    adjacency_list: list[GraphEdge]


@dataclass
class GraphEdge:
    from_node: GraphNode
    to_node: GraphNode
    weight: int
