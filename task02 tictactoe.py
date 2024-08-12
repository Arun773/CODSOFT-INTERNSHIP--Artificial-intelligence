import random
print("WELCOME TO TIC-TAC-TOE")

board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(' | '.join(row))
        print('---------')

def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw(board):
    return ' ' not in board

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -1
    elif check_win(board, 'O'):
        return 1
    elif check_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def ai_move():
    best_move = None
    best_eval = float('-inf')
    for move in available_moves(board):
        board[move] = 'O'
        eval = minimax(board, 0, False)
        board[move] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

while True:
    print_board()
    if check_win(board, 'X'):
        print("You win!")
        break
    elif check_win(board, 'O'):
        print("AI wins!")
        break
    elif check_draw(board):
        print("It's a draw!")
        break

    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == ' ':
        board[player_move] = 'X'
    else:
        print("Invalid move. Try again.")
        continue

    if check_draw(board):
        print("It's a draw!")
        break

    ai_turn = ai_move()
    board[ai_turn] = 'O'
