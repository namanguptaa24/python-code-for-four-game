# Define constants
ROWS = 6
COLS = 7

# Initialize the game board
def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Display the game board
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (COLS * 2 - 1))

# Check if a player has won
def check_win(board, player):
    # Check horizontal
    for row in board:
        for col in range(COLS - 3):
            if all(cell == player for cell in row[col:col+4]):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row+i][col] == player for i in range(4)):
                return True

    # Check diagonals (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row-i][col+i] == player for i in range(4)):
                return True

    # Check diagonals (bottom-right to top-left)
    for row in range(3, ROWS):
        for col in range(3, COLS):
            if all(board[row-i][col-i] == player for i in range(4)):
                return True

    return False

# Check if the board is full (tie)
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Get a valid column choice from the player
def get_player_move(board):
    while True:
        try:
            col = int(input("Enter your move (1-7): ")) - 1
            if 0 <= col < COLS and board[0][col] == ' ':
                return col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 7.")

# Main game loop
def main():
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")

        col = get_player_move(board)

        # Place the player's piece in the chosen column
        for row in range(ROWS - 1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = current_player
                break

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
