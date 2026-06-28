from typing import NamedTuple
from enum import Enum, auto


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


class TileKind(Enum):
    FLOOR = auto()
    WALL = auto()
    CEILING = auto()
    DETAIL = auto()


Color = tuple[int, int, int, int]  # RGBA


class TileDefinition(NamedTuple):
    tile_id: int
    name: str
    kind: TileKind
    color: Color
    solid: bool


class TileCatalog:
    def __init__(self):
        self._tiles: dict[int, TileDefinition] = {}
    
    @classmethod
    def default(cls):
        catalog = cls()
        # TODO: Register placeholders
        return catalog

    def register(self, tile: TileDefinition):
        # Check if already registered:
        if tile.tile_id in self._tiles:
            raise ValueError(f"Tile with id={tile.tile_id} already registered!")
        
        self._tiles[tile.tile_id] = tile

    def __getitem__(self, tile_id: int):
        try:
            return self._tiles[tile_id]
        except KeyError:
            # TODO: Return default tile
            ...
    
    def all(self) -> list[TileDefinition]:
        return list(self._tiles.values())
    