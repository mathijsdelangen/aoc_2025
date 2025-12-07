"""Advent of Code 2025 - Day 7 Solution: Laboratories (Part 1)

Simulate the downward-moving tachyon beam, splitting at each splitter ('^'), and count the total number of splits.
"""

from typing import List, Tuple, Set

def parse_grid(input_text: str) -> Tuple[List[List[str]], Tuple[int, int]]:
	"""Parse the grid and find the start position (S)."""
	grid = [list(line.rstrip('\n')) for line in input_text.strip().splitlines()]
	for r, row in enumerate(grid):
		for c, val in enumerate(row):
			if val == 'S':
				return grid, (r, c)
	raise ValueError("No start position 'S' found.")


def count_splits(grid: List[List[str]], start: Tuple[int, int]) -> int:
	"""
	Simulate the beam, splitting at each splitter ('^'), and count total splits.
	"""
	rows, cols = len(grid), len(grid[0])
	split_count = 0
	# Each beam is (row, col, direction), direction: 'down', 'left', 'right'
	beams = [(start[0], start[1], 'down')]
	visited: Set[Tuple[int, int, str]] = set()
	while beams:
		r, c, d = beams.pop()
		if (r, c, d) in visited:
			continue
		visited.add((r, c, d))
		# Move beam
		if d == 'down':
			nr, nc = r + 1, c
		elif d == 'left':
			nr, nc = r, c - 1
		elif d == 'right':
			nr, nc = r, c + 1
		else:
			continue
		# Out of bounds
		if not (0 <= nr < rows and 0 <= nc < cols):
			continue
		cell = grid[nr][nc]
		if cell == '.':
			beams.append((nr, nc, d))
		elif cell == '^':
			if d == 'down':
				split_count += 1
				# Emit new downward beams from immediate left and right of splitter
				if nc - 1 >= 0 and grid[nr][nc - 1] == '.':
					beams.append((nr, nc - 1, 'down'))
				if nc + 1 < cols and grid[nr][nc + 1] == '.':
					beams.append((nr, nc + 1, 'down'))
			# If beam comes from left/right, it stops at splitter
		# If cell is 'S', ignore (shouldn't happen after first step)
	return split_count
	# Uncomment for debugging:
	# print(f"Beam at ({r},{c}) dir={d}")
	# print(f"  Moves to ({nr},{nc}) cell='{cell}'")
	# print(f"  Split at ({nr},{nc}) dir={d}")


def main():
	with open("input.txt") as f:
		grid, start = parse_grid(f.read())

	print(count_splits(grid, start))
	print(count_timelines(grid, start))


def count_timelines(grid: List[List[str]], start: Tuple[int, int], debug: bool = False) -> int | tuple[int, set]:
	"""
	Part 2: Count the number of unique end positions (timelines) a particle can reach.
	Each time a splitter is encountered, the path splits left and right recursively.
	Return the number of unique end positions (bottom row or edge exits).
	If debug=True, also return the set of end positions.
	"""
	rows, cols = len(grid), len(grid[0])
	end_positions = set()

	from functools import lru_cache

	@lru_cache(maxsize=None)
	def count_paths(r: int, c: int) -> int:
		# Out of bounds: timeline ends
		if not (0 <= r < rows and 0 <= c < cols):
			return 1
		# If at bottom row, timeline ends
		if r == rows - 1:
			return 1
		cell = grid[r][c]
		if cell == '.':
			return count_paths(r + 1, c)
		elif cell == '^':
			# Split: left and right, both continue recursively
			return count_paths(r + 1, c - 1) + count_paths(r + 1, c + 1)
		elif cell == 'S':
			return count_paths(r + 1, c)
		else:
			return 1

	result = count_paths(start[0], start[1])
	if debug:
		return result, set()
	return result

if __name__ == "__main__":
	main()
