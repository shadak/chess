class Piece:
    def __init__(self, position, player):
        self.x, self.y = position
        self.player = player

    def makeMove(position):
        self.x, self.y = position

    def __string__(self):
        return 'Test'
class Pawn(Piece):
    def checkMove(self):
        return False

class Rook(Piece):
    def checkMove(self):
        return False

class Knight(Piece):
    def checkMove(self):
        return False

class Bishop(Piece):
    def checkMove(self):
        return False

class King(Piece):
    def checkMove(self):
        return False

class Queen(Piece):
    def checkMove(self):
        return False
