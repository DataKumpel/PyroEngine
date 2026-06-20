import pyray as pr
from enum import Enum, auto
import logging


WIN_WIDTH = 800
WIN_HEIGHT = 450


class GameState(Enum):
    MAIN_MENU = auto()
    EXPLORATION = auto()
    COMBAT = auto()
    MENU = auto()
    GAME_OVER = auto()


class PyroEngineApp:
    def __init__(self):
        self.logger = setup_logging()
        self.state = GameState.MAIN_MENU

    def run(self):
        self.logger.info("Creating raylib window...")
        pr.init_window(WIN_WIDTH, WIN_HEIGHT, "PYRO ENGINE v0.0.1")

        self.logger.info("Entering window loop...")
        while not pr.window_should_close():
            match self.state:
                case GameState.COMBAT: self.handle_combat()
                case GameState.EXPLORATION: self.handle_exploration()
                case GameState.GAME_OVER: self.handle_game_over()
                case GameState.MAIN_MENU: self.handle_main_menu()
                case GameState.MENU: self.handle_menu()
                case _: self.logger.warning(f"Undefined game-state ({self.state.name!r})!")

        self.logger.info("Closing raylib window...")
        pr.close_window()

        self.logger.info("Engine shutdown complete!")
    
    def handle_main_menu(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_text("Hello from PYRO ENGINE", 50, WIN_HEIGHT // 2, 20, pr.RED)
        pr.end_drawing()

    def handle_combat(self):
        ...
    
    def handle_exploration(self):
        ...

    def handle_game_over(self):
        ...
    
    def handle_menu(self):
        ...



def setup_logging() -> logging.Logger:
    pr.set_trace_log_level(pr.TraceLogLevel.LOG_ERROR)
    logger = logging.getLogger("PYRO_ENGINE")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_fmt = logging.Formatter("[{levelname}] {name}: {message}", style="{")
    console_handler.setFormatter(console_fmt)
    logger.addHandler(console_handler)
    return logger


def main():
    pyro = PyroEngineApp()
    pyro.run()


if __name__ == "__main__":
    main()
