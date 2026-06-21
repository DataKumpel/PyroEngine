import pyray as pr
from .utility import center_text


class MainMenu:
    def __init__(self, win_width: int, win_height: int):
        self.should_close = False
        self.win_width = win_width
        self.win_height = win_height

    def run(self):
        while not self.should_close:
            self.update()
            self.handle_input()

    def update(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        # text = "Hello from PYRO ENGINE"
        # text_x, text_y = center_text(text, self.win_width, self.win_height, 20)
        # pr.draw_text(text, text_x, text_y, 20, pr.RED)
        if(pr.gui_button([10, 10, 120, 30], "Test")):
            self.should_close = True
        pr.end_drawing()

    def handle_input(self):
        if pr.is_key_pressed(pr.KeyboardKey.KEY_ESCAPE):
            self.should_close = True
