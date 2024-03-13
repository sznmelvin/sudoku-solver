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

def print_grid(grid: list[list[int]]) -> None:
    # Print the grid in a more readable format."""

    for row in grid:
        for cell in row:
            print(f"{cell:02d} " if cell > 0 else "__ ", end="")
        print()

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

# Example usage:
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
