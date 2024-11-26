def print_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i < 2:
            print('-' * 5)

def check_win(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {players[turn]} - Enter row and column (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = players[turn]
            if check_win(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            if all(cell != ' ' for row in board for cell in row):
                print_board(board)
                print("It's a draw!")
                break
            turn = 1 - turn
        else:
            print("Cell is already occupied. Try again.")

tic_tac_toe()
