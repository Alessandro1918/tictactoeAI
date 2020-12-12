"""
Tic Tac Toe Player
"""

import math, copy, random


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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            cell = board[row][column]
            if cell == X:
                xCount+=1
            if cell == O:
                oCount+=1
    if (xCount > oCount):
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #actions = set()    #sets cannot be shuffled
    actions = []        # lists can
    if (terminal(board)):
        return actions

    for row in range(len(board)):
        for column in range(len(board[row])):
            if (board[row][column] == EMPTY):
                #actions.add((row, column))     # set
                actions.append((row, column))   # list
    
    random.shuffle(actions)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #If action is not a valid action for the board, program should raise an exception.
    moves = actions(board)
    if action not in moves:
        raise Exception('Not a Valid Move')

    turn = player(board)
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = turn

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #rows
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != EMPTY): return board[0][0]
    if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != EMPTY): return board[1][0]
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != EMPTY): return board[2][0]

    #columns
    if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY): return board[0][0]
    if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY): return board[0][1]
    if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY): return board[0][2]

    #diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY): return board[0][0]
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY): return board[0][2]

    #tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in range(len(board)):
            if (EMPTY in board[row]):
                return False

    return True     # tie


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    switcher = {
        X: 1,
        O: -1
    }
    return switcher.get(winner(board), 0)


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -999
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v


def minValue(board):
    if terminal(board):
        return utility(board)
    v = 999
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        bestValue = -999
        bestAction = None
        for action in actions(board):
            value = minValue(result(board, action))
            if value > bestValue:
                bestValue = value
                bestAction = action
        return bestAction

    else:
        bestValue = 999
        bestAction = None
        for action in actions(board):
            value = maxValue(result(board, action))
            if value < bestValue:
                bestValue = value
                bestAction = action
        return bestAction
        