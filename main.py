import sys
from curses import wrapper
from game import Game 
from interface import Interface

def drawBoard(stdscr, board):
    stdscr.addstr(board)

def main(stdscr):
    interface = Interface(stdscr)
    interface.start()


wrapper(main)

if __name__ == '__main__':
    sys.exit(main())


