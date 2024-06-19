def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def check_tie(board):
    for row in board:
        if any(s == ' ' for s in row):
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get user input
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[row][col] != ' ':
                print("Cell already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers between 0 and 2.")
            continue
        
        # Place the player's mark on the board
        board[row][col] = current_player
        
        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
