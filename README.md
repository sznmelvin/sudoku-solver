# Sudoku Solver

This Python script implements a Sudoku solver using a recursive backtracking algorithm. It can solve any valid 9x9 Sudoku puzzle.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Breakdown](#code-breakdown)
- [Example](#example)
- 
## Features

- Solves 9x9 Sudoku puzzles
- Uses a recursive backtracking algorithm
- Prints the Sudoku grid in a readable format
- Validates moves before placing numbers

## Requirements

- Python 3.x

## Usage

1. Copy the Sudoku solver code into a file named `sudoku_solver.py`.
2. Run the script from the command line:

```bash
python sudoku_solver.py
```

3. The script will solve the example Sudoku puzzle provided in the code. To solve a different puzzle, modify the `grid` variable in the script with your own Sudoku puzzle.

## How It Works

The Sudoku solver uses a recursive backtracking algorithm to find the solution:

1. Find an empty cell in the grid.
2. Try placing numbers 1-9 in the empty cell.
3. Check if the placed number is valid according to Sudoku rules.
4. If the number is valid, recursively attempt to fill the rest of the grid.
5. If the recursive call is successful, the puzzle is solved.
6. If the recursive call fails, backtrack and try the next number.

## Code Breakdown

Let's break down the main components of the code:

### Validity Checking

```python
def is_valid_move(grid: list[list[int]], row: int, col: int, number: int) -> bool:
    # Check if a given number can be placed at a given position in the grid.
    for x in range(9):
        if grid[row][x] == number:
            return False
    for x in range(9):
        if grid[x][col] == number:
            return False
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True
```

This function checks if it's valid to place a number in a specific cell. It checks the row, column, and 3x3 square to ensure the number doesn't already exist in any of them.

### Grid Printing

```python
def print_grid(grid: list[list[int]]) -> None:
    # Print the grid in a more readable format.
    for row in grid:
        for cell in row:
            print(f"{cell:02d} " if cell > 0 else "__ ", end="")
        print()
```

This function prints the Sudoku grid in a readable format, using "\_\_" for empty cells and two-digit formatting for numbers.

### Sudoku Solving

```python
def solve_sudoku(grid: list[list[int]]) -> bool:
    # Solve the given Sudoku grid using a recursive backtracking algorithm.
    def find_next_empty() -> tuple[int, int]:
        # Find the next empty cell in the grid.
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    return row, col
        return -1, -1

    row, col = find_next_empty()
    if row == -1:
        return True
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
        grid[row][col] = 0
    return False
```

This is the main solving function. It uses recursion and backtracking to solve the Sudoku puzzle:
1. Find the next empty cell.
2. If no empty cell is found, the puzzle is solved.
3. Try numbers 1-9 in the empty cell.
4. If a number is valid, place it and recursively try to solve the rest of the puzzle.
5. If the recursive call fails, backtrack by setting the cell back to 0 and try the next number.

## Example

The script includes an example Sudoku puzzle:

```python
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

print_grid(grid)
if solve_sudoku(grid):
    print("Sudoku solved!")
    print_grid(grid)
else:
    print("Could not solve the Sudoku grid.")
```

This example demonstrates how to use the Sudoku solver. It prints the initial grid, attempts to solve it, and then prints the solution if successful.
