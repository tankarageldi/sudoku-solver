# Sudoku Solver with Animation

This is a Python-based Sudoku solver that uses the backtracking algorithm to solve a given Sudoku puzzle. It now supports loading multiple starting boards from a file, with the ability to solve a randomly selected puzzle.

---

## Features

- Solves any valid 9x9 Sudoku puzzle using backtracking.
- Loads multiple puzzles from a `boards.txt` file.
- Randomly selects a puzzle from the list of available puzzles.
- Displays the solving process in real-time, simulating an animation effect.
- Clear and easy-to-read output for both the initial and solved board states.

---

## How It Works

1. The program reads 9x9 Sudoku boards from a text file (`boards.txt`), where:

   - Numbers (1-9) represent pre-filled cells.
   - `0` represents empty cells to be solved.
   - Boards are stored on a single line, separated by spaces. Example:

     ```bash

     3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0 0 8 7 0 0 0 0 3 1 0 0 3 0 1 0 0 8 0 9 0 0 8 6 3 0 0 5 0 5 0 0 9 0 6 0 0 1 3 0 0 0 0 2 5 0 0 0 0 0 0 0 0 7 4 0 0 5 2 0 6 3 0 0
     ```

     - Multiple boards are stored sequentially.

2. A Python script loads the boards into memory and picks one at random to solve.

3. The **backtracking algorithm** attempts to:

   - Place numbers 1-9 in each empty cell.
   - Validate placements according to Sudoku rules:
     - Each number must appear exactly once in each row, column, and 3x3 subgrid.
   - If no valid number can be placed, it backtracks and tries a different configuration.

4. The solving process is visualized in the terminal, with updates displayed step-by-step.

---

## How to Run

1. Ensure you have Python 3 installed.
2. Create a `boards.txt` file in the same directory as the script and populate it with Sudoku puzzles.
3. Run the program using:

   ```bash
   python sudoku.py
   ```

---

## Customization

- **Adding Boards:**
  - Add more puzzles to `boards.txt` by appending them in the required format.
- **Animation Speed:**
  - Adjust the solving animation speed by modifying the `time.sleep()` value in the `print_board_slowly` function.

---
