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