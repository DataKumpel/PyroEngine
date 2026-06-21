import pyray as pr
from enum import Enum, auto
from utility import setup_logging


class GameState(Enum):
    MAIN_MENU = auto()
    EXPLORATION = auto()
    COMBAT = auto()
    MENU = auto()
    GAME_OVER = auto()


class PyroEngineApp:
    def __init__(self, win_width: int, win_height: int):
        # TODO: Which variables need to be set from outside?
        self.win_width = win_width
        self.win_height = win_height
        self.logger = setup_logging()
        self.state = GameState.MAIN_MENU
        self.limit_framerate = True
        self.fps_limit = 60

    def run(self):
        self.logger.info("Creating raylib window...")
        pr.init_window(self.win_width, self.win_height, "PYRO ENGINE v0.0.1")

        # TODO: Own function/method?
        if self.limit_framerate:
            self.logger.info(f"Limiting framerate to {self.fps_limit} fps...")
            pr.set_target_fps(self.fps_limit)
        else:
            self.logger.info("Framerate uncapped...")

        self.logger.info("Entering window loop...")
        while not pr.window_should_close():
            match self.state:
                case GameState.COMBAT     : self.handle_combat()
                case GameState.EXPLORATION: self.handle_exploration()
                case GameState.GAME_OVER  : self.handle_game_over()
                case GameState.MAIN_MENU  : self.handle_main_menu()
                case GameState.MENU       : self.handle_menu()
                case _: self.logger.warning(f"Undefined game-state ({self.state.name!r})!")

        self.logger.info("Closing raylib window...")
        pr.close_window()

        self.logger.info("Engine shutdown complete!")
    
    def handle_main_menu(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_text("Hello from PYRO ENGINE", 50, self.win_height // 2, 20, pr.RED)
        pr.end_drawing()

    def handle_combat(self):
        ...
    
    def handle_exploration(self):
        ...

    def handle_game_over(self):
        ...
    
    def handle_menu(self):
        ...
