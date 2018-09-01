import pygame
import libtcodpy as libtcod
from data.dta_constants import *

from data.system.sys_console import *
from data.system.sys_fov import *
from data.system.sys_menu import *
from data.system.sys_player import *
from data.system.sys_turn import *

class Dta_System:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.console = Sys_Console((15,SCREEN_HEIGHT-115),(300,115))
        self.fov = Sys_Fov()
        self.turn = Sys_Turn()
        self.menu = Sys_Menu()
        self.player = Sys_Player()
        
    def all_render(self):
        self.screen.fill(BACKGROUND_COLOR)

    def gui_render(self):
        self.console.render(self.screen)
        self.menu.render(self)

    def update(self, map):
        self.turn.update(map, self.console)