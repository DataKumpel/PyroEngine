import pyray as pr
import logging
from level.dungeon_map import DungeonMap
from enum import Enum, auto


class LevelEditorAction(Enum):
    EXIT = auto()
    NONE = auto()


class LevelEditor:
    def __init__(self, win_width: int, win_height: int):
        self.win_width = win_width
        self.win_height = win_height

        self.dungeon_map = DungeonMap()

        self.camera = self.setup_camera()
        self.is_camera_moving = False

    def setup_camera(self) -> pr.Camera3D:
        return pr.Camera3D(
            pr.Vector3(10.0, 10.0, 10.0),
            pr.Vector3(0.0, 0.0, 0.0),
            pr.Vector3(0.0, 1.0, 0.0),
            60.0,
            pr.CameraProjection.CAMERA_PERSPECTIVE,
        )

    def update(self) -> LevelEditorAction:
        if pr.is_key_pressed(pr.KeyboardKey.KEY_ESCAPE):
            return LevelEditorAction.EXIT
        
        self.control_camera()
        if self.is_camera_moving:
            pr.update_camera(self.camera, pr.CameraMode.CAMERA_FREE)

        return LevelEditorAction.NONE
    
    def control_camera(self):
        if pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_RIGHT):
            pr.disable_cursor()
            self.is_camera_moving = True
        elif pr.is_mouse_button_released(pr.MouseButton.MOUSE_BUTTON_RIGHT):
            pr.enable_cursor()
            self.is_camera_moving = False

    def draw_axis_gizmo(self):
        zero_vector = pr.Vector3(0.0, 0.0, 0.0)
        axis_len = 5.0
        unit_x = pr.Vector3(axis_len, 0.0, 0.0)
        unit_y = pr.Vector3(0.0, axis_len, 0.0)
        unit_z = pr.Vector3(0.0, 0.0, axis_len)

        pr.draw_line_3d(zero_vector, unit_x, pr.RED)
        pr.draw_line_3d(zero_vector, unit_y, pr.GREEN)
        pr.draw_line_3d(zero_vector, unit_z, pr.BLUE)

    def render_ui(self):
        pr.draw_text("LEVEL EDITOR", 10, 10, 20, pr.RAYWHITE)
        if self.is_camera_moving:
            pr.draw_text("Kamera: Aktiv (WASD = Bewegen; Maus = Umsehen)", 10, 40, 20, pr.GREEN)
        else:
            pr.draw_text("Halte RECHTSKLICK, um die Kamera zu steuern", 10, 40, 20, pr.GRAY)

    def draw(self):
        pr.begin_mode_3d(self.camera)

        pr.draw_grid(20, 1.0)
        self.draw_axis_gizmo()

        pr.end_mode_3d()

        self.render_ui()
