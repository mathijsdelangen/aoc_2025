"""Advent of Code 2025 - Day 8 Solution: Playground (Part 1)

Parse junction box positions, connect 1000 closest pairs, find sizes of all circuits, and multiply the sizes of the three largest circuits.
"""

from typing import List, Tuple
import math

def parse_positions(input_text: str) -> List[Tuple[int, int, int]]:
	positions = []
	for line in input_text.strip().splitlines():
		x, y, z = map(int, line.strip().split(','))
		positions.append((x, y, z))
	return positions

def euclidean(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> float:
	return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def find_closest_pairs(positions: List[Tuple[int, int, int]], k: int) -> List[Tuple[int, int]]:
	n = len(positions)
	pairs = []
	for i in range(n):
		for j in range(i+1, n):
			dist = euclidean(positions[i], positions[j])
			pairs.append((dist, i, j))
	pairs.sort()
	return [(i, j) for _, i, j in pairs[:k]]

class DSU:
	def __init__(self, n):
		self.parent = list(range(n))
		self.size = [1]*n
	def find(self, x):
		while self.parent[x] != x:
			self.parent[x] = self.parent[self.parent[x]]
			x = self.parent[x]
		return x
	def union(self, x, y):
		xr, yr = self.find(x), self.find(y)
		if xr == yr:
			return False
		if self.size[xr] < self.size[yr]:
			xr, yr = yr, xr
		self.parent[yr] = xr
		self.size[xr] += self.size[yr]
		return True
	def get_sizes(self):
		roots = set(self.find(i) for i in range(len(self.parent)))
		return [self.size[r] for r in roots]

def main():
	with open("input.txt") as f:
		positions = parse_positions(f.read())
	n = len(positions)
	# Part 1
	pairs = find_closest_pairs(positions, 1000)
	dsu = DSU(n)
	for i, j in pairs:
		dsu.union(i, j)
	sizes = sorted(dsu.get_sizes(), reverse=True)
	print(sizes[0] * sizes[1] * sizes[2])

	# Part 2
	# Connect pairs until all boxes are in one circuit
	all_pairs = []
	for i in range(n):
		for j in range(i+1, n):
			dist = euclidean(positions[i], positions[j])
			all_pairs.append((dist, i, j))
	all_pairs.sort()
	dsu2 = DSU(n)
	last_i, last_j = None, None
	for _, i, j in all_pairs:
		if dsu2.find(i) != dsu2.find(j):
			dsu2.union(i, j)
			last_i, last_j = i, j
			# Check if all are connected
			if len(set(dsu2.find(x) for x in range(n))) == 1:
				break
	print(positions[last_i][0] * positions[last_j][0])

if __name__ == "__main__":
	main()
