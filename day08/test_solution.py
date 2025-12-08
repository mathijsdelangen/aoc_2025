"""Tests for Advent of Code 2025 - Day 8 Solution (Part 1)

Covers parsing, closest pair finding, and circuit size calculation for the example in puzzle-1.txt.
"""

import pytest
from solution import parse_positions, find_closest_pairs, DSU

EXAMPLE = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

def test_parse_positions():
	positions = parse_positions(EXAMPLE)
	assert positions[0] == (162,817,812)
	assert positions[-1] == (425,690,689)
	assert len(positions) == 20

def test_find_closest_pairs():
	positions = parse_positions(EXAMPLE)
	pairs = find_closest_pairs(positions, 10)
	assert len(pairs) == 10
	# Check that the closest pair is (0,19) as in the example
	assert (0,19) in pairs or (19,0) in pairs

def test_circuit_sizes():
	positions = parse_positions(EXAMPLE)
	pairs = find_closest_pairs(positions, 10)
	dsu = DSU(len(positions))
	for i, j in pairs:
		dsu.union(i, j)
	sizes = sorted(dsu.get_sizes(), reverse=True)
	assert sizes[:3] == [5,4,2]
	assert sizes[0] * sizes[1] * sizes[2] == 40

def test_last_pair_product():
	positions = parse_positions(EXAMPLE)
	n = len(positions)
	all_pairs = []
	from solution import euclidean, DSU
	for i in range(n):
		for j in range(i+1, n):
			dist = euclidean(positions[i], positions[j])
			all_pairs.append((dist, i, j))
	all_pairs.sort()
	dsu = DSU(n)
	last_i, last_j = None, None
	for _, i, j in all_pairs:
		if dsu.find(i) != dsu.find(j):
			dsu.union(i, j)
			last_i, last_j = i, j
			if len(set(dsu.find(x) for x in range(n))) == 1:
				break
	assert positions[last_i][0] * positions[last_j][0] == 25272
