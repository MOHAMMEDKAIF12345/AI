# Step 1: Initialize the Game Board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Step 2: Display the Game Board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Step 3: Player Move
def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("The cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two integers between 0 and 2. Try again.")

# Step 4: Check for Win
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

# Step 5: Check for Draw
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Step 6: Main Game Loop
def tic_tac_toe():
    board = initialize_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Run the Tic Tac Toe game
tic_tac_toe()
