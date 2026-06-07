# Minimax Algorithm (Tic-Tac-Toe)
import math
board = [" "] * 9
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
def winner(b, p):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(b[pos] == p for pos in line) for line in wins)
def draw(b):
    return " " not in b
def minimax(b, is_max, alpha, beta):
    if winner(b, "X"):
        return 1
    if winner(b, "O"):
        return -1
    if draw(b):
        return 0
    if is_max:

        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = max(
                    best,
                    minimax(b, False, alpha, beta)
                )
                b[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = min(
                    best,
                    minimax(b, True, alpha, beta)
                )
                b[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best
def best_move():
    move = -1
    best_score = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def play():
    print("Positions:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    while True:
        print_board()
        pos = int(input("Enter your move (0-8): "))
        if board[pos] != " ":
            print("Invalid Move")
            continue
        board[pos] = "O"
        if winner(board, "O"):
            print_board()
            print("You Win!")
            break
        if draw(board):
            print_board()
            print("Draw!")
            break
        ai = best_move()
        board[ai] = "X"
        print("AI chose:", ai)

        if winner(board, "X"):
            print_board()
            print("AI Wins!")
            break
        if draw(board):
            print_board()
            print("Draw!")
            break
play()
