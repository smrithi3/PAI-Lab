def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                      [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                      [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for condition in win_conditions:
        if all(board[i][j] == player for i, j in condition):
            return True
    return False

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    for _ in range(9):
        print_board(board)
        print(f"Player {players[current_player]}'s turn")
        row, col = map(int, input("Enter row and column (0-2, 0-2): ").split())

        if board[row][col] != ' ':
            print("Invalid move, try again.")
            continue
        
        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            return

        current_player ^= 1

    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()
