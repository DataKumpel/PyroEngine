import pyray as pr
from enum import Enum, auto


class FadeMode(Enum):
    IN = auto()
    OUT = auto()
    NONE = auto()


class ScreenFader:
    def __init__(self, width: int, height: int, duration: float = 1.0):
        self.width = width
        self.height = height
        self.duration = duration

        self.mode = FadeMode.IN
        self.timer = 0.0
        self.next_state = None  # This should be some sort of state-enum...

    def start_fade(self, next_state: int, mode=FadeMode.OUT):
        self.mode = mode
        self.timer = 0.0
        self.next_state = next_state

    def update(self) -> int | None:
        if self.mode == FadeMode.NONE:
            return None
        
        self.timer += pr.get_frame_time()
        progress = min(self.timer / self.duration, 1.0)

        if progress < 1.0:
            return None
        

        match self.mode:
            case FadeMode.OUT:
                state_to_switch = self.next_state
                self.mode = FadeMode.IN
                self.timer = 0.0
                return state_to_switch
            case FadeMode.IN:
                self.mode = FadeMode.NONE
                self.timer = 0.0
                return None
    
    def draw(self):
        if self.mode == FadeMode.NONE:
            return
        
        progress = min(self.timer / self.duration, 1.0)
        alpha = 0
        match self.mode:
            case FadeMode.OUT:
                alpha = int(progress * 255)
            case FadeMode.IN:
                alpha = int((1.0 - progress) * 255)
        
        fade_color = pr.Color(0, 0, 0, alpha)
        pr.draw_rectangle(0, 0, self.width, self.height, fade_color)

    @property
    def is_fading(self) -> bool:
        return self.mode != FadeMode.NONE
