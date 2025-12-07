"""Tests for Advent of Code 2025 - Day 7 Solution (Part 1)

Covers parsing, beam simulation, and split counting for the example in puzzle-1.txt.
"""

import pytest
from solution import parse_grid, count_splits

import sys
sys.setrecursionlimit(10000)

EXAMPLE = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

def test_parse_grid():
	grid, start = parse_grid(EXAMPLE)
	assert grid[start[0]][start[1]] == 'S'
	assert start == (0, 7)
	assert grid[2][7] == '^'

def test_count_splits_example():
	grid, start = parse_grid(EXAMPLE)
	print('Start:', start)
	for row in grid:
		print(''.join(row))
	result = count_splits(grid, start)
	print('Splits:', result)
	assert result == 21


def test_count_timelines_example():
	from solution import count_timelines
	grid, start = parse_grid(EXAMPLE)
	result, ends = count_timelines(grid, start, debug=True)
	print('Timelines:', result)
	print('End positions:', sorted(ends))
	assert result == 40
