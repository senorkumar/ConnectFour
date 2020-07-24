import numpy as np
from Piece import Piece
from PlacementState import PlacementState

class ConnectFour:
    def __init__(self):
        
        self.COLS = 7
        self.ROWS = 6
        self.MIN_COL_INDEX = 0
        self.MAX_COL_INDEX = self.COLS-1
        self.MIN_COL_CAPACITY = 0
        self.MAX_COL_CAPACITY = 6
        self.WINNING_LENGTH = 4

        self.board = np.full((self.ROWS,self.COLS),Piece.EMPTY)
        self.col_capacity = np.zeros(self.COLS, dtype = 'I' )
        

    
    #getter for the np array that represents the board
    def get_board(self):
        return self.board
    
    def get_capacity(self):
        return self.col_capacity

    def get_piece(self,row,col):
        return self.board[row][col]

    def board_to_string(self):
        board_string = ""
        for row in reversed(range(self.ROWS)):
            row_string = ""
            for col in range(self.COLS):
                row_string = row_string + self.board[row][col].value
            board_string = board_string + "\n" + row_string
        return board_string
 
    def place_piece(self, col, piece):
        if col < self.MIN_COL_INDEX or col > self.MAX_COL_INDEX:
            return (PlacementState.fail,(-1,-1))
        elif self.col_capacity[col] == self.MAX_COL_CAPACITY:
            return (PlacementState.fail, (-1,-1))
        else: #place piece
            row = self.col_capacity[col]
            self.col_capacity[col] += 1
          
            self.board[row][col] = piece
            return (PlacementState.success, (row,col))
    
    def check_for_winner(self, row, col):
        
        if self.is_horizontal_win(row,col) or self.is_vertical_win(row,col) or self.is_left_diagonal_win(row,col) or self.is_right_diagonal_win(row,col):
            return True
        else:
            return False
    
    def is_horizontal_win(self, row, col):
        for i in range(4):
            piece_list = [(row-3 +i, col),(row-2 +i,col),(row-1 + i, col),(row + i, col)]
            if self.check_in_a_row(piece_list):
                return True
        return False

    def is_vertical_win(self, row, col):
        for i in range(4):
            piece_list = [(row,col-3+i),(row,col-2+i),(row,col-1+i),(row,col+i)]
            if self.check_in_a_row(piece_list):
                return True
        return False

    def is_right_diagonal_win(self,row, col):
        for i in range(4):
            piece_list = [(row-3+i,col-3+i),(row-2+i,col-2+i),(row-1+i,col-1+i),(row+i,col+i)]
            if self.check_in_a_row(piece_list):
                return True
        return False
    
    def is_left_diagonal_win(self,row, col):
        for i in range(4):
            piece_list = [(row+3-i,col-3+i),(row+2-i,col-2+i),(row+1-i,col-1+i),(row-i,col+i)]
            if self.check_in_a_row(piece_list):
                return True
        return False

    def check_in_a_row(self,piece_list):
        #check that all pieces are valid
        for coords in piece_list:
            if coords[0] >= 0 and coords[0]<self.ROWS and coords[1] >= 0 and coords[1] <self.COLS:
                pass #piece if good
            else:
                return False
        piece_set = set()
        for piece in piece_list:
            piece_set.add(self.get_piece(piece[0],piece[1]).value)
        
        return len(piece_set) ==1
    
    #only to be called after checking for a win as the board can be full with a winning position
    def is_tie(self):
        for index in self.col_capacity:
            if index == self.MAX_COL_CAPACITY:
                pass
            else:
                return False
        return True


        

            


        
            

     
    


    


    


    










