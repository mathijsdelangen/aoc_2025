"""Tests for Advent of Code 2025 - Day 4 Solution"""

import pytest
from solution import parse_input, count_accessible_rolls, total_removed_rolls

EXAMPLE = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def test_parse_input():
    grid = parse_input(EXAMPLE)
    assert grid[0] == list("..@@.@@@@.")
    assert grid[-1] == list("@.@.@@@.@.")
    assert len(grid) == 10
    assert all(len(row) == 10 for row in grid)

def test_count_accessible_rolls():
    grid = parse_input(EXAMPLE)
    assert count_accessible_rolls(grid) == 13

def test_total_removed_rolls():
    grid = parse_input(EXAMPLE)
    assert total_removed_rolls(grid) == 43
