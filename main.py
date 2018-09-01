import libtcodpy as libtcod
import pygame, sys

from data.dta_constants import *
from data.dta_system import *
from data.dta_dungeon_generator import *


def game_render():
    SYSTEM.all_render()
    MAP.all_render(SYSTEM)
    SYSTEM.gui_render()
    pygame.display.flip()

def game_main_loop():
    game_quit = False
    player = MAP.get_player()
    while not game_quit:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT: game_quit = True
            if event.type == pygame.KEYDOWN:
                player.control(event, MAP.cells)
                SYSTEM.turn.pause = False
        MAP.update()
        SYSTEM.update(MAP)
        game_render()

def game_initialize():
    global MAP, SYSTEM
    pygame.init()
    pygame.font.init()
    Generator = Dta_Dungeon_Generator()
    MAP = Generator.create_dungeon()
    SYSTEM = Dta_System()
    SYSTEM.turn.creatures = MAP.creatures

if __name__ == "__main__":
    game_initialize()
    game_main_loop()

print("Hello World")