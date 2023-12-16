#!/bin/bash

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "Python 3 is installed."

    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install colorama
    python3 main.py

else
    echo "Python 3 is not installed. Please install Python 3 before proceeding."
fi
