class Piece:
    def __init__(self, position, color):
        self.x, self.y = position
        self.color = color

    def makeMove(position):
        self.x, self.y = position

class Pawn(Piece):
    
    def getMoves():
        moves = [[self.x-1, self.y+1], [self.x, self.y+1], [self.x+1, self.y+1]]
        return moves

 
