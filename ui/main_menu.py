import pyray as pr
from .utility import center_text, layout_vertical, layout_horizontal
from logging import Logger
from enum import Enum, auto


class MainMenuAction(Enum):
    NEW_GAME = auto()
    LOAD_GAME = auto()
    EXIT = auto()
    NONE = auto()


class MainMenu:
    def __init__(self, win_width: int, win_height: int, logger: Logger):
        self.should_close = False
        self.win_width = win_width
        self.win_height = win_height
        self.logger = logger
        self.layout = layout_horizontal(pr.Rectangle(0, 0, win_width, win_height), 3)
        self.layout = layout_vertical(self.layout[1], 6, 25)
        self.action = MainMenuAction.NONE

    def update(self):
        self.action = MainMenuAction.NONE
        self.draw()
        self.handle_input()
        return self.action

    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        title_pos_x, title_pos_y = center_text("DARKFIELD", self.layout[1].width, self.layout[1].height, 34)
        pr.draw_text("DARKFIELD", int(self.layout[1].x + title_pos_x), int(self.layout[1].y + title_pos_y), 34, pr.BLUE)
        
        if(pr.gui_button(self.layout[2], "New Game")):
            self.action = MainMenuAction.NEW_GAME
        
        if(pr.gui_button(self.layout[3], "Load Game")):
            self.action = MainMenuAction.LOAD_GAME
        
        if(pr.gui_button(self.layout[4], "Exit")):
            self.action = MainMenuAction.EXIT
            self.should_close = True

        pr.end_drawing()

    def handle_input(self):
        if pr.is_key_pressed(pr.KeyboardKey.KEY_ESCAPE):
            self.should_close = True
