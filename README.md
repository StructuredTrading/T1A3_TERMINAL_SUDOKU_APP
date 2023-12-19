<center>

#  T1A3 - Terminal Application

### Sam's Sudoku Puzzler
</center>
<br>
<br>

<a href="https://github.com/StructuredTrading/T1A3_TERMINAL_SUDOKU_APP">Github Repository</a>

<a href="https://app.asana.com/0/1206149212914837/1206149212914837">Asana Project Management</a>


## Project Information

Sam's Sudoku Puzzler App is a python-based application that allows users to play Sudoku puzzles. It provides an interactive interface for solving Sudoku puzzles and offers features like puzzle generation, saving and loading game states, and more.

<br>

## Code Style Guide

This project follows the Python style conventions outlined in <a href="https://peps.python.org/pep-0008/">PEP8</a>. 

PEP 8 is a style guide for Python code, and adherence to its conventions improves code readability and maintainability. Here are five basic rules from PEP 8 and how they are applied in the context of the Sudoku Puzzler App project:

- Indentation (Rule: Use 4 Spaces per Indentation Level):
  - each level of indentation in the Sudoku Puzzler App project is set to four spaces. This consistent indentation style is applied throughout the codebase for better readability.

- Maximum Line Length (Rule: Limit All Lines to 79 Characters for Code):
  - Lines of code in the Sudoku Puzzler App are limited to 79 characters to ensure readability. Longer lines are broken using backslashes.

- Imports (Rule: Imports Should Usually Be on Separate Lines):
  - Import statements are organized with standard library imports first, followed by third-party and local imports. Each group is separated by a blank line.

- Whitespace in Expressions and Statements (Rule: Avoid Extraneous Whitespace):
  - The Sudoku Puzzler App project adheres to the guidelines of avoiding unnecessary whitespace in expressions, parentheses, and other syntax elements.

- Function and Variable Naming (Rule: Function Names Should Be Lowercase, With Words Separated by Underscores):
  - Function and variable names are consistently named in lowercase with underscores for improved readability.

<br>

## Features

- Interactive Sudoku Grid:
  - The app provides an interactive 9x9 Sudoku grid for users to input their answers.
- Puzzle generation: 
  - Users can generate new Sudoku puzzles with varying degree of difficulty levels by choosing a number between 5 and 60. (This numbe represents the amount of numbers to solve on the grid.)
- Save and Load Game:
  - Save the current state of a Sudoku game and load it later to continue playing.
- User-Friendly Interface:
  - Intuitive design for a seamless user experience. 
  
<br>

## Implementation Plan

### Overview

As part of the development process for the Sudoku Puzzler App, I leveraged the Asana project management tool to streamline implimentation of different features and keep on track for deadlines of implimentation and development.

The implimentation plan was to break down each feature:
- Generate Random Sudoku Puzzles.
  - Create a basic generate function that creates a 9 X 9 grid of numbers 1-9
  - Perform tests on sudoku generate function to confirm puzzles are valid numbers
  - remove / hide numbers to make the puzzle playable
  - create a option for users to select difficulty or how many numbers to solve in puzzle
  - Bug test and implement correctly error handling
  
<br>

- Create a Save File Function.
  - Find what imports may be able to help with creating a save file
  - implement a function to save the current state of the sudoku game to a file
  - Prompt the user for input to trigger the save function (eg choosing to quit the game)
  - implement error handling in the save function to manage any issues that may arise.
  - test the functionality of the save file.
  
<br>

- Create a Load File Function.
  - Research ways to load a save file
  - Create a option for players to generate a new sudoku puzzle or load a previously saved puzzle
  - Ensure puzzles are loading correctly and are continuing on from their previous state
  - import libraries if needed to complete the task.
  - perform bug testing and error handling.

<br>

The list of features ready to be implimented:

<img src="./docs/features_task_list.png" alt="features_task_list"></img>

<br>

### Create a Sudoku Random Generator Function.

The goal of implementing the Sudoku random generator function is to create a random 9x9 Sudoku puzzle with varying levels of difficulty. This function is crucial for providing users with a diverse and enjoyable puzzle-solving experience.

<img src="./docs/random_generator_function_start.png" alt="random_generator_function_start"></img>

<img src="./docs/random_generator_function_doing.png" alt="random_generator_function_doing"></img>

