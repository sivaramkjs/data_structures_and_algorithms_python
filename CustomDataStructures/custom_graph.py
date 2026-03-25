class CustomGraph:
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

    def add_directed_edge(self, node1, node2):  # directed graph
        try:
            node1_adjacency_list = self.adjacency_list[node1]
        except KeyError:
            raise ValueError("node1 doesn't exist")

        node1_adjacency_list.append(node2)

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
