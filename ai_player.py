from player import Player
from math import *
from copy import *
from random import *


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """

    def __init__(self):
       super().__init__()
       self.name = "Timo Maszewski & Niels Hendrickx"



    def getColumn(self, board):
        return maxvalue(board,5)[1]


def h(board,action) :
    return uniform(-1,1)


def minvalue(board,prof,alpha=-2,beta=2) :
    if prof==0 :
        return h(board)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(1,s)
        if minvalue(board_bis,prof-1,alpha,beta)>=alpha :
            alpha=minvalue(board_bis,prof-1,alpha,beta)
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


def maxvalue(board,prof,alpha=-1*inf,beta=inf) :
    if prof==0 :
        return h(board)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(-1,s)
        if maxvalue(board_bis,prof-1,alpha,beta)>=alpha :
            alpha=maxvalue(board_bis,prof-1,alpha,beta)
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


