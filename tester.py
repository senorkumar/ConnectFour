from connect_four import ConnectFour
from piece import Piece

x = ConnectFour()


x.place_piece(0,Piece.X)
x.place_piece(0,Piece.X)
x.place_piece(0,Piece.X)
x.place_piece(0,Piece.X)
x.place_piece(0,Piece.X)
x.place_piece(0,Piece.X)
x.place_piece(0,Piece.X)

print(x.board_to_string())