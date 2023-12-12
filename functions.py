import random
from colorama import Fore, Back


def display_grid(grid):
    grid_text = Fore.BLACK
    grid_background = Back.WHITE
    print(f"{grid_background}     1 2 3   4 5 6   7 8 9 {Back.RESET}")
    print(f"{grid_background}   +----------------------+{Back.RESET}")
    for row in range(9):
        print(f"{grid_background}{row + 1}  | ", end="")
        for col in range(9):
            if(grid[row][col] == 0):
                print("_", end=" ")
            else:
                print(str(grid[row][col]), end=" ")

            if((col +1) % 3 == 0 and col < 8):
                print("|", end=" ")

        print(Back.RESET)
        if((row +1) % 3 == 0 and row < 8):
            print(f"{grid_background}   +-----------------------{Back.RESET}")


def load_game():
    pass

def submit_details():
    pass


# Checks to see if number is valid.
def is_valid_move(grid, row, col, num):
    """
    Check if placing a number in a specified cell is a valid move in a Sudoku grid.

    Parameters:
    - grid (list): A 9x9 Sudoku grid.
    - row (int): The row index (0-8) of the cell to check.
    - col (int): The column index (0-8) of the cell to check.
    - num (int): The number to check for validity (1-9).

    Returns:
    - bool: True if the move is valid, False otherwise.

    The function checks whether placing the given number in the specified cell is a valid move
    according to Sudoku rules. It verifies that the number does not already exist in the same row,
    column, or the 3x3 sub-grid containing the specified cell.
    """


    # Checks to see if the number is allready in the row or column
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    # Creates a '3 X 3' sub-grid and checks to see if number is in subgrid.
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for _row in range(start_row, start_row + 3):
        for _col in range(start_col, start_col + 3):
            if grid[_row][_col] == num:
                return False

    # Valid move if number was not found in row, col or sub-grid.
    return True


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
    solve_sudoku(grid)

    puzzle = [row[:] for row in grid]
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle

