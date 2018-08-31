import libtcodpy as libtcod
import pygame, sys

from data.dta_constants import *
from data.dta_system import *
from data.dta_dungeon_generator import *


def game_render():
    global SCREEN
    SCREEN.fill(BACKGROUND_COLOR)
    MAP.all_render(SCREEN)
    SYSTEM["Console"].render(SCREEN)
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
                SYSTEM["Turn"].pause = False
        MAP.update()
        SYSTEM["Turn"].update(MAP, SYSTEM["Console"])
        game_render()

def game_initialize():
    global SCREEN, MAP, PLAYER, SYSTEM
    pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Generator = Dta_Dungeon_Generator()
    MAP = Generator.create_dungeon()
    SYSTEM = {
        "Turn" : Sys_Turn(),
        "Console" : Sys_Console((15,SCREEN_HEIGHT-115),(300,115))
    }
    SYSTEM["Turn"].creatures = MAP.creatures

if __name__ == "__main__":
    game_initialize()
    game_main_loop()
print("Hello World")