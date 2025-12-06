"""Advent of Code 2025 - Day 6 Solution"""

from typing import List
import operator
import re


def parse_worksheet(input_text: str) -> List[str]:
    """
    Parse the worksheet into a list of rows (strings).
    """
    return [line.rstrip('\n') for line in input_text.strip().splitlines() if line.strip()]


def extract_problems(rows: List[str]) -> List[List[str]]:
    """
    Group contiguous non-space columns as problems.
    Returns a list of problems, each as a list of columns (strings).
    """
    max_len = max(len(row) for row in rows)
    padded = [row.ljust(max_len) for row in rows]
    problems = []
    col = 0
    while col < max_len:
        # Find start of next problem (first non-space column)
        while col < max_len and all(row[col] == ' ' for row in padded):
            col += 1
        if col >= max_len:
            break
        start = col
        # Find end of problem (next all-space column or end)
        while col < max_len and not all(row[col] == ' ' for row in padded):
            col += 1
        end = col
        # Extract columns for this problem
        problem = [row[start:end] for row in padded]
        problems.append(problem)
    return problems


def solve_problem(problem: List[str]) -> int:
    """
    Given a problem (list of rows, each a string slice), extract numbers and operation, then solve (part 1).
    """
    op_row = problem[-1]
    op_char = next((c for c in op_row if c in '+*'), None)
    op = operator.add if op_char == '+' else operator.mul
    numbers = []
    for row in problem[:-1]:
        for match in re.finditer(r'\d+', row):
            numbers.append(int(match.group()))
    from functools import reduce
    return reduce(op, numbers)


def solve_problem_right_to_left(problem: List[str]) -> int:
    """
    For part 2: read numbers right-to-left, each column is a digit (top = most significant, bottom = least significant).
    """
    op_row = problem[-1]
    op_char = next((c for c in op_row if c in '+*'), None)
    op = operator.add if op_char == '+' else operator.mul
    num_rows = len(problem) - 1  # exclude operator row
    num_cols = len(problem[0])
    numbers = []
    for col_idx in range(num_cols):
        digits = [problem[row_idx][col_idx] for row_idx in range(num_rows)]
        num_str = ''.join(d for d in digits if d.isdigit())
        if num_str:
            numbers.append(int(num_str))
    from functools import reduce
    return reduce(op, numbers)


def grand_total(input_text: str) -> int:
    rows = parse_worksheet(input_text)
    problems = extract_problems(rows)
    return sum(solve_problem(p) for p in problems)


def grand_total_right_to_left(input_text: str) -> int:
    rows = parse_worksheet(input_text)
    problems = extract_problems(rows)
    return sum(solve_problem_right_to_left(p) for p in problems)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_text = f.read()
    print("Part 1:", grand_total(input_text))
    print("Part 2:", grand_total_right_to_left(input_text))
