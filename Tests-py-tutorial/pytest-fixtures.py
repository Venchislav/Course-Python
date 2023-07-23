import json
import random
import tempfile
from collections.abc import Iterable
import pytest


def kth_stat(iterable, k):
    assert isinstance(iterable, Iterable), "expected iterable first argument"
    return sorted(iterable)[k - 1]


@pytest.fixture
def filled_file():
    with tempfile.TemporaryFile(mode='w+') as f:
        li = list(range(10000))
        random.shuffle(li)
        json.dump(li, f)
        f.seek(0)
        yield f


def test_on_large_seq_from_file(filled_file):
    assert kth_stat(json.load(filled_file), 300) == 299
