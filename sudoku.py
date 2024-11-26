import time
import os
from boards import create_boards
import random

file_path = "boards.txt"

def is_number_in_row(board, number, row):
    return number in board[row]

def is_number_in_column(board, number, column):
    return any(board[i][column] == number for i in range(9))

def is_number_in_box(board, number, row, column):
    start_row, start_col = 3 * (row // 3), 3 * (column // 3)
    return any(
        board[i][j] == number
        for i in range(start_row, start_row + 3)
        for j in range(start_col, start_col + 3)
    )

def is_safe(board, number, row, column):
    return (
        not is_number_in_row(board, number, row)
        and not is_number_in_column(board, number, column)
        and not is_number_in_box(board, number, row, column)
    )

def print_board_slowly(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for animation
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print("\n")
    time.sleep(0.1)  # Delay to simulate animation

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print("\n")

def solve(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:  # Empty cell found
                for number in range(1, 10):  # Try numbers 1-9
                    if is_safe(board, number, row, column):
                        board[row][column] = number  # Place the number
                        print_board_slowly(board)  # Show current board
                        
                        if solve(board):  # Recursive step
                            return True
                        board[row][column] = 0  # Backtrack
                        print_board_slowly(board)  # Show backtracking step
                return False  # No valid number found
    return True  # Solved

# Initial Sudoku board

boards = create_boards(file_path)

random_num =  random.randint(0,len(boards) - 1)
board = []
board = boards[random_num]


if solve(board):
    print("Sudoku solved!")
else:
    print("No solution exists!")
