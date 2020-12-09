from main import (
    find_hax,
    find_outlier,
    read_nums,
)
import unittest


class TestHaxxer(unittest.TestCase):
    """Run: python -m unittest test_main.py"""

    def setUp(self):
        self.nums = read_nums(path='input_test.txt')

    def test_part_1(self):
        """Test find_outlier() and match against expected value."""
        outlier = find_outlier(self.nums, preamble=5)
        self.assertEqual(outlier, 127)

    def test_part_2(self):
        """Test find_hax() and match against expected sum of min and max values."""
        outlier = find_outlier(self.nums, preamble=5)
        min, max = find_hax(self.nums, outlier=outlier)
        self.assertEqual(min, 15)
        self.assertEqual(max, 47)
        self.assertEqual((min+max), 62)


if __name__ == '__main__':
    unittest.main()
