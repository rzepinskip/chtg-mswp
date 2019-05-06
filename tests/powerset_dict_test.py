import pytest

from mswp.algo import powerset_dict
from orderedset import OrderedSet


def test_powerset_dict_basic():
    ps = powerset_dict([1, 2, 3])
    assert ps[frozenset([1])] == OrderedSet([frozenset({1}), frozenset()])
    assert ps[frozenset([1, 2])] == OrderedSet(
        [frozenset({1, 2}), frozenset({1}), frozenset({2}), frozenset()]
    )
    assert ps[frozenset([1, 2, 3])] == OrderedSet(
        [
            frozenset({1, 2, 3}),
            frozenset({1, 2}),
            frozenset({1, 3}),
            frozenset({2, 3}),
            frozenset({1}),
            frozenset({2}),
            frozenset({3}),
            frozenset(),
        ]
    )

