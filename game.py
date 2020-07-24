from connect_four import ConnectFour
from gameState import gameState
from playerType import playerType
from Piece import Piece
from PlacementState import PlacementState
from gameResult import gameResult
#X goes first always
class Game:
    def __init__(self, playerXType, playerOType):
        self.game = ConnectFour()
        self.state = gameState.X
        self.playerXType = playerXType
        self.playerOType = playerOType
        self.result = None
        if self.playerXType == playerType.Human and self.playerOType == playerType.Human:
            self.runHumanGame()   

    def get_result(self):
        return self.result
    
    def runHumanGame(self):
        #human vs human game
        if(self.playerXType == playerType.Human and self.playerOType == playerType.Human):
            while self.state is not gameState.Gameover:
                print(self.game.board_to_string())
                placement_state = PlacementState.fail
                (row,col) = (-1,-1)
                if self.state == gameState.X:
                    while placement_state is not PlacementState.success:
                        colInput = int(input("It is X's turn. Please type which column you would like your piece to go in:"))
                        (placement_state, (row,col)) = self.game.place_piece(colInput,Piece.X)
                    if self.game.check_for_winner(row,col):
                        self.state = gameState.Gameover
                        self.result = gameResult.X
                        print(self.state.value + "wins!")
                    elif self.game.is_tie():
                        self.state = gameState.Gameover
                        self.result = gameResult.Tie
                        print("the game has ended in a tie!")
                    self.state = gameState.O


                elif self.state == gameState.O:
                    while placement_state is not PlacementState.success:
                        colInput = int(input("It is O's turn. Please type which column you would like your piece to go in:"))
                        (placement_state, (row,col)) = self.game.place_piece(colInput,Piece.O)
                    if self.game.check_for_winner(row,col):
                        self.state = gameState.Gameover
                        self.result = gameResult.O
                        print(self.state.value + "wins!")
                    elif self.game.is_tie():
                        self.state = gameState.Gameover
                        self.result = gameResult.Tie
                        print("the game has ended in a tie!")
                    self.state = gameState.X
                
                
            

        

                


                



       
    


