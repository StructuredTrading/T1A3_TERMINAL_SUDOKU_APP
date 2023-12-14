import functions as sudoku

# A valid move of row 3, col 5, num 7 should result in True.
def test_valid_move_valid_number():
    sudoku_grid = [
        [4, 2, 3, 1, 7, 6, 9, 8, 5],
        [1, 5, 6, 2, 8, 9, 3, 4, 7],
        [7, 8, 9, 3, 4, 5, 1, 2, 6],
        [2, 1, 4, 5, 3, 0, 6, 9, 8],
        [3, 6, 5, 4, 9, 0, 2, 7, 1],
        [8, 9, 7, 6, 1, 2, 4, 5, 3],
        [5, 3, 1, 7, 2, 4, 8, 6, 9],
        [6, 4, 8, 9, 5, 1, 7, 3, 2],
        [9, 0, 0, 8, 6, 0, 5, 1, 4]
    ]

    if(sudoku.is_valid_move(sudoku_grid, row = 3, col = 5, num = 7)):
        assert True
    else:
        assert False


# A invalid move of row 3, col 5, num 4 should result in False.
def test_valid_move_invalid_number():
    sudoku_grid = [
        [4, 2, 3, 1, 7, 6, 9, 8, 5],
        [1, 5, 6, 2, 8, 9, 3, 4, 7],
        [7, 8, 9, 3, 4, 5, 1, 2, 6],
        [2, 1, 4, 5, 3, 0, 6, 9, 8],
        [3, 6, 5, 4, 9, 0, 2, 7, 1],
        [8, 9, 7, 6, 1, 2, 4, 5, 3],
        [5, 3, 1, 7, 2, 4, 8, 6, 9],
        [6, 4, 8, 9, 5, 1, 7, 3, 2],
        [9, 0, 0, 8, 6, 0, 5, 1, 4]
    ]

    if(not sudoku.is_valid_move(sudoku_grid, row = 3, col = 5, num = 4)):
        assert True
    else:
        assert False

    
# A invalid move of row 1, col 4, num 3 should result in False.
def test_valid_move_invalid_location():
    sudoku_grid = [
        [4, 2, 3, 1, 7, 6, 9, 8, 5],
        [1, 5, 6, 2, 8, 9, 3, 4, 7],
        [7, 8, 9, 3, 4, 5, 1, 2, 6],
        [2, 1, 4, 5, 3, 0, 6, 9, 8],
        [3, 6, 5, 4, 9, 0, 2, 7, 1],
        [8, 9, 7, 6, 1, 2, 4, 5, 3],
        [5, 3, 1, 7, 2, 4, 8, 6, 9],
        [6, 4, 8, 9, 5, 1, 7, 3, 2],
        [9, 0, 0, 8, 6, 0, 5, 1, 4]
    ]

    if(not sudoku.is_valid_move(sudoku_grid, row = 1, col = 4, num = 3)):
        assert True
    else:
        assert False


# A blank username should return False from valid_useraname() function. 
def test_valid_username_blank_username():
    username = ""
    if(not sudoku.valid_username(username)):
        assert True
    else: 
        assert False

# A username with a space in it should return False from valid_username() function.
def test_valid_username_spaces_in_username():
    username = "my username"
    if(not sudoku.valid_username(username)):
        assert True
    else: 
        assert False

# A username with special characters should return False from valid_username() funcion.
def test_valid_username_special_characters_in_username():
    username = "%$#@@()"
    if(not sudoku.valid_username(username)):
        assert True
    else: 
        assert False