from main import (
    can_hold_shiny_golds,
    read_bags,
    traverse_count,
)
import unittest


class TestBags(unittest.TestCase):
    """Test bag traverser.

    Run: python -m unittest test_main.py"""

    def test_part_1(self):
        """Test can_hold_shiny_golds()."""
        bags, _, _ = read_bags(path='input_test.txt')
        val = can_hold_shiny_golds(bags)
        self.assertEqual(val, 4)

    def test_part_2(self):
        """Test."""
        bags, lines, premise = read_bags(path='input_test2.txt')
        print(premise)
        val = traverse_count(bags, lines)
        self.assertEqual(val, 126)


if __name__ == '__main__':
    unittest.main()
