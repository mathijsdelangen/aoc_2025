"""
Advent of Code 2025 - Day 1 Solution

Implement your solution in clear, well-commented functions.
Adapt code for part 2 as needed.
"""


# Solution for part 1
def solve_part1(input_data: str) -> int:
    """Simulate the dial and count how many times it points at 0 after a rotation."""
    position = 50
    count_zero = 0
    for line in input_data.strip().splitlines():
        if not line:
            continue
        direction = line[0]
        value = int(line[1:])
        if direction == 'L':
            position = (position - value) % 100
        elif direction == 'R':
            position = (position + value) % 100
        else:
            raise ValueError(f"Invalid direction: {direction}")
        if position == 0:
            count_zero += 1
    return count_zero

# Example function for part 2
def solve_part2(input_data: str) -> int:
    """Count all times the dial points at 0 during any rotation, including during the movement."""
    position = 50
    count_zero = 0
    for line in input_data.strip().splitlines():
        if not line:
            continue
        direction = line[0]
        value = int(line[1:])
        if direction == 'L':
            for i in range(1, value + 1):
                pos = (position - i) % 100
                if pos == 0:
                    count_zero += 1
            position = (position - value) % 100
        elif direction == 'R':
            for i in range(1, value + 1):
                pos = (position + i) % 100
                if pos == 0:
                    count_zero += 1
            position = (position + value) % 100
        else:
            raise ValueError(f"Invalid direction: {direction}")
    return count_zero
if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))
