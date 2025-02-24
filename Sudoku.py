import tkinter as tk
from tkinter import messagebox
import random
import copy

class LoginScreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Login")
        self.window.geometry("400x500")
        self.window.configure(bg='#2C3E50')

        # Create main frame
        self.frame = tk.Frame(self.window, bg='#2C3E50')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Logo/Title
        self.title_label = tk.Label(
            self.frame,
            text="SUDOKU",
            font=('Arial Black', 32, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50',
            pady=20
        )
        self.title_label.pack()

        # Welcome message
        self.welcome_label = tk.Label(
            self.frame,
            text="Welcome! Please login to play",
            font=('Arial', 12),
            fg='#ECF0F1',
            bg='#2C3E50',
            pady=10
        )
        self.welcome_label.pack()

        # Username
        self.username_frame = tk.Frame(self.frame, bg='#2C3E50')
        self.username_frame.pack(pady=10)

        self.username_label = tk.Label(
            self.username_frame,
            text="Username:",
            font=('Arial', 10),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        self.username_label.pack()

        self.username_entry = tk.Entry(
            self.username_frame,
            font=('Arial', 12),
            width=20
        )
        self.username_entry.pack(pady=5)

        # Password
        self.password_frame = tk.Frame(self.frame, bg='#2C3E50')
        self.password_frame.pack(pady=10)

        self.password_label = tk.Label(
            self.password_frame,
            text="Password:",
            font=('Arial', 10),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        self.password_label.pack()

        self.password_entry = tk.Entry(
            self.password_frame,
            font=('Arial', 12),
            width=20,
            show="*"  # Masks password with dots
        )
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(
            self.frame,
            text="Login",
            command=self.login,
            font=('Arial', 12, 'bold'),
            bg='#27AE60',
            fg='white',
            width=15,
            pady=8,
            relief='raised',
            bd=2
        )
        self.login_button.pack(pady=20)

        # Register Link
        self.register_label = tk.Label(
            self.frame,
            text="New user? Register here",
            font=('Arial', 10, 'underline'),
            fg='#3498DB',
            bg='#2C3E50',
            cursor="hand2"
        )
        self.register_label.pack(pady=10)
        self.register_label.bind("<Button-1>", self.show_register)

        # For demonstration, store some dummy users
        self.users = {
            "demo": "password123",
            "test": "test123"
        }

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.window.destroy()  # Close login window
            game = SudokuBoard()  # Start Sudoku game
            game.run()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_register(self, event=None):
        self.window.destroy()
        signup = SignupScreen()
        signup.run()

    def run(self):
        self.window.mainloop()
        

class SignupScreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Signup")
        self.window.geometry("400x600")  # Made taller for requirement labels
        self.window.configure(bg='#2C3E50')

        # Create main frame
        self.frame = tk.Frame(self.window, bg='#2C3E50')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        self.title_label = tk.Label(
            self.frame,
            text="CREATE ACCOUNT",
            font=('Arial Black', 24, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50',
            pady=20
        )
        self.title_label.pack()

        # Username Requirements
        self.username_req_label = tk.Label(
            self.frame,
            text="Username must:\n Be 4-20 characters long\n Contain only letters, numbers, or underscore\n Start with a letter",
            font=('Arial', 9),
            fg='#BDC3C7',
            bg='#2C3E50',
            justify='left'
        )
        self.username_req_label.pack(pady=(10,0))

        # Username
        self.username_frame = tk.Frame(self.frame, bg='#2C3E50')
        self.username_frame.pack(pady=5)

        self.username_label = tk.Label(
            self.username_frame,
            text="Create Username:",
            font=('Arial', 10),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        self.username_label.pack()

        self.username_entry = tk.Entry(
            self.username_frame,
            font=('Arial', 12),
            width=20
        )
        self.username_entry.pack(pady=5)

        # Password Requirements
        self.password_req_label = tk.Label(
            self.frame,
            text="Password must:\n Be 8-30 characters long\n Contain at least one uppercase letter\n Contain at least one lowercase letter\n Contain at least one number\n Contain at least one special character (!@#$%^&*)",
            font=('Arial', 9),
            fg='#BDC3C7',
            bg='#2C3E50',
            justify='left'
        )
        self.password_req_label.pack(pady=(10,0))

        # Password
        self.password_frame = tk.Frame(self.frame, bg='#2C3E50')
        self.password_frame.pack(pady=5)

        self.password_label = tk.Label(
            self.password_frame,
            text="Create Password:",
            font=('Arial', 10),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        self.password_label.pack()

        self.password_entry = tk.Entry(
            self.password_frame,
            font=('Arial', 12),
            width=20,
            show="*"
        )
        self.password_entry.pack(pady=5)

        # Confirm Password
        self.confirm_frame = tk.Frame(self.frame, bg='#2C3E50')
        self.confirm_frame.pack(pady=10)

        self.confirm_label = tk.Label(
            self.confirm_frame,
            text="Confirm Password:",
            font=('Arial', 10),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        self.confirm_label.pack()

        self.confirm_entry = tk.Entry(
            self.confirm_frame,
            font=('Arial', 12),
            width=20,
            show="*"
        )
        self.confirm_entry.pack(pady=5)

        # Show/Hide Password Checkbox
        self.show_password_var = tk.BooleanVar()
        self.show_password_check = tk.Checkbutton(
            self.frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            bg='#2C3E50',
            fg='#ECF0F1',
            selectcolor='#34495E'
        )
        self.show_password_check.pack(pady=5)

        # Signup Button
        self.signup_button = tk.Button(
            self.frame,
            text="Sign Up",
            command=self.signup,
            font=('Arial', 12, 'bold'),
            bg='#27AE60',
            fg='white',
            width=15,
            pady=8,
            relief='raised',
            bd=2
        )
        self.signup_button.pack(pady=20)

        # Login Link
        self.login_label = tk.Label(
            self.frame,
            text="Already have an account? Login here",
            font=('Arial', 10, 'underline'),
            fg='#3498DB',
            bg='#2C3E50',
            cursor="hand2"
        )
        self.login_label.pack(pady=10)
        self.login_label.bind("<Button-1>", self.show_login)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
            self.confirm_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            self.confirm_entry.config(show="*")

    def validate_username(self, username):
        import re
        # Check if username starts with a letter and contains only letters, numbers, or underscore
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]{3,19}$'
        return bool(re.match(pattern, username))

    def validate_password(self, password):
        import re
        # Check length
        if not (8 <= len(password) <= 30):
            return False

        # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            return False

        # Check for at least one lowercase letter
        if not re.search(r'[a-z]', password):
            return False

        # Check for at least one number
        if not re.search(r'\d', password):
            return False

        # Check for at least one special character
        if not re.search(r'[!@#$%^&*]', password):
            return False

        return True

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if not self.validate_username(username):
            messagebox.showerror("Error", "Username does not meet requirements")
            return

        if not self.validate_password(password):
            messagebox.showerror("Error", "Password does not meet requirements")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Here you would typically save the new user to your database
        messagebox.showinfo("Success", "Account created successfully!")
        self.window.destroy()
        login = LoginScreen()
        login.run()

    def show_login(self, event=None):
        self.window.destroy()
        login = LoginScreen()
        login.run()

    def run(self):
        self.window.mainloop()

class SudokuBoard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Advanced Sudoku Game")
        self.current_solution = None
        self.original_numbers = set()

        # Set window background and style
        self.window.configure(bg='#2C3E50')  # Dark blue-grey background

        # Create title label with decorative styling
        title_label = tk.Label(
            self.window,
            text="SUDOKU",
            font=('Arial Black', 24, 'bold'),
            fg='#ECF0F1',  # Light grey text
            bg='#2C3E50',  # Match window background
            pady=10
        )
        title_label.pack()

        # Create main frame with border effect
        outer_frame = tk.Frame(self.window, bg='#E74C3C', padx=3, pady=3)  # Red border
        middle_frame = tk.Frame(outer_frame, bg='#ECF0F1', padx=2, pady=2)  # White border
        self.main_frame = tk.Frame(middle_frame, bg='#2C3E50')  # Dark blue-grey background

        outer_frame.pack(padx=10, pady=10)
        middle_frame.pack()
        self.main_frame.pack()

        # Create 9x9 grid of entry widgets
        self.cells = {}
        for i in range(9):
            for j in range(9):
                # Alternate colors for 3x3 boxes
                if (i//3 + j//3) % 2 == 0:
                    cell_bg = '#FCF3CF'  # Light yellow
                else:
                    cell_bg = '#FFFFFF'  # White

                # Create entry widget with styled border
                cell = tk.Entry(
                    self.main_frame,
                    width=2,
                    font=('Arial', 20, 'bold'),
                    justify='center',
                    bg=cell_bg,
                    fg='#2C3E50',  # Dark text
                    relief='solid',
                    borderwidth=1
                )

                # Add padding for 3x3 box effect
                padx = (1, 2) if j % 3 == 2 and j != 8 else 1
                pady = (1, 2) if i % 3 == 2 and i != 8 else 1

                cell.grid(row=i, column=j, padx=padx, pady=pady, ipady=6)
                cell.bind('<KeyRelease>', lambda e, i=i, j=j: self.validate_input(e, i, j))

                self.cells[(i, j)] = cell

        # Create styled control panel
        self.control_panel = tk.Frame(self.window, bg='#2C3E50')
        self.control_panel.pack(pady=10)

        # Create difficulty selector with styled radio buttons
        self.difficulty = tk.StringVar(value="medium")
        difficulty_label = tk.Label(
            self.control_panel,
            text="Difficulty:",
            font=('Arial', 12, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        difficulty_label.pack(side=tk.LEFT, padx=5)

        for level in ["Easy", "Medium", "Hard"]:
            rb = tk.Radiobutton(
                self.control_panel,
                text=level,
                variable=self.difficulty,
                value=level.lower(),
                font=('Arial', 10),
                fg='#ECF0F1',
                bg='#2C3E50',
                selectcolor='#34495E'
            )
            rb.pack(side=tk.LEFT, padx=5)

        # Create styled buttons
        self.buttons_frame = tk.Frame(self.window, bg='#2C3E50')
        self.buttons_frame.pack(pady=10)

        button_style = {
            'font': ('Arial', 11, 'bold'),
            'width': 12,
            'relief': 'raised',
            'bd': 2,
            'padx': 10,
            'pady': 5
        }

        button_configs = [
            ("New Game", self.generate_new_game, '#27AE60'),  # Green
            ("Check Solution", self.check_solution, '#3498DB'),  # Blue
            ("Hint", self.give_hint, '#E67E22'),  # Orange
            ("Clear Board", self.clear_board, '#E74C3C')  # Red
        ]

        for text, command, color in button_configs:
            btn = tk.Button(
                self.buttons_frame,
                text=text,
                command=command,
                bg=color,
                fg='white',
                activebackground=color,
                activeforeground='white',
                **button_style
            )
            btn.pack(side=tk.LEFT, padx=5)

        # Add a decorative footer
        footer = tk.Label(
            self.window,
            text="Good Luck!",
            font=('Arial', 10, 'italic'),
            fg='#ECF0F1',
            bg='#2C3E50',
            pady=5
        )
        footer.pack()

        # Configure window
        self.window.resizable(False, False)
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
            "easy": 50,
            "medium": 40,
            "hard": 30
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
    def is_valid(self, board, row, col, num):
        """Checks if a number is valid in the board"""
        # Check row
        for j in range(9):
            if board[row][j] == num and j != col:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num and i != row:
                return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num and (i, j) != (row, col):
                    return False

        return True
    
    def check_solution(self):
        """Checks if the current board state is correct"""
        for i in range(9):
            for j in range(9):
                value = self.cells[(i, j)].get()
                if not value:
                    messagebox.showinfo("Incomplete", "Please fill in all cells!")
                    return
                if not self.is_valid_move(i, j, int(value)):
                    messagebox.showinfo("Incorrect", "There are some errors in your solution.")
                    return
        messagebox.showinfo("Congratulations!", "You solved the puzzle correctly!")
    def give_hint(self):

        if not self.current_solution:
            messagebox.showinfo("Error", "No puzzle in progress!")
            return

        # Initialize hint tracking if not exists
        if not hasattr(self, 'hints_used'):
            self.hints_used = 0
            self.hint_limit = {'easy': 5, 'medium': 3, 'hard': 2}
            self.last_hint_time = 0

        # Check hint limits based on difficulty
        current_limit = self.hint_limit[self.difficulty.get()]
        if self.hints_used >= current_limit:
            messagebox.showinfo("Hint Limit", 
                f"Maximum hints ({current_limit}) reached for {self.difficulty.get()} difficulty!")
            return

        # Collect and analyze empty cells
        empty_cells = []
        cell_scores = {}

        for i in range(9):
            for j in range(9):
                if not self.cells[(i, j)].get():
                    empty_cells.append((i, j))
                    # Calculate complexity score for this cell
                    score = self._calculate_hint_score(i, j)
                    cell_scores[(i, j)] = score

        if not empty_cells:
            messagebox.showinfo("No Hints", "No empty cells to hint!")
            return

        # Select cell based on difficulty and scores
        selected_cell = self._select_hint_cell(empty_cells, cell_scores)
        if selected_cell:
            row, col = selected_cell
            self._apply_hint_effect(row, col)
            self.hints_used += 1

    def _calculate_hint_score(self, row, col):
        """Calculate the strategic importance of a cell for hinting"""
        score = 0

        # Count filled neighbors
        filled_neighbors = 0
        for i in range(9):
            if self.cells[(row, i)].get():  # Row check
                filled_neighbors += 1
            if self.cells[(i, col)].get():  # Column check
                filled_neighbors += 1

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.cells[(i, j)].get():
                    filled_neighbors += 1

        # Calculate positional weight
        center_distance = abs(row - 4) + abs(col - 4)
        positional_weight = 9 - center_distance  # Prefer center cells

        # Calculate final score
        score = (filled_neighbors * 2) + positional_weight
        return score

    def _select_hint_cell(self, empty_cells, cell_scores):
        """Select appropriate cell based on difficulty and scores"""
        if not empty_cells:
            return None

        sorted_cells = sorted(cell_scores.items(), key=lambda x: x[1])
        difficulty = self.difficulty.get()

        if difficulty == 'easy':
            # Choose easiest cell (highest score)
            return sorted_cells[-1][0]
        elif difficulty == 'hard':
            # Choose harder cell (lower score)
            return sorted_cells[0][0]
        else:  # medium
            # Choose medium difficulty cell
            mid_index = len(sorted_cells) // 2
            return sorted_cells[mid_index][0]

    def _apply_hint_effect(self, row, col):
        """Apply visual feedback for the hint"""
        cell = self.cells[(row, col)]
        value = str(self.current_solution[row][col])

        # Animated hint effect
        original_bg = cell['bg']

        # Flash effect
        def flash_sequence():
            cell.config(bg='yellow')
            self.window.after(200, lambda: cell.config(bg='white'))
            self.window.after(400, lambda: cell.config(bg='yellow'))
            self.window.after(600, lambda: cell.config(bg=original_bg))
            self.window.after(800, lambda: cell.insert(0, value))
            self.window.after(800, lambda: cell.config(fg='green'))

        flash_sequence()
    def clear_board(self):
        """Clears all cells on the board"""
        for cell in self.cells.values():
            cell.delete(0, tk.END)
            cell.config(fg='black')

    def run(self):
        """Starts the game"""
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = LoginScreen()
    game.run()
       
