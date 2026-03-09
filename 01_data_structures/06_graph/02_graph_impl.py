class MyGraph:
    def __init__(self):
        self.no_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, node):
        node_value = self.adjacency_list.get(node, False)
        if node_value == False:
            self.adjacency_list[node] = []
            self.no_of_nodes += 1

    def add_edge(self, node1, node2):  # undirected graph
        try:
            node1_adjacency_list = self.adjacency_list[node1]
            node2_adjacency_list = self.adjacency_list[node2]
        except KeyError:
            raise ValueError("node1 or node2 doesn't exist")

        node1_adjacency_list.append(node2)
        node2_adjacency_list.append(node1)

    def show_node_connections(self):
        if not self.adjacency_list:
            print('empty graph')
            return

        for node, adjacency_list in self.adjacency_list.items():
            node_connections = []
            if adjacency_list:
                for adjacent_item in adjacency_list:
                    node_connections.append(f'{adjacent_item}')

                print(f'{node}-->{' '.join(node_connections)}')


graph = MyGraph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')

graph.show_node_connections()
