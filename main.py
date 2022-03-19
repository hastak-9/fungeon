import tcod
import copy

from engine import Engine
import entity_factories
from procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 10

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player)

    engine.game_map = generate_dungeon(
        max_rooms,
        room_min_size,
        room_max_size,
        map_width,
        map_height,
        max_monsters_per_room,
        engine)
    player.gamemap = engine.game_map #TODO: Attribute error entity has no gamemap umgangen, nach lsg schauen
    engine.update_fov()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="My Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(root_console, context)
            engine.event_handler.handle_events()


if __name__ == '__main__':
    main()
