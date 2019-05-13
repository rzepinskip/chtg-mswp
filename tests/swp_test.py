import pytest

import networkx as nx
from mswp.algo import MSWPAlgo

testdata = [
    (2, 2 * ((2 ** 4 + 1) ** 6)),
    (3, 6 * ((3 ** 4 + 1) ** 5 + 2 * (3 ** 4 + 1) ** 7))
]


@pytest.mark.parametrize("k,expected_result", testdata)
def test_swp_basic(k, expected_result):
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
    assert algo._swp(V, k, W) == expected_result
