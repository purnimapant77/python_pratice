import random
def print_board(board):
    symbols = {
        "X": " X ", "O": " O ",
    }
    print()
    for i in range(3):
        row = []
        for cell in board[i*3:(i+1)*3]:
            if cell in ("X", "O"):
                row.append(symbols[cell])
            else:
                row.append(f"[{cell}]")  # numbered empty cell
        print(" | ".join(row))
        if i < 2:
            print("-----------")
    print()

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def bot_move(board):
    # Try to win
    for i in range(9):
        if board[i] not in ("X", "O"):
            board[i] = "O"
            if check_winner(board, "O"):
                return i
            board[i] = str(i+1)

    # Block player
    for i in range(9):
        if board[i] not in ("X", "O"):
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = str(i+1)
                return i
            board[i] = str(i+1)

    # Take center
    if board[4] not in ("X", "O"):
        return 4

    # Take random
    empty = [i for i in range(9) if board[i] not in ("X", "O")]
    return random.choice(empty)

def get_player_name(player_num, symbol):
    name = input(f"Enter name for Player {player_num} ({symbol}): ").strip()
    return name if name else f"Player {player_num}"

def play():
    print("*****TIC TAC TOE*****")

    while True:
        try:
            num_players = int(input("How many players? (1 or 2): "))
            if num_players in (1, 2):
                break
            print("Enter 1 or 2 only.")
        except ValueError:
            print("Enter 1 or 2 only.")

    if num_players == 2:
        p1 = get_player_name(1, "X")
        p2 = get_player_name(2, "O")
        vs_bot = False
    else:
        p1 = get_player_name(1, "X")
        p2 = "Bot"
        vs_bot = True
        print(f"\nOkay {p1}, you'll play against Bot!")

    players = {"X": p1, "O": p2}
    board = [str(i+1) for i in range(9)]
    current = "X"

    print(f"\n{p1} (X)  vs  {p2} (O)")
    print("Positions:")
    print_board(board)

    for turn in range(9):
        if vs_bot and current == "O":
            print(f"{p2} (Bot) is thinking...")
            move = bot_move(board)
            print(f"Bot chose position {move+1}")
        else:
            while True:
                try:
                    move = int(input(f"{players[current]}'s turn ({current}) — enter position (1-9): ")) - 1
                    if 0 <= move <= 8 and board[move] not in ("X", "O"):
                        break
                    print("Invalid move. Try again.")
                except ValueError:
                    print("Enter a number 1-9.")

        board[move] = current
        print_board(board)

        if check_winner(board, current):
            if vs_bot and current == "O":
                print("Bot wins! Better luck next time.")
            else:
                print(f"Congratulations {players[current]} ({current}) wins!")
            return

        current = "O" if current == "X" else "X"

    print("Match draw!!!!!")

play()