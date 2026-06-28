import json
import logging
from typing import TypedDict
from .tiles import TileRef


logger = logging.getLogger("PYRO_ENGINE")


class MapCell:

    # Serialization fields:
    #         0    1    2    3      4
    serial = "base wall ceil detail entity".split()

    def __init__(self, 
                 base_layer: TileRef | None = None, 
                 wall_layer: TileRef | None = None, 
                 ceiling_layer: TileRef | None = None, 
                 detail_layer: list[TileRef] | None = None, 
                 entity_id=0):
        self.base_layer = base_layer
        self.wall_layer = wall_layer
        self.ceiling_layer = ceiling_layer
        self.detail_layer = detail_layer or []
        self.entity_id = entity_id

    def to_dict(self) -> dict:
        return {
            self.serial[0]: self.base_layer.to_dict() if self.base_layer else None,
            self.serial[1]: self.wall_layer.to_dict() if self.wall_layer else None,
            self.serial[2]: self.ceiling_layer.to_dict() if self.ceiling_layer else None,
            self.serial[3]: [layer.to_dict() for layer in self.detail_layer],
            self.serial[4]: self.entity_id,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "MapCell":
        base = data.get(cls.serial[0])
        wall = data.get(cls.serial[1])
        ceiling = data.get(cls.serial[2])
        return cls(
            base_layer=TileRef.from_dict(base) if base is not None else None,
            wall_layer=TileRef.from_dict(wall) if wall is not None else None,
            ceiling_layer=TileRef.from_dict(ceiling) if ceiling is not None else None,
            detail_layer=[TileRef.from_dict(detail) for detail in data.get(cls.serial[3], [])],
            entity_id=data.get(cls.serial[4], 0),
        )
    

IntVec3 = tuple[int, int, int]


class DungeonMapSerial(TypedDict):
    map_name: str
    cells: dict[str, dict]


class DungeonMap:
    def __init__(self, name: str = "New Map"):
        self.name = name
        self.cells: dict[IntVec3, MapCell] = {}

    def __getitem__(self, pos: IntVec3):
        return self.cells.get(pos)
    
    def __setitem__(self, pos: IntVec3, cell: MapCell):
        self.cells[pos] = cell

    def __delitem__(self, pos: IntVec3):
        self.cells.pop(pos)

    def save_to_json(self, filepath: str):
        json_cells = {}
        for (x, y, z), cell in self.cells.items():
            key_str = f"{x},{y},{z}"
            json_cells[key_str] = cell.to_dict()
        
        data: DungeonMapSerial = {
            "map_name": self.name,
            "cells": json_cells,
        }

        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            logger.info(f"Map {self.name!r} saved to {filepath!r}...")
        except IOError as ex:
            logger.error(f"Error while saving map {self.name!r} to {filepath!r}!", exc_info=ex)
    
    @classmethod
    def load_from_json(cls, filepath: str) -> DungeonMap | None:
        try:
            with open(filepath, encoding="utf-8") as file:
                data: DungeonMapSerial = json.load(file)
            
            loaded_map = cls(name=data.get("map_name", "Unknown Map"))

            for key_str, cell_dict in data.get("cells", {}).items():
                x, y, z = [int(pos_str) for pos_str in key_str.split(",")]
                loaded_map[x, y, z] = MapCell.from_dict(cell_dict)

            logger.info(f"Loading map {loaded_map.name!r} successfully from {filepath!r}...")
            return loaded_map
        except (IOError, json.JSONDecodeError, ValueError) as ex:
            logger.error(f"Error loading map from {filepath!r}!", exc_info=ex)
            return None
        