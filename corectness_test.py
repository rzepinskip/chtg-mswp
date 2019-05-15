import networkx as nx
from mswp.algo import MSWPAlgo
from mswp.utils import draw_bipartite_graph
from itertools import combinations

def create_example_graph(vertices_count, max_weight):
    graph = nx.Graph()
    vertices = list(range(0, vertices_count))

    for i in range(0, vertices_count - 2):
        graph.add_node(i, weight=1)
    graph.add_node(vertices_count - 1, weight=max_weight)
    graph.add_node(vertices_count - 2, weight=max_weight)

    for x in [v for v in vertices if v % 2 == 0]:
        for y in [v for v in vertices if v % 2 != 0]:
            if x == vertices_count - 2 and y == vertices_count - 1:
                continue
            graph.add_edge(x, y)

    solution = max_weight + 2

    return graph, solution


def create_full_graph(vertices_count):
    graph = nx.Graph()
    vertices = list(range(0, vertices_count))

    for i in range(0, vertices_count):
        graph.add_node(i, weight=1)

    for x, y in combinations(vertices, 2):
        graph.add_edge(x, y)

    solution = vertices_count

    return graph, solution

def test_correctness():
    example_test_cases = [create_example_graph(n, w) for n in range(4, 11, 2) for w in range(3, 11)]
    full_test_cases = [create_full_graph(n) for n in range(1, 11)]
    count = 0
    passed = 0
    for graph, solution in full_test_cases:
        # draw_bipartite_graph(graph)
        algo = MSWPAlgo(graph)
        res = algo.mswp()
        print(res)
        if res == solution:
            passed += 1
        count += 1
        print('PASSED {0}/{1}'.format(passed, count))

test_correctness()