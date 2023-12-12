import random

def load_game():
    pass

def submit_details():
    pass





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

