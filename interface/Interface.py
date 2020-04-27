from enum import Enum
import curses

class State(Enum):
    MAIN_MENU = 0
    NET_MENU = 1
    GAME_YOUR_TURN = 2
    GAME_THEIR_TURN = 3


class Interface:
    def __init__(self, stdscr):
        self.state = State.MAIN_MENU
        self.screen = stdscr
    
    def run(self):
        while(True):
            if self.state == State.MAIN_MENU:
                self.render_main_menu()
            elif self.state == State.NET_MENU:
                self.render_network_menu()
            elif self.state == State.GAME_YOUR_TURN:
                self.render_game()
            elif self.state == State.GAME_THEIR_TURN:
                self.render_game()

    def render_main_menu(self):
        menu_options = ["Network Game", "Exit"]
        key = -1
        cursor_pos = 0
        screen = self.screen
        while(key != '\n'):
            if key == 'KEY_DOWN':
                cursor_pos = 1
            elif key == 'KEY_UP':
                cursor_pos = 0
            screen.addstr(menu_options[0], curses.A_REVERSE if cursor_pos == 0 else 0)
            screen.addstr(menu_options[1], curses.A_REVERSE if cursor_pos == 1 else 0)
            screen.refresh() 
            key = screen.getkey() 
        screen.clear()
        



    def render_network_menu(self):
        return
    def render_game(self):
        return
        
