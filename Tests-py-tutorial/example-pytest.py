import pytest
import random
from collections.abc import Iterable


def kth_stat(iterable, k):
    assert isinstance(iterable, Iterable), "expected iterable first argument"
    return sorted(iterable)[k - 1]


def test_on_range():
    assert kth_stat(range(10), 4) == 3


def test_on_shuffled_range():
    li = list(range(10))
    random.shuffle(li)
    assert kth_stat(li, 4) == 3

