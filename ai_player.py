from player import Player
from math import *
from copy import *


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """

    def __init__(self):
        self.name = "Timo Maszewski & Niels Hendrickx"


    def getColumn(self, board):
        return maxvalue(board,5)[1]


def h(board,action) :
    score=0
    board_copy=deepcopy(board)
    for s in board_copy.getPossibleColumns() :
        L=board_copy.getCol(s).sort()
        F=[i for i in L if i>0]





def minvalue(board,prof,action=0,alpha=-1*inf,beta=inf) :
    if prof==0 :
        return h(action)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(1,s)
        if minvalue(board_bis,prof-1,s,alpha,beta)>=alpha :
            alpha=minvalue(board_bis,prof-1,s,alpha,beta)
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


def maxvalue(board,prof,action=0,alpha=-1*inf,beta=inf) :
    if prof==0 :
        return h(action)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(-1,s)
        if maxvalue(board_bis,prof-1,s,alpha,beta)>=alpha :
            alpha=maxvalue(board_bis,prof-1,s,alpha,beta)
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