<img src="./docs/random_generator_function_complete.png" alt="random_generator_function_complete"></img>

<br>

### Create a Save File Function.

The Save File function is responsible for saving the current state of the Sudoku game, including the filled-in numbers and the user's progress. This saved data is then stored in a file, format called pickle. Each save is unuqie using the username given by the users with the "_save" and the ".pickle" extention.

<img src="./docs/create_save_file_function_start.png" alt="create_save_file_function_start"></img>

<img src="./docs/create_save_file_function_doing.png" alt="create_save_file_function_doing"></img>

<img src="./docs/create_save_file_function_complete.png" alt="create_save_file_function_complete"></img>

<br>

#### Create a Load File Function.

The Load File function is designed to read a saved ".pickle" file, of the data, and restore the game state. It allows users to pick up where they left off by loading their saved Sudoku game.

<img src="./docs/create_load_file_function_doing.png" alt="create_load_file_function_doing"></img>

<img src="./docs/all_tasks_list_complete.png" alt="all_task_list_complete"></img>

<br>

### Testing

<br>

Once functions were written, testing was performed using pytest to make sure the functions are working as expected. Here is the results of the pytest log:

<img src="./docs/pytest_results.png" alt="pytest_results">

<br>

## Sam's Sudoku Puzzler App Help Documentation

### Installation

#### Requirements

Ensure you have the following prerequisites installed on your system:

- Python (version3.6 or higher)
- pip (Python package installer)

#### Installation Steps

1. Clone The Repository:

```
git clone https://github.com/StructuredTrading/T1A3_TERMINAL_SUDOKU_APP.git
```

<br>

2. Navigate to the Project Directory:

```
cd T1A3_TERMINAL_SUDOKU_APP
```

<br>

3. Make sure bash script is executable with the following command

```
chmod +x run.sh
```

<br>

4. Install Dependencies / Run App:

```
bash run.sh
```

<br>

### Running the Application

1. If You have allready run the 'run.sh' bash script. you can simply navigate to the project directory:

```
cd T1A3_TERMINAL_SUDOKU_APP
```

<br>

2. Open the python main.py file:

```
python3 main.py
```

<br>

### Gameplay Instructions

1. Welcome Screen - This is the first screen you will see when opening the sudoku App. You will be prompted to enter 'y' or 'n' to load a saved game. If you enter anything other then 'n' you will start a new game. 
<img src="./docs/welcome_screen.png" alt="welcome_screen"></img>

<br>

2. Load Screen - if you entered 'y' for yes, you will then be prompted to enter a username to load a saved game file.
<img src="./docs/load_screen.png" alt="load_screen"></img>

<br>

3. Game Loaded Successfully - if your saved game was found, you will see this screen to indicate it has loaded successfully. Once loaded it will display the sudoku grid as it was when you previously quit.
<img src="./docs/game_loaded_successfully.png" alt="game_loaded_successfully"></img>

<br>

4. No Save Found - if there was not a save file under that name, You will automatically create a new game with the entered username and be asked to choose a difficulty.
<img src="./docs/no_save_found.png" alt="no_save_found"></img>

<br>

5. New Game Screen - if you didn't select to load a saved game, this is the screen you would see. You will be prompted to enter a username.
<img src="./docs/new_game_screen.png" alt="new_game_screen"></img>

<br>

6. Select Difficulty - Once have entered a username you will need to select your difficulty between 5 and 60. The number represents how many numbers you will need to solve within the sudoku grid. So entering a higher number will result in a greater difficulty.
<img src="./docs/difficulty_screen.png" alt="difficulty_screen"></img>

<br>

7. Sudoku Game Screen - This is the sudoku game screen. You will be prompted to enter the row number, followed by the column number, followed by the number to solve the grid.
<img src="./docs/sudoku_grid_screen.png" alt="sudoku_grid_screen"></img>

<br>

8. Invalid Entry - If for some reason the entry you have entered is invalid, this is the screen you will see. You will be prompted to enter again.
<img src="./docs/sudoku_invalid_entry.png" alt="sudoku_invalid_entry"></img>

<br>

9. You Win Screen - This screen will display the message 'you win!' and prompt the player to choose if they would like to play again or quit.
<img src="./docs/you_win_screen.png" alt="you_win_screen"></img>