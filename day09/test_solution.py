"""
Tests for Advent of Code 2025 - Day 9 Solution

Validates:
	- Parsing of red tile input
	- Largest rectangle area (part 1)
	- Green tile filling logic for rectangles and polygons (part 2)
	- Edge cases for green tile fill

Uses pytest style throughout.
"""

from solution import parse_red_tiles, largest_rectangle_area, largest_rectangle_area_red_green, build_green_tiles

EXAMPLE = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

def test_parse_red_tiles():
	tiles = parse_red_tiles(EXAMPLE)
	assert tiles[0] == (7,1)
	assert tiles[-1] == (7,3)
	assert len(tiles) == 8

def test_largest_rectangle_area():
	tiles = parse_red_tiles(EXAMPLE)
	assert largest_rectangle_area(tiles) == 50

def test_largest_rectangle_area_red_green():
	tiles = parse_red_tiles(EXAMPLE)
	assert largest_rectangle_area_red_green(tiles) == 24

def test_green_tiles_rectangle():
	"""Green tile fill for a simple 3x3 rectangle."""
	red = [(1,1), (1,3), (3,1), (3,3)]
	green = build_green_tiles(red)
	expected = set((x, y) for x in range(1, 4) for y in range(1, 4))
	assert green == expected

def test_green_tiles_l_shape():
	"""Green tile fill for an L-shape polygon."""
	red = [(1,1), (1,3), (3,3)]
	green = build_green_tiles(red)
	assert (1,2) in green
	assert (2,3) in green
