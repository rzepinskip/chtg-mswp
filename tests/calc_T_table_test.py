import pytest

import networkx as nx
from mswp.algo import calc_T_table


def test_basic():
    G = nx.Graph()
    G.add_nodes_from(
        [
            (1, dict(weight=1)),
            (2, dict(weight=1)),
            (3, dict(weight=1)),
            (4, dict(weight=1)),
            (5, dict(weight=20)),
            (6, dict(weight=20)),
        ]
    )
    G.add_edges_from([(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4)])

    W = max([attr["weight"] for node, attr in G.nodes.items()])
    calc_T_table(G, frozenset(G.nodes), W)
