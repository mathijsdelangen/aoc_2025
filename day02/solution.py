"""Advent of Code 2025 - Day 2 Solution

Find all invalid product IDs in the given ranges. An invalid ID is a number that consists of a sequence of digits repeated twice (e.g., 55, 6464, 123123).
"""

def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def is_invalid_id_part2(n: int) -> bool:
    s = str(n)
    l = len(s)
    # Try all possible chunk sizes from 1 up to half the length
    for size in range(1, l // 2 + 1):
        if l % size != 0:
            continue
        chunk = s[:size]
        if chunk * (l // size) == s:
            return True
    return False


def parse_ranges(line: str):
    for part in line.strip().split(","):
        if not part:
            continue
        start, end = map(int, part.split("-"))
        yield start, end


def solve_part1(input_line: str) -> int:
    total = 0
    for start, end in parse_ranges(input_line):
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total


def solve_part2(input_line: str) -> int:
    total = 0
    for start, end in parse_ranges(input_line):
        for n in range(start, end + 1):
            if is_invalid_id_part2(n):
                total += n
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input_line = f.read().strip()
    print("Part 1:", solve_part1(input_line))
    print("Part 2:", solve_part2(input_line))