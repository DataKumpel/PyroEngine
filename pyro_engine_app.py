import pyray as pr
from enum import Enum, auto
from utility import setup_logging
from ui.main_menu import MainMenu, MainMenuAction
from ui.screen_effects import ScreenFader
from editor.level_editor import LevelEditor, LevelEditorAction


class GameState(Enum):
    MAIN_MENU = auto()
    EXPLORATION = auto()
    COMBAT = auto()
    MENU = auto()
    GAME_OVER = auto()
    EDITOR = auto()


class PyroEngineApp:
    def __init__(self, win_width: int, win_height: int, fullscreen=False):
        # TODO: Which variables need to be set from outside?
        self.win_width = win_width
        self.win_height = win_height
        self.fullscreen = fullscreen
        self.logger = setup_logging()
        self.state = GameState.MAIN_MENU
        self.limit_framerate = True
        self.fps_limit = 60
        self.should_close = False

        # Components:
        self.main_menu = MainMenu(self.win_width, self.win_height, self.logger)
        self.level_editor = LevelEditor(win_width, win_height)
        self.fader = ScreenFader(self.win_width, self.win_height, duration=2.0)

    def update_window_size(self):
        self.win_width = pr.get_screen_width()
        self.win_height = pr.get_screen_height()

        # Update components depending on screen size:
        self.main_menu.win_width = self.win_width
        self.main_menu.win_height = self.win_height
        self.main_menu.update_layout()

        self.fader.width = self.win_width
        self.fader.height = self.win_height

        self.logger.info(f"Fullscreen size: {self.win_width}x{self.win_height}")

    def run(self):
        self.logger.info("Creating raylib window...")
        pr.init_window(self.win_width, self.win_height, "PYRO ENGINE v0.0.1")
        
        if self.fullscreen:
            pr.toggle_fullscreen()
            self.update_window_size()
            
        # TODO: Own function/method?
        if self.limit_framerate:
            self.logger.info(f"Limiting framerate to {self.fps_limit} fps...")
            pr.set_target_fps(self.fps_limit)
        else:
            self.logger.info("Framerate uncapped...")

        self.logger.info("Entering window loop...")
        while not self.should_close and not pr.window_should_close():
            # Update fader and listen to state changes:
            new_state = self.fader.update()
            if new_state is not None:
                self.state = new_state

            pr.begin_drawing()
            pr.clear_background(pr.BLACK)
            
            match self.state:
                case GameState.COMBAT     : self.handle_combat()
                case GameState.EXPLORATION: self.handle_exploration()
                case GameState.GAME_OVER  : self.handle_game_over()
                case GameState.MAIN_MENU  : self.handle_main_menu()
                case GameState.MENU       : self.handle_menu()
                case GameState.EDITOR     : self.handle_editor()

            self.fader.draw()

            pr.end_drawing()

        self.logger.info("Closing raylib window...")
        pr.close_window()

        self.logger.info("Engine shutdown complete!")
    
    def handle_main_menu(self):
        # Don't interact while fading...
        if self.fader.is_fading:
            self.main_menu.update()
            return

        match self.main_menu.update():
            case MainMenuAction.NEW_GAME:
                self.logger.debug("Start a new game...")
                self.fader.start_fade(GameState.EXPLORATION)
            case MainMenuAction.LOAD_GAME:
                self.logger.debug("Load a saved game...")
            case MainMenuAction.MAP_EDITOR:
                self.logger.debug("Entering map editor...")
                self.fader.start_fade(GameState.EDITOR)
            case MainMenuAction.EXIT:
                self.logger.debug("Exiting game...")
                self.should_close = True
            case MainMenuAction.NONE:
                pass

    def handle_combat(self):
        ...
    
    def handle_exploration(self):
        ...

    def handle_game_over(self):
        ...
    
    def handle_menu(self):
        ...

    def handle_editor(self):
        # No interaction while fading:
        if self.fader.is_fading:
            self.level_editor.draw()
            return
        
        match self.level_editor.update():
            case LevelEditorAction.EXIT:
                self.fader.start_fade(GameState.MAIN_MENU)
        
        self.level_editor.draw()
