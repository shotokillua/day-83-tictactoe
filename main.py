# CREATE BOARD
board = [' ' for _ in range(9)]

# YOU CAN ALSO CREATE A BOARD THIS WAY
# board = [[" ", " ", " "],
#          [" ", " ", " "],
#          [" ", " ", " "]]

# DISPLAY THE BOARD
def display_board(board):
    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("     |     |     ")
    print("----------------")
    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("     |     |     ")
    print("----------------")
    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("     |     |     ")

# GET PLAYER INPUT
def make_move(board, position, character):
    board[position] = character

# CHECK FOR A WINNER
def check_winner(board, player):
    # check row
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # check column
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True

    return False

# CHECK FOR A TIE
def check_tie(board):
    return ' ' not in board # this will return true if there are no empty spots left on the board and false if there are still spots left to fill
                            # we do not need to include the check for winning in this function because we will call that function first to check for a winner


# CREATE MAIN GAME LOOP
def play_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False
    while not game_over:
        display_board(board)
        selected_position = int(input(f"Player {current_player}, select a position (0-8): "))

        if board[selected_position] == " ": # this is to validate the position is unoccupied
            make_move(board, selected_position, current_player)
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif check_tie(board):
                display_board(board)
                print(f"It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X' # this means that if it's player X's turn,
                                                                       # swap to player O, and if the current player isn't X then it becomes player X's turn
        else:
            print("Position is occupied, try again.")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == 'Y':
        play_game()

play_game()