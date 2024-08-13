import math

def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return '' not in board

def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == '']

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ''
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ''
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ''
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [''] * 9
    while True:
        print_board(board)
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != '':
            print("Invalid move! Try again.")
            continue
        board[human_move] = 'X'
        if check_win(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        print("AI's turn:")
        board[ai_move(board)] = 'O'
        if check_win(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()

