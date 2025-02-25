import networkx as nx
from matplotlib import pyplot as plt

from component.node import Node


class Network:
    def __init__(self, nodes: list, fog_nodes: list):
        self.nodes = nodes
        self.fog_nodes = fog_nodes

        self.edge_servers = [x for x in nodes if x.is_server_placed]

        self.graph = nx.Graph()
        self.graph.add_nodes_from(nodes)
        self.graph.add_nodes_from(fog_nodes)

        for node in self.nodes:
            x = node.x
            y = node.y

            node_n = Node.get_node_by_coordinates(x, y + 1)
            node_e = Node.get_node_by_coordinates(x + 1, y)
            node_s = Node.get_node_by_coordinates(x, y - 1)
            node_w = Node.get_node_by_coordinates(x - 1, y)

            if node_n:
                self.graph.add_edge(node, node_n)
            if node_e:
                self.graph.add_edge(node, node_e)
            if node_s:
                self.graph.add_edge(node, node_s)
            if node_w:
                self.graph.add_edge(node, node_w)

        for fog_node in self.fog_nodes:
            for node in self.nodes:
                self.graph.add_edge(fog_node, node)

    def draw_graph(self):
        graph = self.graph

        # Draw the graph
        pos = nx.spring_layout(graph, seed=42)  # Positions for all nodes
        node_types = []
        for node in graph.nodes:
            if isinstance(node, Node):
                if node.is_server_placed:
                    node_types.append('es')
                else:
                    node_types.append('bs')
            else:
                node_types.append('fs')
        color_map = {'bs': 'blue', 'es': 'green', 'fs': 'red'}
        node_color_list = [color_map[node_type] for node_type in node_types]

        plt.figure(figsize=(12, 8))

        # Draw the nodes and edges
        nx.draw(graph, pos, with_labels=True, node_color=node_color_list, node_size=700, font_size=10,
                font_color='black')

        # Draw edge labels with bitrate values
        #edge_labels = {(u, v): f"{d['bitrate']}" for u, v, d in graph.edges(data=True)}
        #nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')

        plt.show()
