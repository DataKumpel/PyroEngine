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

    def to_dict(self) -> dict:
        return {
            "id": self.tile_id,
            "rotation": self.rotation.value,
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        rotation = CardinalRotation.NORTH
        match data.get("rotation"):
            case 0:
                rotation = CardinalRotation.NORTH
            case 90:
                rotation = CardinalRotation.WEST
            case 180:
                rotation = CardinalRotation.SOUTH
            case 270:
                rotation = CardinalRotation.EAST
        
        return cls(
            data.get("id"),
            rotation,
        )
