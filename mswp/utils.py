import networkx as nx
import matplotlib.pyplot as plt
from typing import List


def get_sample_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node(1, weight=1)
    G.add_node(2, weight=1)
    G.add_node(3, weight=1)
    G.add_node(4, weight=1)
    G.add_node(5, weight=20)
    G.add_node(6, weight=20)
    G.add_edges_from([(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4)])
    return G


def draw_graph(G: nx.Graph, node_pos: List[int] = None):
    node_attrs = nx.get_node_attributes(G, "weight")
    custom_node_attrs = {}
    for node, attr in node_attrs.items():
        custom_node_attrs[node] = f"{node} ({str(attr)})"

    args = {"labels": custom_node_attrs, "font_weight": "bold", "node_size": 2000}
    if node_pos is not None:
        args["pos"] = node_pos

    nx.draw(G, **args)
    plt.show()


def draw_bipartite_graph(G: nx.Graph):
    odd_nodes = [v for v in G.nodes if v % 2 == 1]
    node_pos = nx.drawing.layout.bipartite_layout(G, odd_nodes)
    draw_graph(G, node_pos)
