board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def display_board():
    print('-' * 5)
    for row in board:
        print('|'.join(row))
        print('-' * 5)
#display_board()
def get_player_move():
    while True:
        try:
            row = int(input("Enter the row number (0-2): "))
            column = int(input("Enter the column number (0-2): "))
            if 0 <= row <= 2 and 0 <= column <= 2:
                return row, column
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def update_board(row, column, player):
    if board[row][column] == ' ':
        board[row][column] = player
        return True
    else:
        return False

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def play_game():
    current_player = 'X'
    while True:
        display_board()
        print(f"Player {current_player}'s turn.")
        row, column = get_player_move()
        if update_board(row, column, current_player):
            winner = check_winner()
            if winner:
                display_board()
                print(f"Player {winner} wins!")
                break
            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                display_board()
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already occupied. Try again.")

play_game()