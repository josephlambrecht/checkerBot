
import pandas as pd
import numpy as np
from core.io import from_square, to_square

class man():
    def __init__(self,color,double=False):
        self.color = color
        self.double = double
    
    def possible_moves(self,board,rank,file):
        moves=[]
        jumps=[]

        if (self.color == "black") or (self.double == True):
            if rank > 0 and file < 7:
                option = board.iloc[rank-1,file+1]
                if option == 0:
                    moves.append(to_square(rank-1,file+1))
                #check for jump
                elif rank > 1 and file < 6 and option.color != self.color:
                    option = board.iloc[rank-2,file+2]
                    if option == 0:
                        jumps.append(to_square(rank-2,file-2))
                        #TODO: check for double jump
            if rank > 0 and file > 0:
                option = board.iloc[rank-1,file-1]
                if option == 0:
                    moves.append(to_square(rank-1,file-1))
                #check for jump
                elif rank > 1 and file > 1 and option.color != self.color:
                    option = board.iloc[rank-2,file-2]
                    if option == 0:
                        jumps.append(to_square(rank-2,file-2))
                        #TODO: check for double jump


        if (self.color != "black") or (self.double == True):
            if rank < 7 and file > 0:
                option = board.iloc[rank+1,file-1]
                if option == 0:
                    moves.append(to_square(rank+1,file-1))
                #check for jump
                elif rank < 6 and file > 1 and option.color != self.color:
                    option = board.iloc[rank+2,file-2]
                    if option == 0:
                        jumps.append(to_square(rank+2,file-2))
                        #TODO: check for double jump
            if rank < 7 and file < 7:
                option = board.iloc[rank+1,file+1]
                if option == 0:
                    moves.append(to_square(rank+1,file+1))
                #check for jump
                elif rank < 6 and file < 6 and option.color != self.color:
                    option = board.iloc[rank+2,file+2]
                    if option == 0:
                        jumps.append(to_square(rank+2,file+2))
                        #TODO: check for double jump
        return moves, jumps

class game(): 
    def add_man(self,rank,file,color,double=False):
        self.board.iloc[rank,file] = man(color,double)

    def __init__(self): 
        self.board = pd.DataFrame(np.zeros(shape=(8,8),dtype=int),index=[1,2,3,4,5,6,7,8],columns=['h','g','f','e','d','c','b','a'])

    def show(self):
        output = self.board.copy()
        for rank in range(8):
            for file in range(8):
                square = self.board.iloc[rank,file]
                if type(square) != int:
                    # print(square)
                    # print(type(square),type(type(square)))
                    # print(square.color)
                    if square.color == 'black':
                        if square.double:
                            output.iloc[rank,file]='B'
                        else:
                            output.iloc[rank,file]='b'
                    elif square.color != 'black':
                        if square.double:
                            output.iloc[rank,file]='W'
                        else:
                            output.iloc[rank,file]='w'
        return output
                        

    def show_board(self,color = "black"):
        if color == "black":
            print(self.show())
        else:
            print(self.show().T.iloc[::-1].T[::-1])

    def possible_moves(self,color):
        moves = {}
        jumps = {}
        for rank in range(8):
            for file in range(8):
                square = self.board.iloc[rank,file]
                if type(square) != int:
                    if square.color == color:
                        m, j = square.possible_moves(self.board,rank,file)
                        if len(m) != 0:
                            moves[to_square(rank,file)] = m
                        if len(j) != 0:
                            jumps[to_square(rank,file)] = j
                        # for move in m:
                        #     moves.append(to_square(rank,file)+'-'+to_square(*move))
                        # for jump in j:
                        #     jumps.append(to_square(rank,file)+'x'+to_square(*jump))
        if len(jumps) != 0:
            return jumps
        else: return moves
