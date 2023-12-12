from colorama import Fore, Style
from os import system
import random
import time
import pickle
import functions 




def play_sudoku():
    print("Welcome to Sam's Sudoku Puzzler App!")

    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if(load_option == "y"):
        username = functions.load_game()
        if(not username):
            print("No saved game found. Starting a new game.")
    else:
        username = input("Enter a username: ")
        sudoku_grid = functions.generate_grid()
        points = 0

    time.sleep(1)
    print(sudoku_grid)

system("Sam's Sudoku Puzzler")
play_sudoku()