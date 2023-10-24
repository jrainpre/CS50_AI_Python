"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



"""The player function should take a board state as input, and return which player’s turn it is (either X or O).
In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over)."""
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    countX = 0
    countO = 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X
    

"""Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
Possible moves are any cells on the board that do not already have an X or an O in them.
Any return value is acceptable if a terminal board is provided as input."""

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions



"""The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
If action is not a valid action for the board, your program should raise an exception.
The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes."""

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copiedBoard = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("Invalid action")
    copiedBoard[action[0]][action[1]] = player(board)
    return copiedBoard
"""The winner function should accept a board as input, and return the winner of the board if there is one.
If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None."""
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return board [2][0]
    return None


"""If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
Otherwise, the function should return False if the game is still in progress."""
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        _, action = maxValue(board)
        return action
    if player(board) == O:
        _, action = minValue(board)
        return action
        
    

def maxValue(board):
    v = float('-inf')
    return_action = None
    if terminal(board):
        return (utility(board)), None
    for action in actions(board):
        old_v = v
        temp_v, _ = minValue(result(board, action))
        if temp_v > v:
            v = temp_v
            return_action = action
    return v, return_action

    
def minValue(board):
    v = float('inf')
    return_action = None
    if terminal(board):
        return (utility(board)), None
    for action in actions(board):
        old_v = v
        temp_v, _ = maxValue(result(board, action))
        if temp_v < v:
            v = temp_v
            return_action = action
    return v, return_action