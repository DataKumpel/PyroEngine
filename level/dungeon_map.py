import json
import logging


logger = logging.getLogger("PYRO_ENGINE")


class MapCell:
    def __init__(self, base_layer=0, wall_layer=0, detail_layer: list | None = None, entity_id=0, collision=False):
        self.base_layer = base_layer
        self.wall_layer = wall_layer
        self.detail_layer = detail_layer or []
        self.entity_id = entity_id
        self.collision = collision

    def to_dict(self) -> dict:
        return {
            "b": self.base_layer,
            "w": self.wall_layer,
            "d": self.detail_layer,
            "e": self.entity_id,
            "c": self.collision,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "MapCell":
        return cls(
            base_layer=data.get("b", 0),
            wall_layer=data.get("w", 0),
            detail_layer=data.get("d", []),
            entity_id=data.get("e", 0),
            collision=data.get("c", False),
        )