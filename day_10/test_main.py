from main import (
    read_adapters,
    find_adapters,
    options,
)
import unittest


class TestAdapters(unittest.TestCase):
    """Run: python -m unittest test_main.py"""

    def setUp(self):
        self.adapters = read_adapters(path='input_test.txt')

    def test_part_1(self):
        res = find_adapters(self.adapters)
        self.assertEqual((len(res[1])+len(res[3])), 12)
        self.assertEqual(len(res[1]), 7)
        self.assertEqual(len(res[3]), 5)

    def test_part_2(self):
        adapters = self.adapters
        adapters.append(max(adapters)+3)
        opts = options(adapters, i=0, hits=([1]*len(adapters)))
        self.assertEqual(opts, 8)


if __name__ == '__main__':
    unittest.main()
