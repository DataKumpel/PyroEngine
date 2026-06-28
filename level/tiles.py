from typing import NamedTuple
from enum import Enum


class CardinalRotation(Enum):
    """
    Cardinal Rotation in degrees. It describes the direction an object is facing.
    Default is NORTH (0°).
    """
    NORTH = 0
    WEST  = 90
    SOUTH = 180
    EAST  = 270


class TileRef(NamedTuple):
    tile_id: int
    rotation: CardinalRotation

    #===== SERIALIZATION =====
    def to_dict(self) -> dict:
        return {
            "id": self.tile_id,
            "rotation": self.rotation.value,
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("id", 0),
            CardinalRotation(data.get("rotation", 0)),
        )
    #===== SERIALIZATION =====
