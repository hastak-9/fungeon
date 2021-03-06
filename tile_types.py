from typing import Tuple

import numpy as np # type: ignore

# Tile graphics structured type compatible with Console.tiles_rb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #UNicode codepoint
        ("fg", "3B"), # 3 unsigned bytes for RGB colors fg-foreground
        ("bg", "3B"), # bg - background color
    ]
)
# Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), #True if this tile van be walked over
        ("transparent", np.bool), #True if this thile doesnt block FOV
        ("dark", graphic_dt), #Graphics for when this tile is not in FOV
        ("light", graphic_dt), #Graphics for when the tile is in FOV
    ]
)


def new_tile(
        *, # Enforce the use of keywords, so that parameter order doesnt matter
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


#SHROUD represents unexplored, new tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50))
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)