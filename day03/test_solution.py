"""Tests for Advent of Code 2025 - Day 3 Solution"""

import pytest
from solution import max_joltage_for_bank, total_max_joltage, parse_input, max_joltage_12_for_bank, total_max_joltage_12


def test_max_joltage_for_bank():
    assert max_joltage_for_bank("987654321111111") == 98
    assert max_joltage_for_bank("811111111111119") == 89
    assert max_joltage_for_bank("234234234234278") == 78
    assert max_joltage_for_bank("818181911112111") == 92


def test_total_max_joltage():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert total_max_joltage(banks) == 357


def test_max_joltage_12_for_bank():
    assert max_joltage_12_for_bank("987654321111111") == 987654321111
    assert max_joltage_12_for_bank("811111111111119") == 811111111119
    assert max_joltage_12_for_bank("234234234234278") == 434234234278
    assert max_joltage_12_for_bank("818181911112111") == 888911112111


def test_total_max_joltage_12():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert total_max_joltage_12(banks) == 3121910778619


def test_parse_input():
    input_text = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    assert parse_input(input_text) == [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
