import pytest

import networkx as nx
from mswp.algo import reconstruct_coloring

G1 = nx.Graph()
G1.add_nodes_from(
    [(1, dict(weight=1)), (2, dict(weight=1)), (3, dict(weight=3)), (4, dict(weight=3))]
)
G1.add_edges_from([(1, 2), (1, 4), (2, 3)])

G2 = nx.Graph()
G2.add_nodes_from(
    [
        (1, dict(weight=1)),
        (2, dict(weight=1)),
        (3, dict(weight=3)),
        (4, dict(weight=3)),
        (5, dict(weight=7)),
        (6, dict(weight=7)),
    ]
)
G2.add_edges_from([(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4)])

testdata = [(G1, {1: 2, 2: 3, 3: 1, 4: 1}), (G2, {5: 1, 6: 1, 1: 2, 3: 2, 2: 3, 4: 3})]


@pytest.mark.parametrize("G,expected_result", testdata)
def test_swp_basic(G, expected_result):
    coloring = reconstruct_coloring(G)
    assert coloring == expected_result
