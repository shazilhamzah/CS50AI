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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==X:
                countX+=1
            elif board[i][j]==O:
                countO+=1
            else:
                continue
    if(countO==countX):
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    tupleToReturn = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                tupleToReturn.add((i,j))
    return tupleToReturn
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        print(action)
        raise Exception("Invlid action")
    row,col = action
    newBoard = copy.deepcopy(board)
    newBoard[row][col] = player(board);
    return newBoard
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0,3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            return board[i][0]
        
    for j in range(0,3):
        if board[0][j]==board[1][j] and board[1][j]==board[2][j]:
            return board[0][j]
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[1][1]
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]
    
    return EMPTY

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X or winner(board)==O:
        return True
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                return False;
    return True;
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    whoWon = winner(board)
    if whoWon==X:
        return 1
    elif whoWon==O:
        return -1
    else:
        return 0

    raise NotImplementedError


def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,minValue(result(board,action)))
    return v

def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board) 
    for action in actions(board):
        v = min(v,maxValue(result(board,action)))
    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    whosPlaying = player(board)
    if(whosPlaying==X):
        bestValue = -math.inf
        bestAction = None
        for action in actions(board):
            v = minValue(result(board,action))
            if v>bestValue:
                bestValue = v
                bestAction = action
        return bestAction
    
    elif(whosPlaying==O):
        bestValue = math.inf
        bestAction = None
        for action in actions(board):
            v = maxValue(result(board,action))
            if v<bestValue:
                bestValue = v
                bestAction = action
        return bestAction
    
    
    raise NotImplementedError
