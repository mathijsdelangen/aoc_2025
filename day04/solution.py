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


def total_removed_rolls(grid: List[List[str]]) -> int:
    """
    Iteratively remove accessible rolls and count the total removed until no more can be accessed.
    Only remove rolls that are accessible at the start of each round.
    """
    from copy import deepcopy
    grid = deepcopy(grid)
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    total_removed = 0
    while True:
        to_remove = []
        # Collect all accessible rolls at the start of the round
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
                    to_remove.append((r, c))
        if not to_remove:
            break
        # Remove all collected rolls at once
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)
    return total_removed


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = parse_input(f.read())
    print("Part 1:", count_accessible_rolls(grid))
    print("Part 2:", total_removed_rolls(grid))
