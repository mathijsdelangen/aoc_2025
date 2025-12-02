# Copilot Agent Instructions for Advent of Code 2025

This repository is structured for solving Advent of Code puzzles using Copilot agent mode. Please follow these guidelines:

- Each day (day01 to day12) has its own subfolder.
- Each puzzle for a day is described in `puzzle-X.txt` (where X is the puzzle number, e.g., 1, 2, ...).
- The real input for each puzzle is in `input.txt`.
- Use the example in `puzzle-X.txt` to verify your solution before using the real input.
- Write clear, well-commented Python code with functions for each part.
- Structure code so it is easy to adapt for part 2 or further changes.
- Commit with clear, descriptive messages.
- To add or tweak agent instructions, edit this file or the README as needed.

## Example Structure for a Day

```
day01/
  puzzle-1.txt
  puzzle-2.txt
  input.txt
  solution.py
  test_solution.py
```


## Agent Best Practices

- **Do not add or track Advent of Code puzzle descriptions or input files in the repository.** These files should remain local and are excluded by `.gitignore`.
- Always read all `puzzle-X.txt` files in order for the day (if present locally).
- Use the provided example(s) for testing before running on `input.txt`.
- Keep code modular and easy to update for part 2.
- Use clear, descriptive, and consistent function and variable names (snake_case for Python).
- Add comments explaining logic and edge cases, but avoid redundant comments.
- Make it easy to add new instructions or change agent behavior by editing this file.
- **File and Code Structure:**
  - Place a module-level docstring or comment at the very top of each file, before imports.
  - Group imports: standard library, then third-party, then local imports, with a blank line between groups.
  - Remove all unused imports and variables.
  - Ensure exactly one blank line after imports, and two blank lines before each top-level function or class.
  - Group helper functions before main solution functions.
  - No extra blank lines at the top or bottom of files.
  - No trailing whitespace or tabs (use 4 spaces for indentation).
  - No print/debug statements in solution files unless required for output.
  - Only include `if __name__ == "__main__":` in solution files, not in test files.
  - Test files should only import what is needed and use clear, consistent test naming.
  - Each test file should have a header comment explaining what is being tested.
  - Use `unittest` or `pytest` style consistently in test files.
  - No unnecessary code (e.g., commented-out code, unused variables).
  - Review all code for consistency in style, whitespace, and structure before finalizing.


## Additional Agent Best Practices

- **Clarify Puzzle Logic Interpretation:**
  - When implementing logic based on a puzzle description, always clarify edge cases and provide explicit examples in the instructions or tests. If the description is ambiguous, prompt the user for clarification before proceeding.

- **Test-Driven Development:**
  - Always write or update tests for helper functions and edge cases before implementing or refactoring logic. Use the provided examples to create comprehensive tests.

- **Error Handling and Feedback:**
  - If a test fails, analyze the failure and suggest possible causes or clarifications before making further changes. Avoid making multiple speculative changes in a row.

- **PowerShell Command Chaining:**
  - When running multiple git or shell commands, use PowerShell-compatible syntax (`;` instead of `&&`) to avoid errors.

- **Explicitly Confirm Requirements:**
  - If a requirement or expected behavior is unclear (e.g., what counts as an invalid ID), ask the user for confirmation before proceeding.

- **Patch and Test Cycle:**
  - After each code change, always run the relevant tests and only proceed if all tests pass.