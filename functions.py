import random 
import subprocess
import os
import pickle
# import colorama
from colorama import Fore, Back



# Displays the sudoku grid
def display_grid(grid):
    """
    Displays the Sudoku grid on the screen.

    Parameters:
    - grid (list): A 9X9 Sudoku grid.

    Returns:
    - None

    The function is used to display the Sudoku grid to the user, With numbers above and to the left of the grid to be used to help players choose a position for their next move.
    """
    grid_text = Fore.BLACK
    grid_background = Back.WHITE
    print(f"   {grid_background}{grid_text}Sam's Sudoku Puzzler!{Back.RESET}")
    print()
    print()
    print(f"{grid_background}     1 2 3   4 5 6   7 8 9 {Back.RESET}")
    print(f"{grid_background}   +----------------------+{Back.RESET}")
    for row in range(9):
        print(f"{grid_background}{grid_text}{row + 1}  | ", end="")
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

    print(f"{Fore.RESET}")



def valid_username(username):
    """
    Check if a username is valid.

    Parameters:
    - username (str): The input username to be validated.

    Returns:
    - bool: True if the username consists only of alphabetic characters,
            False otherwise.

    This function validates a username by checking if it consists only of alphabetic
    characters. If the username is valid, it returns True. If the username is non-empty
    but contains non-alphabetic characters or spaces, it prints an error message and
    returns False. If the username is empty, it returns False.
    """
    if(username.isalpha()):
        return True
    elif(username != ""):
        print("Please only enter Alphabetic characters without spaces.")
        return False
    return False



# Load's a saved game.
def load_game():
    """
    Load a saved Sudoku game.

    Returns:
    - Tuple[str, list]: A tuple containing the loaded player's username and the Sudoku grid.
      If no saved game is found, returns (None, None).

    This function prompts the user to input their username and attempts to load a saved Sudoku game
    from a binary file named "{username}_save.pickle". If the file is found, the game is loaded
    successfully, and the player's username and Sudoku grid are returned. If no saved game is found,
    a message is printed, and (None, None) is returned.
    """
    try:
        username = ""
        while not valid_username(username):
            username = input("Input your username to load a save file: ").lower()
        with open(f"{username}_save.pickle", "rb") as file:
            data = pickle.load(file)
        print("Game loaded successfully.")
        return(data["username"], data["sudoku_grid"])
    except FileNotFoundError:
        print("No saved game found.")
        return username, None



# Save's the game.
def save_game(username, sudoku_grid):
    """
    Save the current Sudoku game state.

    Parameters:
    - username (str): The player's username.
    - sudoku_grid (list): The current state of the Sudoku grid.

    This function saves the current state of a Sudoku game, including the player's
    username and the Sudoku grid, into a binary file using pickle. The file is named
    "{username}_save.pickle". A success message is printed after saving.
    """
    data = {
        "username": username,
        "sudoku_grid": sudoku_grid
    }

    with open(f"{username}_save.pickle", "wb") as file:
        pickle.dump(data, file)
        print("Game saved successfully.")



# Sets difficulty for a new sudoku game.
def new_game(username):
    """
    Start a new Sudoku game.

    Parameters:
    - username (str): The player's username. If None, prompt the user to enter a username.

    Returns:
    - Tuple[str, list]: A tuple containing the player's username and the generated Sudoku grid.

    This function initiates a new Sudoku game, allowing the player to set their username
    and choose the difficulty level. If a username is not provided, the user will be prompted
    to enter one. The difficulty level is set by the player, and a Sudoku grid is generated
    based on the chosen difficulty.
    """
    if(username == ""):
        while(not valid_username(username)):
            username = input("Enter a username: ").lower()
    difficulty = 0
    while(difficulty < 5 or difficulty > 60):
        try:
            difficulty = int(input(f"Hello {username}, set your difficulty by entering a number between 5 and 60 (The higher the number, the harder the puzzle!): "))
        except ValueError:
            print("Invalid input.")
    sudoku_grid = generate_grid(difficulty)

    return username, sudoku_grid
    


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



# Completes a sudoku puzzle.
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
def generate_grid(difficulty):
    """
    creates a random sudoku grid in a formatted way.

    Parameters:
    - grid (list): The 9x9 Sudoku grid represented as a list of lists.

    Returns:
    list[list[int]]
    """

    # Creates a 9 X 9 list of lists
    grid = [[0] * 9 for _ in range(9)]

    # Randomizes the first row the grid, then assign to first row.
    randomize_first_row = random.sample(range(1,10), 9)
    for _col in range(9):
        grid[0][_col] = randomize_first_row[_col]
    
    # Completes the rest of the sudoku puzzle
    solve_sudoku(grid)

    # Removes 'X' amount of numbers specified by the user setting the difficulty and returns the grid to solve.
    puzzle = [row[:] for row in grid]
    for _ in range(difficulty):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while(puzzle[row][col] == 0):
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle



# Clears the console screen
def clear_console():
    """Clears the console screen."""
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)



# Returns how many moves left
def moves_left(sudoku_grid):
    """
    Count the number of empty cells (moves left) in a Sudoku grid.

    Parameters:
    - sudoku_grid (list): A 9x9 Sudoku grid represented as a list of lists.
      Empty cells are denoted by the value 0.

    Returns:
    - int: The number of empty cells remaining in the Sudoku grid.

    This function iterates through each cell in the Sudoku grid and counts the
    number of empty cells (cells with the value 0), indicating the remaining moves
    available in the Sudoku puzzle.
    """
    moves = 0
    for _row in range(9):
        for _col in range(9):
            if(sudoku_grid[_row][_col] == 0):
                moves += 1
    return(moves)