import networkx as nx
import timeit
from functools import partial
from random import random, randint
from itertools import combinations
from typing import NamedTuple, List, Callable

from mswp.algo import MSWPAlgo

import matplotlib.pyplot as plt


class TestCase(NamedTuple):
    n_vertices: int
    g_density: float
    max_weight: int


def create_test_case(test_case: TestCase):
    return create_test_graph(
        test_case.n_vertices, test_case.g_density, test_case.max_weight
    )


def create_test_graph(n_vertices: int, density: float, max_weight: int):
    graph = nx.Graph()
    vertices = list(range(0, n_vertices))

    for i in range(0, n_vertices):
        graph.add_node(i, weight=randint(1, max_weight))

    for x, y in combinations(vertices, 2):
        if random() < density:
            graph.add_edge(x, y)

    return graph


def run_algo(G):
    MSWPAlgo(G).mswp()


def measure_test_cases(test_cases: List[TestCase]):
    def run_test(G):
        return MSWPAlgo(G).mswp()

    def measure_single_test_case(test_case: TestCase):
        G = create_test_case(test_case)
        return min(timeit.Timer(partial(run_algo, G)).repeat(repeat=3, number=1))

    return {test_case: measure_single_test_case(test_case) for test_case in test_cases}


def test_vertices_number():
    max_n = 10
    test_cases = [TestCase(x, 0.5, max_n) for x in range(1, max_n)]
    result = measure_test_cases(test_cases)
    fig = plt.figure()
    ax = plt.axes()

    n = [x.n_vertices for x, _ in result.items()]
    y = [duration for _, duration in result.items()]
    ax.plot(n, y)
    ax.plot(n, [x ** 2 for x in n])
    plt.show()


def test_max_weight():
    pass


test_vertices_number()
