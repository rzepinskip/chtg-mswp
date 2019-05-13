import networkx as nx
import itertools
from math import floor
from typing import Iterable, FrozenSet, Any, Set, Dict, Callable
from orderedset import OrderedSet
import numpy as np


class MSWPAlgo:
    def __init__(self, G: nx.Graph):
        self.G = G
        self._powersets = powerset_dict(G.nodes)

    def mswp(self) -> int:
        n = self.G.number_of_nodes()
        W = max([attr["weight"] for node, attr in self.G.nodes.items()])
        w_min = n * W
        for k in range(1, n + 1):
            t = self._swp(
                frozenset(self.G.nodes),
                k,
                W
            )
            r = k * W
            alpha = np.empty(r + 1, dtype=int)
            while r >= 0:
                alpha[r] = t / ((k ** n + 1) ** r)
                t = t % ((k ** n + 1) ** r)
                r = r - 1
            r = 0
            while r <= k * W and alpha[r] == 0:
                r = r + 1

            if r <= k * W and r < w_min:
                w_min = r

        return w_min

    def _swp(
        self,
        V: FrozenSet[int],
        k: int,
        M: int,
    ):
        n = len(V)
        f_dashed = dict()
        T = self._calc_T_table(V, M)
        for X in self.powerset(V):
            outer = V - X
            for l in range(0, n + 1):
                f_val = 0
                for q in range(1, M + 1):
                    f_val = f_val + ((k ** n + 1) ** q) * T[(outer, q, l)]
                f_dashed[(l, X)] = f_val
        g = dict()
        b = dict()
        p_val = 0
        for X in self.powerset(V):
            outer = V - X
            for m in range(0, n + 1):
                for c in range(1, k + 1):
                    g[(c, c, m)] = f_dashed[(m, outer)]
                for t in range(1, k + 1):
                    for s in range(t - 1, 0, -1):
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
            p_val = p_val + ((-1) ** len(X)) * b[X]

        return p_val

    def _calc_T_table(
        self,
        V: FrozenSet[int],
        M: int,
    ):
        T = self._get_empty_T_table(V, M)
        n = len(V)
        for q in range(1, M + 1):
            for v in V:
                weight = self.G.node[v]["weight"]
                if weight == q:
                    T[(V - {v}, q, 1)] = 1
        for q in range(1, M + 1):
            for X in self.powerset(V).difference(OrderedSet([V, frozenset()])):
                for l in range(1, n - len(X) + 2):
                    for v in X:
                        weight = self.G.node[v]["weight"]
                        if weight < q:
                            val = (
                                T[(X, q, l)]
                                + T[(X.union(self.G.neighbors(v)), q, l - 1)]
                            )
                        elif weight == q and l > 1:
                            val = T[(X, q, l)] + sum(
                                [
                                    T[(X.union(self.G.neighbors(v)), j, l - 1)]
                                    for j in range(1, q + 1)
                                ]
                            )
                        elif weight == q and l == 1:
                            val = T[(X, q, l)] + 1
                        else:
                            val = T[(X, q, l)]
                        T[(X - {v}, q, l)] = val
        return T

    def _get_empty_T_table(self, V, W):
        T = dict()
        for X in self.powerset(V):
            for l in range(0, len(V) + 1):
                for q in range(1, W + 1):
                    T[(X, q, l)] = 0
        return T

    def powerset(self, l):
        return self._powersets[l]


def powerset_dict(seq):
    dic = dict()
    previous = frozenset()
    dic[previous] = OrderedSet([frozenset()])
    for i in seq:
        current = previous.union(set([i]))
        dic[current] = [x for x in dic[previous]]
        for existing in dic[previous]:
            dic[current].append(existing.union(set([i])))

        dic[current] = OrderedSet(sorted(dic[current], reverse=True, key=len))
        previous = current
    return dic

