def display_board(board):
    print("*************")
    print(f"* {board[0]} | {board[1]} | {board[2]} *")
    print("*---|---|---*")
    print(f"* {board[3]} | {board[4]} | {board[5]} *")
    print("*---|---|---*")
    print(f"* {board[6]} | {board[7]} | {board[8]} *")
    print("*************")

def player_input(player, board):
    while True:
        try:
            position = int(input(f"Player {player} ({'X' if player == 1 else 'O'}), choose your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[position] != " ":
                print("That spot is already taken. Choose another.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]            
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False

def is_board_full(board):
    return " " not in board

def play():
    board = [" "] * 9
    current_player = 1

    print("Welcome to Tic Tac Toe!")
    display_board([str(i+1) for i in range(9)])

    while True:
        display_board(board)
        position = player_input(current_player, board)
        mark = "X" if current_player == 1 else "O"
        board[position] = mark

        if check_win(board, mark):
            display_board(board)
            print(f"🎉 Player {current_player} ({mark}) wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        else:
            current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play()         
