# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

# Function to check if placing num at position (row, col) is valid
def is_safe(board, row, col, num):
    # Check if num is not in the same row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num is not in the same column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if num is not in the same 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:  # No more empty cells, puzzle solved
        return True

    row, col = empty_cell

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num  # Place num
            if solve_sudoku(board):  # Recur to place rest of the numbers
                return True
            board[row][col] = 0  # Backtrack if num doesn't lead to a solution

    return False  # Trigger backtracking if no number can be placed in this cell

# Helper function to find an empty location in the Sudoku board
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 represents an empty cell
                return i, j
    return None  # No empty cell found

# Example Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("Sudoku solved successfully!")
    print_board(board)
else:
    print("No solution exists.")
