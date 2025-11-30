# Advent of Code 2025 - Copilot Agent Mode

This repository is set up to solve Advent of Code 2025 puzzles using Copilot agent mode and Python.

## Structure
- Each day has its own folder: `day01`, `day02`, ..., `day12`.
- Each puzzle for a day is described in `puzzle-X.txt` (where X is the puzzle number).
- The real input for each puzzle is in `input.txt`.
- Solutions go in `solution.py`.
- Tests for examples go in `test_solution.py`.

## Usage
1. Copy the puzzle description and example(s) into `puzzle-X.txt`.
2. Copy your input into `input.txt`.
3. Implement your solution in `solution.py`.
4. Use the example(s) from `puzzle-X.txt` to write tests in `test_solution.py`.
5. Run tests to verify your solution before using the real input.

## Agent Instructions
- Read all `puzzle-X.txt` files in order for the day.
- Use the examples for testing.
- Write clear, modular, and well-commented code.
- Make it easy to adapt code for part 2 or further changes.
- Commit with clear messages.

## Tweaking Agent Behavior
- Edit `.github/copilot-instructions.md` to change agent instructions.
- Keep instructions concise and focused on best practices.
