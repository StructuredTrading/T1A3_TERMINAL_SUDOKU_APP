#!/bin/bash

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "Python 3 is installed."
    sleep 2

    # Run virtual_environment bash script
    bash virtual_environment.sh

    # run install_dependencies bash script
    bash install_dependencies.sh
   
    # run sudoku app
    echo "Running application: Sam's Sudoku Puzzler APP"
    sleep 5
    python3 main.py

else
    bash python_install.sh
fi
