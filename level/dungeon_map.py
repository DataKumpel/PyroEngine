import json
import logging


logger = logging.getLogger("PYRO_ENGINE")


class MapCell:

    # Serialization fields:
    #         0    1    2    3      4      5
    serial = "base wall ceil detail entity col".split()

    def __init__(self, base_layer=0, wall_layer=0, ceiling_layer=0, detail_layer: list | None = None, entity_id=0, collision=False):
        self.base_layer = base_layer
        self.wall_layer = wall_layer
        self.ceiling_layer = ceiling_layer
        self.detail_layer = detail_layer or []
        self.entity_id = entity_id
        self.collision = collision

    def to_dict(self) -> dict:
        return {
            self.serial[0]: self.base_layer,
            self.serial[1]: self.wall_layer,
            self.serial[2]: self.ceiling_layer,
            self.serial[3]: self.detail_layer,
            self.serial[4]: self.entity_id,
            self.serial[5]: self.collision,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "MapCell":
        return cls(
            base_layer=data.get(cls.serial[0], 0),
            wall_layer=data.get(cls.serial[1], 0),
            ceiling_layer=data.get(cls.serial[2], 0),
            detail_layer=data.get(cls.serial[3], []),
            entity_id=data.get(cls.serial[4], 0),
            collision=data.get(cls.serial[5], False),
        )