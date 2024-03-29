import pytest

import networkx as nx
from mswp.algo import MSWPAlgo


def test_basic():
    G = nx.Graph()
    G.add_nodes_from(
        [
            (1, dict(weight=1)),
            (2, dict(weight=1)),
            (3, dict(weight=3)),
            (4, dict(weight=3)),
        ]
    )
    G.add_edges_from([(1, 2), (1, 4), (2, 3)])
    W = max([attr["weight"] for node, attr in G.nodes.items()])
    V = frozenset(G.nodes)
    algo = MSWPAlgo(G)
    expected_result = algo._get_empty_T_table(V, W)
    expected_result[(V - {1}, 1, 1)] = 1
    expected_result[(V - {2}, 1, 1)] = 1
    expected_result[(V - {3}, 3, 1)] = 1
    expected_result[(V - {4}, 3, 1)] = 1
    expected_result[(V - {1, 2}, 1, 1)] = 2
    expected_result[(V - {1, 3}, 1, 1)] = 1
    expected_result[(V - {1, 3}, 3, 1)] = 1
    expected_result[(V - {1, 3}, 3, 2)] = 1
    expected_result[(V - {1, 4}, 1, 1)] = 1
    expected_result[(V - {1, 4}, 3, 1)] = 1
    expected_result[(V - {2, 3}, 1, 1)] = 1
    expected_result[(V - {2, 3}, 3, 1)] = 1
    expected_result[(V - {2, 4}, 1, 1)] = 1
    expected_result[(V - {2, 4}, 3, 1)] = 1
    expected_result[(V - {2, 4}, 3, 2)] = 1
    expected_result[(V - {3, 4}, 3, 1)] = 2
    expected_result[(V - {3, 4}, 3, 2)] = 1
    expected_result[(V - {1, 2, 3}, 1, 1)] = 2
    expected_result[(V - {1, 2, 3}, 3, 1)] = 1
    expected_result[(V - {1, 2, 3}, 3, 2)] = 1
    expected_result[(V - {1, 2, 4}, 1, 1)] = 2
    expected_result[(V - {1, 2, 4}, 3, 1)] = 1
    expected_result[(V - {1, 2, 4}, 3, 2)] = 1
    expected_result[(V - {1, 3, 4}, 1, 1)] = 1
    expected_result[(V - {1, 3, 4}, 3, 1)] = 2
    expected_result[(V - {1, 3, 4}, 3, 2)] = 2
    expected_result[(V - {2, 3, 4}, 1, 1)] = 1
    expected_result[(V - {2, 3, 4}, 3, 1)] = 2
    expected_result[(V - {2, 3, 4}, 3, 2)] = 2
    expected_result[(V - {1, 2, 3, 4}, 1, 1)] = 2
    expected_result[(V - {1, 2, 3, 4}, 3, 1)] = 2
    expected_result[(V - {1, 2, 3, 4}, 3, 2)] = 3

    T = algo._calc_T_table(V, W)
    assert T == expected_result
