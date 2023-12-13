# from colorama import Fore, Style
# from os import system
# import random
import time
# import pickle
import functions as sudoku

sudoku_grid = [[]]


# The main function which is used to play the game.
def play_sudoku(username, sudoku_grid):

    time.sleep(2)
    sudoku.clear_console()
    sudoku.display_grid(sudoku_grid)

    while sudoku.moves_left(sudoku_grid) > 0:
        try:
            row = int(input("Enter the row number (1-9, or 0 to save and exit): "))
            if row == 0:
                print(f"Goodbye, {username}!")
                sudoku.save_game(username, sudoku_grid)
                break
            col = int(input("Enter the column number (1-9): "))
            num = int(input("Enter the number to fill (1-9): "))

            if(1 <= row <= 9 and 1 <= num <= 9 and 1 <= col <= 9):
                if(sudoku.is_valid_move(sudoku_grid, row -1, col -1, num)):
                    sudoku_grid[row-1][col-1] = num

                    sudoku.clear_console()

                    sudoku.display_grid(sudoku_grid)

                else:
                    print("invalid move! Try again.")
            else:
                print("Invalid input! Please enter valid row, column, and number.")
        except ValueError:
            print("Invalid input! Please enter valid row, column, and number.")
    else:
        print("You won!\n")
        play_again = input("Would you like to play again? (y/n)").lower()
        if(play_again == "y"):
            sudoku.clear_console()
            username, sudoku_grid = sudoku.new_game(username)
            play_sudoku(username, sudoku_grid)
        else:
            print(f"Goodbye, {username}!")




# Start of Application

sudoku.clear_console()
print("Welcome to Sam's Sudoku Puzzler App!")

load_option = input("Do you want to load a saved game? (y/n): ").lower()
if(load_option == "y"):
    username, sudoku_grid = sudoku.load_game()

    # No saved game found.
    if(not sudoku_grid):
        print(f"Starting new game as: {username}")
        username, sudoku_grid = sudoku.new_game(username)

else:
    username, sudoku_grid = sudoku.new_game(None)
    

play_sudoku(username, sudoku_grid)