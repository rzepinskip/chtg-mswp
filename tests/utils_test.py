import pytest

import networkx as nx
from mswp.utils import read_graph_dimacs_format


def test_read_graph_dimacs_format_basic():
    G = read_graph_dimacs_format("./tests/data/dimacs_basic.col")
    assert set(G.nodes) == set([1, 2, 3, 4, 5, 6])
    assert set(G.edges) == set(
        [(1, 2), (1, 4), (1, 6), (2, 3), (2, 5), (4, 3), (4, 5), (6, 3)]
    )


def test_read_graph_dimacs_format_full():
    G = read_graph_dimacs_format("./tests/data/dimacs_full.col")
    assert len(G.nodes) == 74
    assert len(G.edges) == 602 / 2
