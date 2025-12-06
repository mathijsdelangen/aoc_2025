"""Tests for Advent of Code 2025 - Day 6 Solution"""

import pytest
from solution import parse_worksheet, extract_problems, solve_problem, grand_total, solve_problem_right_to_left, grand_total_right_to_left

EXAMPLE = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def test_parse_worksheet():
    rows = parse_worksheet(EXAMPLE)
    assert len(rows) == 4
    assert rows[0].startswith("123")
    assert rows[-1].strip().endswith("+")

def test_extract_problems():
    rows = parse_worksheet(EXAMPLE)
    problems = extract_problems(rows)
    assert len(problems) == 4
    # Check first problem's operation
    op_char = next((c for c in problems[0][-1] if c in '+*'), None)
    assert op_char == '*'
    # Check second problem's operation
    op_char2 = next((c for c in problems[1][-1] if c in '+*'), None)
    assert op_char2 == '+'

def test_solve_problem():
    rows = parse_worksheet(EXAMPLE)
    problems = extract_problems(rows)
    assert solve_problem(problems[0]) == 33210
    assert solve_problem(problems[1]) == 490
    assert solve_problem(problems[2]) == 4243455
    assert solve_problem(problems[3]) == 401

def test_grand_total():
    assert grand_total(EXAMPLE) == 4277556

# Part 2 tests

def test_solve_problem_right_to_left():
    rows = parse_worksheet(EXAMPLE)
    problems = extract_problems(rows)
    # Example answers from puzzle-2.txt
    # Leftmost: 8544, then 625, 3253600, 1058 (rightmost)
    assert solve_problem_right_to_left(problems[0]) == 8544
    assert solve_problem_right_to_left(problems[1]) == 625
    assert solve_problem_right_to_left(problems[2]) == 3253600
    assert solve_problem_right_to_left(problems[3]) == 1058


def test_grand_total_right_to_left():
    assert grand_total_right_to_left(EXAMPLE) == 3263827
