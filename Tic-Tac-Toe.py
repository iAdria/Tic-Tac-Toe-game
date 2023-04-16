board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

def print_board():
    print("   0  1  2")
    for i in range(3):
        row_str = f"{i}  "
        for j in range(3):
            row_str += f"{board[i][j]}  "
        print(row_str)

def is_game_over():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '-':
            return True, board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return True, board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True, board[0][2]
    if all(all(row != '-' for row in row_lst) for row_lst in board):
        return True, "Tie"
    return False, None

def play_game():
    print("Let's play Tic Tac Toe!")
    player = 'X'
    while True:
        print_board()
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))
        if board[row][col] == '-':
            board[row][col] = player
            game_over, winner = is_game_over()
            if game_over:
                if winner == "Tie":
                    print_board()
                    print("It's a tie!")
                else:
                    print_board()
                    print(f"Congratulations, Player {winner} wins!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")

play_game()
