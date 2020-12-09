from main import (
    execute,
    permutate,
    read_instructions,
)
import unittest


class TestAnswerParser(unittest.TestCase):
    """Run: python -m unittest test_main.py"""

    def setUp(self):
        self.inst = read_instructions(path='input_test.txt')

    def test_part_1(self):
        """Test that execution is interrupted due to executing duplicate instructions, verify acc value."""
        val, terminated = execute(self.inst)
        self.assertEqual(terminated, True)
        self.assertEqual(val, 5)

    def test_part_2(self):
        """Test that execution is *not* terminated as a result of finding correct permutation, verify acc value."""
        val, terminated = permutate(self.inst)
        self.assertEqual(terminated, False)
        self.assertEqual(val, 8)


if __name__ == '__main__':
    unittest.main()
