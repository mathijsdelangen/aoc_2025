"""Advent of Code 2025 - Day 5 Solution"""

from typing import List, Tuple


def parse_input(input_text: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    """
    Parse the input into a list of (start, end) ranges and a list of available IDs.
    """
    ranges = []
    ids = []
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    i = 0
    # Parse ranges
    while i < len(lines) and '-' in lines[i]:
        start, end = map(int, lines[i].split('-'))
        ranges.append((start, end))
        i += 1
    # Skip blank line
    while i < len(lines) and '-' not in lines[i]:
        if lines[i].isdigit():
            ids.append(int(lines[i]))
        i += 1
    # Parse remaining IDs
    for line in lines[i:]:
        if line.isdigit():
            ids.append(int(line))
    return ranges, ids


def is_fresh(ingredient_id: int, ranges: List[Tuple[int, int]]) -> bool:
    """
    Return True if the ingredient_id is in any of the fresh ranges.
    """
    return any(start <= ingredient_id <= end for start, end in ranges)


def count_fresh_ids(ranges: List[Tuple[int, int]], ids: List[int]) -> int:
    """
    Count how many of the available ingredient IDs are fresh.
    """
    return sum(1 for id_ in ids if is_fresh(id_, ranges))


def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping or adjacent ranges and return the merged list.
    """
    if not ranges:
        return []
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def count_total_fresh_ids(ranges: List[Tuple[int, int]]) -> int:
    """
    Count the total number of unique ingredient IDs considered fresh by the union of all ranges.
    """
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)


if __name__ == "__main__":
    with open("input.txt") as f:
        ranges, ids = parse_input(f.read())
    print("Part 1:", count_fresh_ids(ranges, ids))
    print("Part 2:", count_total_fresh_ids(ranges))
