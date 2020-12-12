from main import (
    count_answers,
    read_group_answers,
)
import unittest


class TestAnswerParser(unittest.TestCase):
    """Test answer parser.

    Run: python -m unittest test_main.py"""

    def setUp(self):
        """Read test data for test cases."""
        self.group_answers = read_group_answers(path='input_test.txt')

    def test_group_answer_reader(self):
        """Test read_group_answers()."""
        self.assertEqual(len(self.group_answers), 5)

    def test_answer_counter(self):
        """Test count_answers()."""
        unique_answer_count, same_answer_count = count_answers(self.group_answers)
        self.assertEqual(unique_answer_count, 11)
        self.assertEqual(same_answer_count, 6)


if __name__ == '__main__':
    unittest.main()
