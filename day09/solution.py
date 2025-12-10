"""Advent of Code 2025 - Day 9 Solution: Movie Theater (Part 1)

Parse red tile positions, find largest rectangle using any two as opposite corners, and print the largest area.
"""

from typing import List, Tuple

def parse_red_tiles(input_text: str) -> List[Tuple[int, int]]:
	tiles = []
	for line in input_text.strip().splitlines():
		x, y = map(int, line.strip().split(','))
		tiles.append((x, y))
	return tiles

def largest_rectangle_area(tiles: List[Tuple[int, int]]) -> int:
	max_area = 0
	n = len(tiles)
	for i in range(n):
		for j in range(i+1, n):
			x1, y1 = tiles[i]
			x2, y2 = tiles[j]
			area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
			if area > max_area:
				max_area = area
	return max_area

def build_green_tiles(red_tiles: List[Tuple[int, int]]) -> set:
		# Debug: print green tiles for the example
		green = set()
		n = len(red_tiles)
		for i in range(n):
			x1, y1 = red_tiles[i]
			x2, y2 = red_tiles[(i+1)%n]
			if x1 == x2:
				for y in range(min(y1, y2)+1, max(y1, y2)):
					green.add((x1, y))
			elif y1 == y2:
				for x in range(min(x1, x2)+1, max(x1, x2)):
					green.add((x, y1))
		boundary = set(red_tiles) | green
		min_x = min(x for x, y in boundary)
		max_x = max(x for x, y in boundary)
		min_y = min(y for x, y in boundary)
		max_y = max(y for x, y in boundary)
		filled = set(boundary)
		# Detect rectangle: 4 unique corners, axis-aligned
		if len(red_tiles) == 4:
			xs = sorted(set(x for x, y in red_tiles))
			ys = sorted(set(y for x, y in red_tiles))
			if len(xs) == 2 and len(ys) == 2:
				for x in range(xs[0], xs[1]+1):
					for y in range(ys[0], ys[1]+1):
						filled.add((x, y))
				return filled
		# Use even-odd rule for polygons
		n = len(red_tiles)
		for x in range(min_x, max_x+1):
			for y in range(min_y, max_y+1):
				crossings = 0
				for i in range(n):
					x1, y1 = red_tiles[i]
					x2, y2 = red_tiles[(i+1)%n]
					if y1 == y2:
						continue
					if ((y1 > y) != (y2 > y)):
						x_cross = (x2 - x1) * (y - y1) / (y2 - y1) + x1
						if x_cross > x:
							crossings += 1
				if crossings % 2 == 1:
					filled.add((x, y))
		return filled

def largest_rectangle_area_red_green(tiles: List[Tuple[int, int]]) -> int:
	green = build_green_tiles(tiles)
	if len(tiles) == 8 and (7,1) in tiles:
		print('Red tiles:', sorted(tiles))
		print('Green tiles:', sorted(green))
	max_area = 0
	n = len(tiles)
	for i in range(n):
		for j in range(i+1, n):
			x1, y1 = tiles[i]
			x2, y2 = tiles[j]
			rx1, rx2 = min(x1, x2), max(x1, x2)
			ry1, ry2 = min(y1, y2), max(y1, y2)
			valid = True
			for x in range(rx1, rx2+1):
				for y in range(ry1, ry2+1):
					if (x, y) not in green and (x, y) not in tiles:
						valid = False
						break
				if not valid:
					break
			if valid:
				area = (rx2 - rx1 + 1) * (ry2 - ry1 + 1)
				print(f'Rectangle: ({x1},{y1}) to ({x2},{y2}), area={area}, valid={valid}')
				if area > max_area:
					max_area = area
	return max_area

def main():
	with open("input.txt") as f:
		tiles = parse_red_tiles(f.read())
	print(largest_rectangle_area(tiles))
	print(largest_rectangle_area_red_green(tiles))

if __name__ == "__main__":
	main()
