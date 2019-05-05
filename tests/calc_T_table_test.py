import pytest

import networkx as nx
from mswp.algo import calc_T_table


# def test_basic():
#     G = nx.Graph()
#     G.add_nodes_from(
#         [
#             (1, dict(weight=1)),
#             (2, dict(weight=1)),
#             (3, dict(weight=1)),
#             (4, dict(weight=1)),
#             (5, dict(weight=20)),
#             (6, dict(weight=20)),
#         ]
#     )
#     G.add_edges_from([(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4)])

#     W = max([attr["weight"] for node, attr in G.nodes.items()])
#     calc_T_table(G, frozenset(G.nodes), W)

def test_basic():
    G = nx.Graph()
    G.add_nodes_from(
        [
            (1, dict(weight=1)),
            (2, dict(weight=1)),
            (3, dict(weight=1)),
        ]
    )
    G.add_edges_from([(1, 2),(2,3)])

    expected_result = {
        (frozenset({1, 2, 3}), 1, 0): 0,
        (frozenset({1, 2, 3}), 1, 1): 0,
        (frozenset({1, 2, 3}), 1, 2): 0,
        (frozenset({1, 2, 3}), 1, 3): 0,
        (frozenset({1, 2}), 1, 0): 0,
        (frozenset({1, 2}), 1, 1): 1,
        (frozenset({1, 2}), 1, 2): 0,
        (frozenset({1, 2}), 1, 3): 0,
        (frozenset({2, 3}), 1, 0): 0,
        (frozenset({2, 3}), 1, 1): 1,
        (frozenset({2, 3}), 1, 2): 0,
        (frozenset({2, 3}), 1, 3): 0,
        (frozenset({1, 3}), 1, 0): 0,
        (frozenset({1, 3}), 1, 1): 1,
        (frozenset({1, 3}), 1, 2): 0,
        (frozenset({1, 3}), 1, 3): 0,
        (frozenset({1}), 1, 0): 0,
        (frozenset({1}), 1, 1): 2,
        (frozenset({1}), 1, 2): 0,
        (frozenset({1}), 1, 3): 0,
        (frozenset({2}), 1, 0): 0,
        (frozenset({2}), 1, 1): 2,
        (frozenset({2}), 1, 2): 1,
        (frozenset({2}), 1, 3): 0,
        (frozenset({3}), 1, 0): 0,
        (frozenset({3}), 1, 1): 2,
        (frozenset({3}), 1, 2): 0,
        (frozenset({3}), 1, 3): 0,
        (frozenset(), 1, 0): 0,
        (frozenset(), 1, 1): 3,
        (frozenset(), 1, 2): 1,
        (frozenset(), 1, 3): 0
    }

    W = max([attr["weight"] for node, attr in G.nodes.items()])
    T = calc_T_table(G, frozenset(G.nodes), W)
    assert T == expected_result
