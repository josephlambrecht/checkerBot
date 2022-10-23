
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
                        jumps.append(to_square(rank-2,file+2))
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

    def options(self,board,rank,file):
        moves,jumps = self.possible_moves(board,rank,file)
        #check for double jumps
        prev_list = []
        current_list=jumps
        while(prev_list!=current_list):
            prev_list = current_list
            for move in prev_list:
                jump_game = game(board.copy())
                jump_game.make_move(move)
                jumps = self.possible_moves(jump_game.board,*from_square(move.split('x')[-1]))[1]
                if len(jumps) > 0: prev_list.remove(move)
                for j in jumps:
                    current_list.append(move+'x'+j)
        jumps = current_list
        return moves,jumps

class game(): 
    def add_man(self,rank,file,color,double=False):
        self.board.iloc[rank,file] = man(color,double)
    
    def remove_man(self,rank,file):
        self.board.iloc[rank,file] = 0

    def __init__(self,board=pd.DataFrame(np.zeros(shape=(8,8),dtype=int),index=[1,2,3,4,5,6,7,8],columns=['h','g','f','e','d','c','b','a'])): 
        self.board = board

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
        moves = []
        jumps = []
        for rank in range(8):
            for file in range(8):
                square = self.board.iloc[rank,file]
                if type(square) != int:
                    if square.color == color:
                        m, j = square.options(self.board,rank,file)
                        # if len(m) != 0:
                        #     moves[to_square(rank,file)] = m
                        # if len(j) != 0:
                        #     jumps[to_square(rank,file)] = j
                        for move in m:
                            moves.append(to_square(rank,file)+'-'+move)
                        for jump in j:
                            jumps.append(to_square(rank,file)+'x'+jump)
        if len(jumps) != 0:
            return jumps
        else: return moves

    def make_move(self,move):
        promote = False
        if move[-1] == "^":
            move = move[:-1]
            promote = True
        if "-" in move:
            steps = move.split("-")
            color = self.board.iloc[from_square(steps[0])].color
            double = self.board.iloc[from_square(steps[0])].double
            self.remove_man(*from_square(steps[0]))
            self.add_man(*from_square(steps[1]),color,(double or promote))
        elif "x" in move:
            steps = move.split("x")
            color = self.board.iloc[from_square(steps[0])].color
            double = self.board.iloc[from_square(steps[0])].double
            for i in range(1,len(steps)):
                #find jumped square and remove its piece
                r0,f0 = from_square(steps[i-1])
                r2,f2 = from_square(steps[i])
                r1 = int((r0+r2)/2)
                f1 = int((f0+f2)/2)
                self.remove_man(r1,f1)
            #remove starting piece and place at end
            self.remove_man(*from_square(steps[0]))
            self.add_man(*from_square(steps[-1]),color,(double or promote))