"""Advent of Code 2025 - Day 4 Solution"""

from typing import List, Tuple


def parse_input(input_text: str) -> List[List[str]]:
    """
    Parse the input text into a grid of characters.
    """
    return [list(line.strip()) for line in input_text.strip().splitlines() if line.strip()]


def count_accessible_rolls(grid: List[List[str]]) -> int:
    """
    Count the number of '@' rolls that have fewer than four '@' neighbors in the 8 adjacent cells.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neighbors += 1
            if neighbors < 4:
                accessible += 1
    return accessible


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = parse_input(f.read())
    print(count_accessible_rolls(grid))
