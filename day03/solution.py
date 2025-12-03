"""Advent of Code 2025 - Day 3 Solution"""

from typing import List


def max_joltage_for_bank(bank: str) -> int:
    """
    Given a string of digits representing a bank of batteries, return the largest two-digit number
    that can be formed by selecting any two batteries (digits) in order (not rearranged).
    """
    max_joltage = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            pair = int(bank[i] + bank[j])
            if pair > max_joltage:
                max_joltage = pair
    return max_joltage


def total_max_joltage(banks: List[str]) -> int:
    """
    Given a list of battery banks, return the sum of the largest possible joltage from each bank.
    """
    return sum(max_joltage_for_bank(bank) for bank in banks)


def parse_input(input_text: str) -> List[str]:
    """
    Parse the input text into a list of battery banks (strings of digits).
    """
    return [line.strip() for line in input_text.strip().splitlines() if line.strip()]


if __name__ == "__main__":
    with open("input.txt") as f:
        banks = parse_input(f.read())
    print(total_max_joltage(banks))
