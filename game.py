from connect_four import ConnectFour
from gameState import gameState
from playerType import playerType
from Piece import Piece
from PlacementState import PlacementState
#X goes first always
class Game:
    def __init__(self, playerXType, playerOType):
        self.game = ConnectFour()
        self.state = gameState.X
        self.playerXType = playerXType
        self.playerOType = playerOType
        self.runGame()
    
    def runGame(self):
        #human vs human game
        if(self.playerXType == playerType.Human and self.playerOType == playerType.Human):
            while self.state is not gameState.Gameover:
                print(self.game.board_to_string())
                placement_state = PlacementState.fail
                (row,col) = (-1,-1)
                if(self.state == gameState.X):
                    while placement_state is not PlacementState.success:
                        print("It is X's turn. Please type which column you would like your piece to go in:")
                        colInput = int(input())
                        (placement_state, (row,col)) = self.game.place_piece(colInput,Piece.X)

                elif(self.state == gameState.O):
                    while placement_state is not PlacementState.success:
                        print("It is O's turn. Please type which column you would like your piece to go in:")
                        colInput = int(input())
                        (placement_state, (row,col)) = self.game.place_piece(colInput,Piece.O)
                
                if(self.game.check_for_winner(row,col)):
                    print("The game is over")
                    print(self.state.value + " wins!")
                    self.state = gameState.Gameover
                


                



       
    


