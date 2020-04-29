from collections import namedtuple
from .Piece import *

State = namedtuple("State", ["player_turn", "board"])
class Game:
    def __init__(self):
        self.state= State(player_turn = 0, board = gen_board())

def gen_board():
    empty_board = [*gen_pieces(1), *gen_pieces(2)]
    return empty_board



def gen_pieces(player):
    first_row = 1 if player == 1 else 8
    second_row = 2 if player == 1 else 7
    king_pos, queen_pos = [4, 5] if player == 1 else [5, 4]
    pawns = [Pawn([x, second_row], player) for x in range(8)]
    rooks = [Rook([x, first_row], player) for x in [1, 8]]
    knights = [Knight([x, first_row], player) for x in [2, 7]]
    bishops = [Bishop([x, first_row], player) for x in [3, 6]]
    king = King([king_pos, first_row], player)
    queen = Queen([queen_pos, first_row], player)
    return [*pawns, *rooks, *knights, *bishops, king, queen] 

  
