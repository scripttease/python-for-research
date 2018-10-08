import numpy as np

# Exercise 1
# Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board, attempting to make a row, column, or diagonal of three with their mark. In this homework, we will use the tools we've covered in the past two weeks to create a tic-tac-toe simulator and evaluate basic winning strategies. In the following 13 exercises, we will learn to create a tic-tac-toe board, place markers on the board, evaluate if either player has won, and use this to simulate two basic strategies.

# For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. Make a function create_board() that creates such a board, with values of integers 0
def create_board():
    return np.zeros((3,3))

# Call create_board(), and store this as board
board = create_board()

# Create a function place(board, player, position), where:
#player is the current player (an integer 1 or 2)
#position a tuple of length 2 specifying a desired location to place their marker.
#Your function should only allow the current player to place a marker on the board (change the board position to their number) if that position is empty (zero).

def place(board, player, position):
    if board[position[0],position[1]] == 0.0:
        board[position[0], position[1]] = player

#Use create_board() to store a board as board, and use place to have Player 1 place a marker on location (0, 0).

board = create_board()
def place(board, player, position):
    if board[position[0],position[1]] == 0.0:
        board[position[0], position[1]] = player
        
place(board, 1, (0,0))

#Create a function possibilities(board) that returns a list of all positions (tuples) on the board that are not occupied (0). (Hint: numpy.where is a handy function that returns a list of indices that meet a condition.)

#board is already defined from previous exercises. Call possibilities(board) to see what it returns!

def possibilities(board):
    list_tuple_possibilities = []
    ltp = []
    poss_indicies_array = np.where(board == 0)
    pia = np.where(board == 0)
    for i in pia[0]:
        n = (pia[0][0], pia[0][i])
        ltp.append(n)
    return ltp
    
possibilities(board)

#Write a function random_place(board, player) that places a marker for the current player at random among all the available positions (those currently set to 0).
#Find possible placements with possibilities(board).
#Select one possible placement at random using random.choice(selection).
#board is already defined from previous exercises. Call random_place(board, player) to place a random marker for Player 2, and store this as board to update its value.

def random_place(board, player):
    # possible positions
    pp = possibilities(board)
    # a random poss position tuple
    r = random.choice(pp)
    # selects board spot using tuple
    rX = r[0]
    rY = r[1]
    # assigns it to player
    board[rX][rY] = player
    return board

board = random_place(board, 2)

#board is already given. Call random_place(board, player) to place three pieces each on board for players 1 and 2.
#Print board to see your result.
board = create_board()
random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)

print(board)

#Make a function row_win(board, player) that takes the player (integer), and determines if any row consists of only their marker. Have it return True of this condition is met, and False otherwise.
#board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.

import numpy as np

def row_win(board, player):
    row_sum = np.sum(board, axis=1)
    col_sum = np.sum(board, axis=0)
    row_same = np.all(board, axis=1)
    col_same = np.all(board, axis=0)
    p = player*3
    for i in range(3):
        if row_sum[i] == p and row_same[i] == True:
            return True
        elif col_sum[i] == p and col_same[i] == True:
            return True
        else:
            return False

row_win(board, 1)
# note my above answer does row win and col win i think

#Create a similar function col_win(board, player) that takes the player (integer), and determines if any column consists of only their marker. Have it return True if this condition is met, and False otherwise.
#board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.

#yep. col_win works exactly as above.

#Finally, create a function diag_win(board, player) that tests if either diagonal of the board consists of only their marker. Have it return True if this condition is met, and False otherwise.
#board is already defined from previous exercises. Call diag_win to check if Player 1 has a complete diagonal.

def diag_win(board, player):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] + board[1][1] + board[2][2] == player*3:
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] + board[1][1] + board[2][0] == player*3:
        return True
    else:
        return False
        
diag_win(board, 1)
#Create a function evaluate(board) that uses row_win, col_win, and diag_win functions for both players. If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
#board is already defined from previous exercises. Call evaluate to see if either player has won the game yet.

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply. 
        if row_win or col_win or diag_win:
            winner = player
		# If so, store `player` as `winner`.
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

## nb I ma not sure that even though this seems to work, it might be wrong because doesnt seem to work with this board
array([[2, 2, 1],
       [0, 1, 0],
       [0, 1, 2]])
#create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises. Create a function play_game() that: Creates a board.
#Alternates taking turns between two players (beginning with Player 1), placing a marker during each turn.
#Evaluates the board for a winner after each placement.
#Continues the game until one player wins (returning 1 or 2 to reflect the winning player), or the game is a draw (returning -1).
#Call play_game once.

def take_turn(board, player):
    if evaluate(board) == 0:
        random_place(board, player)
        
def play_game():
    board = create_board()
    winner = evaluate(board)
    while evaluate(board) == 0:
        for player in [1,2]:
            take_turn(board, player)
            evaluate(board)
    return evaluate(board)
    
play_game()

#Use the play_game() function to play 1,000 random games, where Player 1 always goes first.
#Import and use the time library to call the time() function both before and after playing all 1,000 games.
#Store these times as start and stop, respectively.
#Subtract them to evaluate how long it takes to play 1,000 games, and print your answer.
import time
start = time.clock()
for i in range(1000):
    play_game()
stop = time.clock()
print(stop-start)
#The library matplotlib.pyplot has already been stored as plt. Use plt.hist() and plt.show() to plot a histogram of the results.
#Does Player 1 win more than Player 2?
#Does either player win more than each player draws?
import time
start = time.clock()
for i in range(1000):
    play_game()
stop = time.clock()
print(stop-start)

games = []
for i in range(1000):
    games.append(play_game())

plt.hist(games, bins=np.linspace(-1.5,5))
plt.show()

# This works FINE but the correct submission wants time.time() used which is actual time (which is probably bad code as has to be calculated adding time but anyway!
# Not player 1 usually wins because they go first... even in a rando game

#create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises. Create a function play_strategic_game(), where Player 1 always starts with the middle square, and otherwise both players place their markers randomly.
#Call play_strategic_game once.

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            if evaluate(board) == 0:
                random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game() 

#The results from Exercise 12 have been stored. Use the play_strategic_game() function to play 1,000 random games.
#Use the time libary to evaluate how long all these games takes.
#The library matplotlib.pyplot has already been stored as plt. Use plt.hist and plt.show to plot your results. Did Player 1's performance improve? Does either player win more than each player draws?

import time
start = time.time()
for i in range(1000):
    play_strategic_game()
stop = time.time()
print(stop-start)

games = []
for i in range(1000):
    games.append(play_strategic_game())

plt.hist(games, bins=np.linspace(-1.5,5))
plt.show()

# note this took 3.5 hours but I took breaks so... unsure. will be more focused for next one ideally and not doing it at midnigt while on social media...
