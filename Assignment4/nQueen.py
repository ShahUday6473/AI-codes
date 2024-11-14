N = 8  # Change this to any value for N-Queens

def printSol(board):
    for row in board:
        print(" ".join(str(x) for x in row))

def isSafe(row, col, board, rowLookup, slashLookup, backslashLookup):
    if rowLookup[row] or slashLookup[row + col] or backslashLookup[row - col + N - 1]:
        return False
    return True

def solveNQUtil(board, col, rowLookup, slashLookup, backslashLookup):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(i, col, board, rowLookup, slashLookup, backslashLookup):
            board[i][col] = 1
            rowLookup[i] = slashLookup[i + col] = backslashLookup[i - col + N - 1] = True

            if solveNQUtil(board, col + 1, rowLookup, slashLookup, backslashLookup):
                return True

            # Backtrack
            board[i][col] = 0
            rowLookup[i] = slashLookup[i + col] = backslashLookup[i - col + N - 1] = False

    return False

def solveNQ():
    board = [[0] * N for _ in range(N)]
    rowLookup = [False] * N
    slashLookup = [False] * (2 * N - 1)
    backslashLookup = [False] * (2 * N - 1)

    if not solveNQUtil(board, 0, rowLookup, slashLookup, backslashLookup):
        print("Solution does not exist")
        return False

    printSol(board)
    return True

# Run the N-Queens solution
solveNQ()
