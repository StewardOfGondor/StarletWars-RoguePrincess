#!/usr/bin/env python3
import tcod

import dungen
from engine import Engine
from entity import Entity
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    rooms_max_size = 16
    rooms_min_size = 9
    max_rooms = 50

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32,8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (237,211,92) )
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (63,252,202) )
    entities = {npc, player}

    game_map = dungen.generate_dungeon(max_rooms,rooms_min_size, rooms_max_size, map_width, map_height, player)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Starlet Wars: Rogue Princess",
        vsync=True
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(root_console, context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()
