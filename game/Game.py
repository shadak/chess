from .Piece import Pawn

class Game:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)] 
        for i in range(8):
            for j in range(8):
                if i == 0:
                    self.board[i][j] = Pawn([j, i], 'white')
                elif i == 8:
                    self.board[i][j] = Pawn([j, i], 'black')

    def getBoard(self):
        boardString = ''
        for row in self.board:
            for cell in row:
                boardString += 'x'
            boardString += '\n'
        return boardString


   
