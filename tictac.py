board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def print_turn(player):
    print(player + "'s turn")
    position = input("Enter position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid choice (1-9)")
        position = input("Enter position from 1-9: ")
    position = int(position) - 1
    while board[position] != "_":
        position = int(input("Position already taken: ")) - 1
    board[position] = player
    print_board()


def check_game_over():
    if (board[0] == board[1] == board[2] != "_") or \
            (board[3] == board[4] == board[5] != "_") or \
            (board[6] == board[7] == board[8] != "_") or \
            (board[0] == board[3] == board[6] != "_") or \
            (board[1] == board[4] == board[7] != "_") or \
            (board[2] == board[5] == board[8] != "_") or \
            (board[0] == board[4] == board[8] != "_") or \
            (board[2] == board[4] == board[6] != "_"):
        return "win"
    elif "_" not in board:
        return "tie"
    else:
        return "play"


def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        print_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


play_game()
