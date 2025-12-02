"""Tests for Advent of Code 2025 - Day 1 Solution

Use the example(s) from puzzle-1.txt and puzzle-2.txt for tests.
"""

import unittest
from solution import solve_part1, solve_part2


class TestDay01(unittest.TestCase):
    def test_part1_example(self):
        example_input = (
            "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
        )
        expected = 3
        self.assertEqual(solve_part1(example_input), expected)

    def test_part2_example(self):
        example_input = (
            "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
        )
        expected = 6
        self.assertEqual(solve_part2(example_input), expected)


if __name__ == "__main__":
    unittest.main()