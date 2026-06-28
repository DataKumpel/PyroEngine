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


# Some Default Tiles:
DEFAULT_FLOOR_TILE   = TileDefinition(0, "Default Floor", TileKind.FLOOR, (133, 133, 133, 255), True)
DEFAULT_WALL_TILE    = TileDefinition(0, "Default Wall", TileKind.WALL, (200, 55, 255, 255), True)
DEFAULT_CEILING_TILE = TileDefinition(0, "Default Ceiling", TileKind.CEILING, (0, 170, 255, 255), True)


class TileCatalog:
    def __init__(self):
        self._tiles: dict[int, TileDefinition] = {}
        self._default_tile = DEFAULT_FLOOR_TILE
    
    @classmethod
    def default(cls):
        catalog = cls()
        catalog.register(DEFAULT_FLOOR_TILE)
        catalog.register(DEFAULT_WALL_TILE)
        catalog.register(DEFAULT_CEILING_TILE)
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
            return self._default_tile
    
    def all(self) -> list[TileDefinition]:
        return list(self._tiles.values())
    