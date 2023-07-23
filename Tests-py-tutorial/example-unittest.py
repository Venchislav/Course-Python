import unittest
import random
from collections.abc import Iterable


def kth_stat(iterable, k):

    assert isinstance(iterable, Iterable), "expected iterable first argument"
    return sorted(iterable)[k - 1]


class TestStat(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_on_range(self):
        print(list(range(10)))
        self.assertEqual(kth_stat(range(10), 4), 2)
        # assert kth_stat(range(10), 4) == 2 - it's worse as we don't ger enough useful info

    def test_on_shuffled_range(self):
        li = list(range(10))
        random.shuffle(li)
        self.assertEqual(kth_stat(li, 3), 2)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()


# unittest is not that good as standard assert doesn't work here.
# also unittest's fixtures doesn't follow PEP-8 (method name is half camel cased in here)
# and anyway, mostly it's worse than pytest, so there is no particular reason to use it

# nevertheless DISCLAIMER: I'm not a pro in testing, so I may be wrong here
