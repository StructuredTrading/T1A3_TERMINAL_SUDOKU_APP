import random

def load_game():
    pass

def submit_details():
    pass



def solve_sudoku(grid):
    """
    Solve a Sudoku puzzle using a backtracking algorithm.

    Parameters:
    - grid (list): A 9x9 Sudoku grid represented as a list of lists.
      Empty cells are denoted by 0.

    Returns:
    - bool: True if a solution is found, False otherwise.

    The function employs a recursive backtracking algorithm to solve a given Sudoku puzzle.
    It iterates through each cell in the grid, attempting to fill in missing numbers.
    For each empty cell, it tries different numbers and recursively explores potential solutions.
    If a valid number is found for a cell, the function proceeds to solve the remaining puzzle.
    If a solution is not found, it backtracks and tries a different number, repeating the process.
    """
    for _row in range(9):
        for _col in range(9):
            if grid[_row][_col] == 0:
                for num in range(1, 10):
                    if(is_valid_move(grid, _row, _col, num)):
                        grid[_row][_col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[_row][_col] = 0
                return False
    return True


# Generates a sudoku grid and returns it
def generate_grid():
    """
    creates a random sudoku grid in a formatted way.

    Parameters:
    - board (list): The 9x9 Sudoku board represented as a list of lists.

    Returns:
    list[list[int]]
    """

    # Creates a 9 X 9 list of lists
    grid = [[0] * 9 for _ in range(9)]
    print(f"Base = {grid}\n\n")
    solve_sudoku(grid)

    puzzle = [row[:] for row in grid]
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle

