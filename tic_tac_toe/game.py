def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def play():
    board = [str(i+1) for i in range(9)]
    current = "X"

    print("Tic Tac Toe!")
    print("Enter position (1-9):")
    print_board(board)

    for turn in range(9):
        while True:
            try:
                move = int(input(f"Player {current}, enter position: ")) - 1
                if 0 <= move <= 8 and board[move] not in ("X", "O"):
                    break
                print("Invalid move. Try again.")
            except ValueError:
                print("Enter a number 1-9.")

        board[move] = current
        print_board(board)

        if check_winner(board, current):
            print(f"Player {current} wins!")
            return

        current = "O" if current == "X" else "X"

    print("It's a draw!")

play()