"""Tests for Advent of Code 2025 - Day 5 Solution"""

import pytest
from solution import parse_input, is_fresh, count_fresh_ids, merge_ranges, count_total_fresh_ids

EXAMPLE = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def test_parse_input():
    ranges, ids = parse_input(EXAMPLE)
    assert ranges == [(3, 5), (10, 14), (16, 20), (12, 18)]
    assert ids == [1, 5, 8, 11, 17, 32]

def test_is_fresh():
    ranges, ids = parse_input(EXAMPLE)
    assert not is_fresh(1, ranges)
    assert is_fresh(5, ranges)
    assert not is_fresh(8, ranges)
    assert is_fresh(11, ranges)
    assert is_fresh(17, ranges)
    assert not is_fresh(32, ranges)

def test_count_fresh_ids():
    ranges, ids = parse_input(EXAMPLE)
    assert count_fresh_ids(ranges, ids) == 3

def test_merge_ranges():
    ranges, _ = parse_input(EXAMPLE)
    merged = merge_ranges(ranges)
    assert merged == [(3, 5), (10, 20)]

def test_count_total_fresh_ids():
    ranges, _ = parse_input(EXAMPLE)
    assert count_total_fresh_ids(ranges) == 14
