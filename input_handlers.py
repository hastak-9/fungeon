from __future__ import annotations
from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, EscapeAction, BumpAction, WaitAction

if TYPE_CHECKING:
    from engine import Engine


MOVE_KEYS = {
    tcod.event.K_UP: (0, -1),
    tcod.event.K_w: (0, -1),
    tcod.event.K_DOWN: (0, 1),
    tcod.event.K_x: (0, 1),
    tcod.event.K_LEFT: (-1, 0),
    tcod.event.K_a: (-1, 0),
    tcod.event.K_RIGHT: (1, 0),
    tcod.event.K_d: (1, 0),
    tcod.event.K_q: (-1, -1),
    tcod.event.K_e: (1, -1),
    tcod.event.K_c: (1, 1),
    tcod.event.K_y: (-1, 1),
}

WAIT_KEYS = {
    tcod.event.K_s,
}


class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key in WAIT_KEYS:
            action = WaitAction(player)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        #no valid key was pressed
        return action
