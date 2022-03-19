from entity import Entity
from game_map import GameMap

player = Entity(
    char="@",
    color=(0, 255, 100),
    name="player",
    blocks_movement=True
)

orc = Entity(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    blocks_movement=True
)

troll = Entity(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    blocks_movement=True
)