from player import Player
from math import *
from copy import *


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """

    def __init__(self):
        self.name = "Timo Maszewski & Niels Hendrickx"


    def getColumn(self, board):
        return maxvalue(board,5)


def h(board) :
    return 0


def minvalue(board,action,prof,alpha=-1*inf,beta=inf) :
    if prof==0 :
        return h(action)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(1,s)
        if minvalue(board,prof-1,alpha,beta)>=alpha :
            alpha=minvalue(board,prof-1,alpha,beta)
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


def maxvalue(board,action,prof,alpha=-1*inf,beta=inf) :
    if prof==0 :
        return h(action)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(-1,s)
        if maxvalue(board_bis,s,prof-1,alpha,beta)>=alpha :
            alpha=maxvalue(board_bis,s,prof-1,alpha,beta)
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


