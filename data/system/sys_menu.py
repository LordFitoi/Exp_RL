import pygame
import libtcodpy as libtcod
from data.dta_constants import *
from data.system.menus.mnu_inventory import *

class Sys_Menu:
    def __init__(self):
        self.invetory = Mnu_Inventory()
    
    def render(self, system):
        self.invetory.all_render(system)