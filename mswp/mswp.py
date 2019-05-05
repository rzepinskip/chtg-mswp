import networkx as nx
import itertools
from math import floor
from typing import Iterable, FrozenSet, Any, Set, Dict


def mswp(G: nx.Graph) -> int:
    n = G.number_of_nodes()
    W = max([attr["weight"] for node, attr in G.nodes.items()])
    w_min = n ** 2 * W
    for k in range(1, n + 1):
        t = swp(G, frozenset(G.nodes), k, W)
        r = k ** 2 * W
        alpha = list()
        while r >= 0:
            alpha_r = t // (k ** n + 1) ** r
            if alpha_r == 0:
                alpha.append(r)
            t = t % ((k ** n + 1) ** r)
            r = r - 1

        if len(alpha) > 0 and alpha[-1] < w_min:
            w_min = r

    return w_min


def swp(G: nx.Graph, V: FrozenSet[int], k: int, M: int):
    n = len(V)
    f_dashed = dict()
    T = calc_T_table(G, V, M)
    for X in powerset(V):
        outer = V - X
        for l in range(0, n + 1):
            f_val = 0
            for q in range(1, M + 1):
                f_val = f_val + q * T[(outer, q, l)]
            f_dashed[(l, outer)] = f_val

    g = dict()
    b = dict()
    p_val = 0
    for X in powerset(V):
        outer = V - X
        for m in range(0, n + 1):
            for c in range(1, k + 1):
                g[(c, c, m)] = f_dashed[(m, outer)]
            for t in range(1, k + 1):
                for s in range(1, t):
                    g_tmp = 0
                    for m_0 in range(0, m + 1):
                        m_1 = m - m_0
                        g_tmp = (
                            g_tmp
                            + g[(s, floor((s + t) / 2), m_0)]
                            * g[(floor((s + t) / 2) + 1, t, m_1)]
                        )
                    g[(s, t, m)] = g_tmp
        b[X] = g[(1, k, n)]
        p_val = p_val + (-1) ** len(X) * b[X]

    return p_val


def calc_T_table(G: nx.Graph, V: FrozenSet[int], M: int):
    T = dict()
    n = len(V)
    for l in range(0, n + 1):
        for q in range(1, M + 1):
            T[(V, q, l)] = 0
    for q in range(1, M + 1):
        for v in V:
            weight = G.node[v]["weight"]
            if weight == q:
                T[(V - {v}, q, 1)] = 1
            else:
                T[(V - {v}, q, 1)] = 0
    for q in range(1, M + 1):
        for X in powerset(V).difference(V):
            for l in range(n - len(X) + 1, n + 1):
                T[(X, q, l)] = 0
    for q in range(1, M + 1):
        for X in powerset(V).difference(V, frozenset()):
            for l in range(0, n - len(X) + 2):
                for v in X:
                    if G.node[v]["weight"] < q:
                        val = T[(X, q, l)] + T[(X + G.neighbors(v), q, l - 1)]
                    elif G.node[v]["weight"] == q and l > 1:
                        val = T[(X, q, l)] + T[(X + G.neighbors(v), q, l - 1)]
                    elif G.node[v]["weight"] == q and l == 1:
                        val = T[(X, q, l)] + T[(X + G.neighbors(v), q, l - 1)] + 1
                    else:
                        val = T[(X, q, l)]
                    T[(X - {v}, q, l)] = val
    return T


def powerset(l) -> FrozenSet[FrozenSet[Any]]:
    """[1, 2, 3] -> {{}, {2}, {2, 3}, {1}, {1, 2}, {3}, {1, 3}, {1, 2, 3}}"""
    result = [()]
    for i in range(len(l)):
        result += itertools.combinations(l, i + 1)
    return frozenset([frozenset(x) for x in result])
