import networkx as nx
import matplotlib.pyplot as plt
from typing import List


def get_sample_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(
        [
            (1, dict(weight=1)),
            (2, dict(weight=1)),
            # (3, dict(weight=1)),
            # (4, dict(weight=1)),
            (5, dict(weight=3)),
            (6, dict(weight=3)),
        ]
    )
    G.add_edges_from([(1, 2), (1, 6), (5, 2)])
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
