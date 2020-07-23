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
            return (PlacementState.fail,"column invalid")
        elif self.col_capacity[col] == self.MAX_COL_CAPACITY:
            return (PlacementState.fail, "column is full")
        else: #place piece
            row = self.col_capacity[col]
            self.col_capacity[col] += 1
            print((row,col))
            self.board[row][col] = piece
            return PlacementState.success
    def check_for_winner(self):







