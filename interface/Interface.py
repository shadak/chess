from enum import Enum
from game import Game
import curses

class State(Enum):
    MAIN_MENU = 0
    NET_MENU = 1
    GAME_YOUR_TURN = 2
    GAME_THEIR_TURN = 3


class Interface:
    def __init__(self, stdscr):


        

