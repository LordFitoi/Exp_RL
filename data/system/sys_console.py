import pygame
import libtcodpy as libtcod
from data.dta_constants import *

class Sys_Console:
    def __init__(self, coords, size):
        self.font = pygame.font.SysFont(FONT_15[0],FONT_15[1])
        self.log = []
        self.x, self.y = coords[0], coords[1] 
        self.canvas = pygame.Surface((size[0],size[1]))
        self.canvas_alpha = CONSOLE_ALPHA
        self.font_color = (255,255,255)
        self.font_background_color = BACKGROUND_COLOR
        self.background_color = BACKGROUND_COLOR

    def add_text(self, text):
        self.log.append(text)
    
    def remove_text(self, text):
        self.log.remove(text)

    def text_render(self, text):
        text_render = self.font.render(text,False,self.font_color,self.font_background_color)
        text_width = text_render.get_width()
        text_height = text_render.get_height()
        return [text_render, text_width, text_height]

    def render(self, surface):
        self.canvas.fill(self.background_color)
        current_text = 0
        while len(self.log) > 6: self.log.pop(0)
        for text in self.log:
            text_render = self.text_render(text)
            self.canvas.blit(text_render[0],(0,text_render[2]*current_text))
            current_text += 1
        self.canvas.set_alpha(self.canvas_alpha)
        surface.blit(self.canvas,(self.x,self.y))