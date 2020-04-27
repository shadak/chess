import sys
from curses import wrapper
from game import Game 

def drawBoard(stdscr, board):
    stdscr.addstr(board)

def main(stdscr):
    game = Game()
    stdscr.clear()
    board = game.getBoard()
    drawBoard(stdscr, board)
    while True:
        stdscr.refresh() 
        key = stdscr.getch()
        stdscr.addstr(key)


wrapper(main)

if __name__ == '__main__':
    sys.exit(main())


