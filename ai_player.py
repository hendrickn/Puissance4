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
        return maxvalue(self,board,2)[1]



def h(self,board) :
    return uniform(-1,1)

def minvalue(self,board,prof,alpha=-2,beta=2) :
    if prof==0 :
        return h(self,board)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(-1,s)
        if maxvalue(self,board_bis,prof-1,alpha,beta)[0]>=alpha :
            alpha=maxvalue(self,board_bis,prof-1,alpha,beta)[0]
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


def maxvalue(self,board,prof,alpha=-1*inf,beta=inf) :
    if prof==0 :
        return h(self,board)
    for s in board.getPossibleColumns() :
        board_bis=deepcopy(board)
        board_bis.play(1,s)
        if minvalue(self,board_bis,prof-1,alpha,beta)[0]>=alpha :
            alpha=minvalue(self,board_bis,prof-1,alpha,beta)[0]
            choice=s
        if alpha>=beta :
            return beta
    return alpha,choice


