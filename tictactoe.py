def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check if there's a winner
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6],  
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

def is_draw(board):
    return all(spot != " " for spot in board)

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'\n")

    board = [" "] * 9
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")
        
        try:
            move = int(input("Enter a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
