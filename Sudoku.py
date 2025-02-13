import tkinter as tk
from tkinter import messagebox
import random
import copy
class SudokuBoard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Advanced Sudoku Game")
        self.current_solution = None
        self.original_numbers = set()  # To track initial numbers

        # Create main frame
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(padx=10, pady=10)

        # Create 9x9 grid of entry widgets
        self.cells = {}
        for i in range(9):
            for j in range(9):
                # Create frame for each 3x3 box
                if i % 3 == 0 and j % 3 == 0:
                    box_frame = tk.Frame(
                        self.main_frame,
                        borderwidth=2,
                        relief='solid'
                    )
                    box_frame.grid(row=i//3, column=j//3, padx=1, pady=1)

                # Calculate box color
                box_color = 'white' if (i//3 + j//3) % 2 == 0 else '#f0f0f0'

                # Create entry widget
                cell = tk.Entry(
                    box_frame,
                    width=2,
                    font=('Arial', 18),
                    justify='center',
                    bg=box_color
                )

                # Position within 3x3 box
                cell.grid(row=i%3, column=j%3, padx=1, pady=1)
                cell.bind('<KeyRelease>', lambda e, i=i, j=j: self.validate_input(e, i, j))

                self.cells[(i, j)] = cell
                     # Create control panel
        self.control_panel = tk.Frame(self.window)
        self.control_panel.pack(pady=10)

        # Create difficulty selector
        self.difficulty = tk.StringVar(value="medium")
        tk.Label(self.control_panel, text="Difficulty:").pack(side=tk.LEFT)
        tk.Radiobutton(self.control_panel, text="Easy", variable=self.difficulty, 
                      value="easy").pack(side=tk.LEFT)
        tk.Radiobutton(self.control_panel, text="Medium", variable=self.difficulty, 
                      value="medium").pack(side=tk.LEFT)
        tk.Radiobutton(self.control_panel, text="Hard", variable=self.difficulty, 
                      value="hard").pack(side=tk.LEFT)

        # Create buttons
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack(pady=5)

        buttons = [
            ("New Game", self.generate_new_game),
            ("Check Solution", self.check_solution),
            ("Hint", self.give_hint),
            ("Clear Board", self.clear_board)
        ]

        for text, command in buttons:
            tk.Button(self.buttons_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)
    def validate_input(self, event, i, j):
            """Validates user input in cells"""
            cell = self.cells[(i, j)]
            value = cell.get()

            # Clear invalid inputs
            if value and not value.isdigit():
                cell.delete(0, tk.END)
                return

            if len(value) > 1:
                cell.delete(1, tk.END)
                value = value[0]

            if value and (i, j) not in self.original_numbers:
                if not self.is_valid_move(i, j, int(value)):
                    cell.config(fg='red')
                else:
                    cell.config(fg='blue')

    def is_valid_move(self, row, col, num):
        """Checks if a number placement is valid"""
        # Check row
        for j in range(9):
            if j != col:
                cell_value = self.cells[(row, j)].get()
                if cell_value and int(cell_value) == num:
                    return False

        # Check column
        for i in range(9):
            if i != row:
                cell_value = self.cells[(i, col)].get()
                if cell_value and int(cell_value) == num:
                    return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i, j) != (row, col):
                    cell_value = self.cells[(i, j)].get()
                    if cell_value and int(cell_value) == num:
                        return False

        return True
    def generate_new_game(self):
        """Generates a new Sudoku puzzle"""
        self.clear_board()
        self.original_numbers.clear()

        # Create a solved board
        self.current_solution = self.generate_solved_board()
        puzzle = copy.deepcopy(self.current_solution)

        # Remove numbers based on difficulty
        cells_to_keep = {
            "easy": 40,
            "medium": 30,
            "hard": 25
        }[self.difficulty.get()]

        # Randomly remove numbers
        cells_to_remove = 81 - cells_to_keep
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)

        for i, j in positions[:cells_to_remove]:
            puzzle[i][j] = 0

        # Fill the board
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    self.cells[(i, j)].insert(0, str(puzzle[i][j]))
                    self.cells[(i, j)].config(fg='black')
                    self.original_numbers.add((i, j))
    def generate_solved_board(self):
        """Generates a solved Sudoku board"""
        board = [[0]*9 for _ in range(9)]
        self.solve_board(board)
        return board

    def solve_board(self, board):
        """Solves the Sudoku board using backtracking"""
        empty = self.find_empty(board)
        if not empty:
            return True

        row, col = empty
        for num in random.sample(range(1, 10), 9):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve_board(board):
                    return True
                board[row][col] = 0

        return False

    def find_empty(self, board):
        """Finds an empty cell in the board"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
                    

