import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict


def get_sample_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(
        [
            (1, dict(weight=1)),
            (2, dict(weight=1)),
            (3, dict(weight=1)),
            (4, dict(weight=1)),
            (5, dict(weight=5)),
            (6, dict(weight=5)),
        ]
    )
    G.add_edges_from([(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4)])
    return G


def draw_graph(
    G: nx.Graph, nodes_pos: List[int] = None, color_mapping: Dict[int, int] = None
):
    node_attrs = nx.get_node_attributes(G, "weight")
    custom_node_attrs = {}
    for node, attr in node_attrs.items():
        custom_node_attrs[node] = f"{node} ({str(attr)})"

    args = {"labels": custom_node_attrs, "font_weight": "bold", "node_size": 2000}
    if nodes_pos is not None:
        args["pos"] = nodes_pos
    if color_mapping is not None:
        args["node_color"] = [color_mapping[v] for v in G.nodes]

    nx.draw(G, **args)
    plt.show()


def draw_bipartite_graph(G: nx.Graph, color_mapping: Dict[int, int] = None):
    odd_nodes = [v for v in G.nodes if v % 2 == 1]
    nodes_pos = nx.drawing.layout.bipartite_layout(G, odd_nodes)
    draw_graph(G, nodes_pos, color_mapping)
