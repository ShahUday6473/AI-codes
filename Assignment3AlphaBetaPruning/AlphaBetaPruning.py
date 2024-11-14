MAX, MIN = float('inf'), float('-inf')
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:  
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(2):  
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):  
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
if __name__ == "__main__":
    values_input = input("Enter the leaf node values separated by commas (8 val): ")
    values = list(map(int, values_input.split(',')))
    expected_size = 2 ** 3  
    if len(values) != expected_size:
        print(f"Error: You must enter exactly {expected_size} values.")
    else:
        print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))

'''
Output 3,5,6,9,1,2,0,-1
Optimal value : 5'''