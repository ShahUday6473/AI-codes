# Define players
player, opponent = 'x', 'o'

# Function to check if any moves are left on the board
def isMovesLeft(board):
    return any('_' in row for row in board)

# Function to evaluate the board and return a score
def evaluate(board):
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':  # Check row
            return 10 if board[i][0] == player else -10
        if board[0][i] == board[1][i] == board[2][i] != '_':  # Check column
            return 10 if board[0][i] == player else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 10 if board[0][0] == player else -10
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 10 if board[0][2] == player else -10

    # No winner, return 0
    return 0

# Minimax function to find the optimal move
def minimax(board, depth, isMax):
    score = evaluate(board)

    # If the player has won, return the score
    if score == 10 or score == -10:
        return score

    # If no moves left, return a tie
    if not isMovesLeft(board):
        return 0

    # Maximizer's move
    if isMax:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player  # Make a move
                    best = max(best, minimax(board, depth + 1, False))  # Recursive minimax
                    board[i][j] = '_'  # Undo the move
        return best

    # Minimizer's move
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent  # Make a move
                    best = min(best, minimax(board, depth + 1, True))  # Recursive minimax
                    board[i][j] = '_'  # Undo the move
        return best

# Function to find the best possible move for the player
def findBestMove(board):
    bestVal = -float('inf')
    bestMove = (-1, -1)

    # Traverse all cells and evaluate minimax function for each move
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player  # Make the move
                moveVal = minimax(board, 0, False)  # Compute the minimax value
                board[i][j] = '_'  # Undo the move

                # If the move is better than the current best, update bestMove
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best move is:", bestVal)
    return bestMove

# Driver code to test the findBestMove function
board = [
    ['x', 'o', 'x'],
    ['o', 'o', 'x'],
    ['_', '_', '_']
]

bestMove = findBestMove(board)
print("The Optimal Move is:")
print("ROW:", bestMove[0], "COL:", bestMove[1])
