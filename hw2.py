# hw2.py by Mohammed

import numpy as np
import random 
random.seed(1)

# creates a 3x3 board
def create_board():
    return np.zeros((3, 3), dtype=int)
    
# place a players marker on the board
def place(board, player, position):
    if board[position] == 0:
        board[position] = player

#initialize the board
board = create_board()        
place(board, 1, (0,0))
print(board)

# function finds available positions on the board
def possibilities(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row, col] == 0]

# function places marker at a random available position
def random_place(board, player):
    placement = possibilities(board)
    if placement :
        position = random.choice(placement)
        board[position] = player

#initialize the board
board = create_board()

# this simulates 3 round of tic-tac-toe
for i  in range(3):
    random_place(board, 1)
    random_place(board, 2)

print(board)

# function for row match
def row_win(board, player):
    for row in board:
        if np.all(row == player): # checks if element in the row matches player
            return True
        return False
        
player1_row_win = row_win(board, 1)
print(player1_row_win)

# function for col match
def col_win(board, player):
    for col in board:
        if np.all(board[:, col] == player): # board[:, col] iterate column
            return True
    return False

player1_col_win = col_win(board, 1)
print(player1_col_win)

# function for diag match
def diag_win(board, player):
    # checks top left to bottom right
    if np.all(np.diag(board) == player): 
        return True
    # checks top right to bottom left
    if np.all(np.diag(np.fliplr(board)) == player): 
        return True
    
    return False

board[1,1] = 2
player2_diag_win = diag_win(board, 2)
print(player2_diag_win)

# function for finding win
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            pass
        
    if np.all(board != 0) and winner == 0:
        winner = -1
        
    return winner
    
result = evaluate(board)
print("\nGame Result:")
if result == 1:
    print("Player 1 wins!")
elif result == 2:
    print("Player 2 wins!")
elif result == -1:
    print("It's a draw!")
else:
    print("The game is still ongoing.")


# function to simulate entire games
def play_game():
    board = create_board()
    current_player = 1
    while True:
        random_place(board, current_player)  # Place a marker for the current player
        result = evaluate(board)  # Evaluate the board
        if result != 0:  # Check if the game is over
            return result  # Return the result (1, 2, or -1)
        current_player = 3 - current_player  # Switch players (1 -> 2, 2 -> 1)


results = [play_game() for i in range(1000)]
player1_wins = results.count(1)   
print(player1_wins)

def play_strategic_game():
    board = create_board()
    current_player = 1

    # Player 1 always starts with the middle square
    board[1, 1] = 1

    while True:
        # Alternate players and place markers randomly
        random_place(board, current_player)

        result = evaluate(board)
        if result != 0:  # Game ends if there's a winner or a draw
            return result

        current_player = 3 - current_player  # Switch players (1 -> 2, 2 -> 1)
        
stratresults = [play_strategic_game() for _ in range(1000)]
player1_strat_wins = stratresults.count(1)
print(player1_strat_wins)
