
import pandas as pd
import numpy as np
from core.io import from_square, to_square

class man():
    def __init__(self,color,double=False):
        self.color = color
        self.double = double
    
    def possible_moves(self,board,rank,file):
        print(rank,file)
        moves=[]
        jumps=[]

        if self.color == "black" or self.double == True:
            if rank < 7 and file < 7:
                option = board.iloc[rank+1,file+1]
                if option == 0:
                    moves.append((rank+1,file+1))
                #check for jump
                elif rank < 6 and file < 6 and option.color != self.color:
                    option = board.iloc[rank+2,file+2]
                    if option == 0:
                        jumps.append((rank+2,file+2))
                        #TODO: check for double jump
            if rank > 0 and file < 7:
                option = board.iloc[rank-1,file+1]
                if option == 0:
                    moves.append((rank-1,file+1))
                #check for jump
                elif rank > 1 and file < 6 and option.color != self.color:
                    option = board.iloc[rank-2,file+2]
                    if option == 0:
                        jumps.append((rank-2,file-2))
                        #TODO: check for double jump
        if self.color != "black" or self.double == True:
            if rank < 7 and file > 0:
                option = board.iloc[rank+1,file-1]
                if option == 0:
                    moves.append((rank+1,file-1))
                #check for jump
                elif rank < 6 and file > 1 and option.color != self.color:
                    option = board.iloc[rank+2,file-2]
                    if option == 0:
                        jumps.append((rank+2,file-2))
                        #TODO: check for double jump
            if rank > 0 and file > 0:
                option = board.iloc[rank-1,file-1]
                if option == 0:
                    moves.append((rank-1,file-1))
                #check for jump
                elif rank > 1 and file > 1 and option.color != self.color:
                    option = board.iloc[rank-2,file-2]
                    if option == 0:
                        jumps.append((rank-2,file-2))
                        #TODO: check for double jump
        if len(jumps) == 0:
            return moves
        else:
            return jumps

class game(): 
    def add_man(self,rank,file,color,double=False):
        self.board.iloc[rank,file] = man(color,double)

    def __init__(self): 
        self.board = pd.DataFrame(np.zeros(shape=(8,8),dtype=np.int8),index=[1,2,3,4,5,6,7,8],columns=['h','g','f','e','d','c','b','a'])
        for s in ['a1']:
            self.add_man(*from_square(s),"black")

    def show_board(self,color = "black"):
        if color == "black":
            print(self.board)
        else:
            print(self.board.T.iloc[::-1].T[::-1])