"""
Tests for Advent of Code 2025 - Day 2 Solution
"""
import unittest
from solution import solve_part1, is_invalid_id, solve_part2, is_invalid_id_part2

class TestDay02(unittest.TestCase):
    def test_is_invalid_id_part2(self):
        self.assertTrue(is_invalid_id_part2(11))
        self.assertTrue(is_invalid_id_part2(22))
        self.assertTrue(is_invalid_id_part2(99))
        self.assertTrue(is_invalid_id_part2(6464))
        self.assertTrue(is_invalid_id_part2(123123))
        self.assertTrue(is_invalid_id_part2(1212))
        self.assertTrue(is_invalid_id_part2(12341234))
        self.assertTrue(is_invalid_id_part2(123123123))
        self.assertTrue(is_invalid_id_part2(1212121212))
        self.assertTrue(is_invalid_id_part2(1111111))
        self.assertFalse(is_invalid_id_part2(101))
        self.assertFalse(is_invalid_id_part2(1234))
        self.assertFalse(is_invalid_id_part2(12345))
        self.assertFalse(is_invalid_id_part2(123456))
    def test_is_invalid_id(self):
        self.assertTrue(is_invalid_id(11))
        self.assertTrue(is_invalid_id(22))
        self.assertTrue(is_invalid_id(99))
        self.assertTrue(is_invalid_id(6464))
        self.assertTrue(is_invalid_id(123123))
        self.assertFalse(is_invalid_id(101))
        self.assertFalse(is_invalid_id(1234))
        self.assertFalse(is_invalid_id(12345))
        self.assertFalse(is_invalid_id(123456))
        self.assertTrue(is_invalid_id(1212))

    def test_example(self):
        example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        # From the puzzle description, the sum should be 1227775554
        self.assertEqual(solve_part1(example), 1227775554)

    def test_example_part2(self):
        example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        # From the puzzle description, the sum should be 4174379265
        self.assertEqual(solve_part2(example), 4174379265)

if __name__ == "__main__":
    unittest.main()
