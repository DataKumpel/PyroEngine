import pyray as pr
import logging
from level.dungeon_map import DungeonMap


class LevelEditor:
    def __init__(self, win_width: int, win_height: int):
        self.win_width = win_width
        self.win_height = win_height

        self.dungeon_map = DungeonMap()

        self.camera = self.setup_camera()
        self.is_camera_moving = False

    def setup_camera(self) -> pr.Camera3D:
        return pr.Camera3D(
            position=pr.Vector3(10.0, 10.0, 10.0),
            target=pr.Vector3(0.0, 0.0, 0.0),
            up=pr.Vector3(0.0, 1.0, 0.0),
            fovy=60.0,
            projection=pr.CameraProjection.CAMERA_PERSPECTIVE,
        )

    def update(self):
        pass

    def draw(self):
        pr.begin_mode_3d(self.camera)

        pr.end_mode_3d()
