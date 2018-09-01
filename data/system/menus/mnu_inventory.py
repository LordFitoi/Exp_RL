import pygame
from data.dta_constants import *

class Mnu_Inventory:
    def __init__(self):
        self.font = pygame.font.SysFont(FONT_15[0],FONT_15[1])
        self.font_color = (255,255,50)
        self.displays = {
            "Stats" : None,
            "Equipment" : None,
            "Invetory" : None,
            "Combat" : None,
            "Talent" : None
        }
        self.canvas = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.canvas_alpha = INVENTORY_ALPHA

    def stats_render(self, system):
        x, y = 0, 0
        current_stat = 0
        for stat in system.player.stats:
            label_render = self.font.render(stat,False,self.font_color)
            label_height = label_render.get_height()
            current_stat += 1
            self.canvas.blit(label_render,(x,y+label_height*current_stat))
        x = 100
        current_stat = 0
        for stat in system.player.stats:
            label_render = self.font.render(str(system.player.stats[stat]),False,self.font_color)
            label_height = label_render.get_height()
            current_stat += 1
            self.canvas.blit(label_render,(x,y+label_height*current_stat))
        system.screen.blit(self.canvas,(0,0))

    def all_render(self, system):
        self.canvas.fill(BACKGROUND_COLOR)
        self.stats_render(system)
        self.canvas.set_alpha(self.canvas_alpha)