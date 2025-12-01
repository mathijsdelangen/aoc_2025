"""
Tests for Advent of Code 2025 - Day 1 Solution

Use the example(s) from puzzle-1.txt and puzzle-2.txt for tests.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from solution import solve_part1, solve_part2

class TestDay01(unittest.TestCase):
    def test_part1_example(self):
        example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
        expected = 3
        self.assertEqual(solve_part1(example_input), expected)

    def test_part2_example(self):
        example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
        expected = 6
        self.assertEqual(solve_part2(example_input), expected)

if __name__ == "__main__":
    unittest.main()
