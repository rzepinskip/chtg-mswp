import networkx as nx
import matplotlib.pyplot as plt
from typing import List


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


def read_graph_dimacs_format(inputfile):
    G = nx.Graph()
    solution = None

    with open(inputfile, newline=None) as f:
        for line in f:
            first_char = line[0]
            if first_char == "c" or first_char == "p":
                continue
            elif first_char == "e":
                _, source, target = line.strip().split(" ")
                G.add_edge(int(source), int(target))
            elif first_char == "v":
                _, node, weight = line.strip().split(" ")
                G.node[int(node)]["weight"] = int(weight)
            elif first_char == "s":
                _, solution = line.strip().split(" ")
                solution = int(solution)
            else:
                raise ValueError("Invalid line beginning")

    if len(nx.get_node_attributes(G, 'weight')) == 0:
        nx.set_node_attributes(G, 1, 'weight')
    return G, solution
