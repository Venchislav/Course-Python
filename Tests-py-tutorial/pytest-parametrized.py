import pytest
from collections.abc import Iterable


def kth_stat(iterable, k):
    assert isinstance(iterable, Iterable), "expected iterable first argument"
    return sorted(iterable)[k - 1]


@pytest.mark.parametrize(
    ('values', 'stat_order', 'expected'), [
        ([1, ], 1, 1),
        ([1, 1, 1, 1, 1], 4, 1),
        (range(100), 4, 3)
    ]
)
def test_on_range(values, stat_order, expected):
    assert kth_stat(values, stat_order) == expected

# useful tools(decorators)
# pytest.raises(AssertionError) etc. means that we wait for AssertionError, so test will be passed if we get it
# -----------
# pytest.mark.xfail() - gives us an ability to pass test even if it doesn't work (we can use it when something useless or not important doesn't work, and we don't need to fix it)
# xfail also has arg strict=True. Test will be passed if we get an error and won't if we don't get it
# -----------
# pytest.mark.skipif() - test won't be started under certain conditions. For example if we have test for .exe file opening we don't need to start such a test if user have macOS platform (strange example, but yeah)
