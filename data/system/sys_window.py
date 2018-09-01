import pygame
from data.dta_constants import *

class Sys_Window:
    def __init__(self, coords, size):
        self.x, self.y = coords[0], coords[1]
        self.width, self.height = size[0], size[1]
        self.canvas = pygame.Surface((self.width, self.height))
        self.canvas_color = COLORS["Black"]
        self.texture = FONT
        self.char = WINDOW_CHAR
        
    def box_render(self):
        self.canvas.fill(self.canvas_color)
        # Draw: Outlines:
        for x in range(round(self.width/CELL_SIZE[0])):
            self.char_render((x*CELL_SIZE[0],0),self.char[1])
            self.char_render((x*CELL_SIZE[0],self.height-CELL_SIZE[1]),self.char[1])
        for y in range(round(self.height/CELL_SIZE[1])):
            self.char_render((0,y*CELL_SIZE[1]),self.char[0])
            self.char_render((self.width-CELL_SIZE[0],y*CELL_SIZE[1]),self.char[0])
        
        # Draw: Borders.
        self.char_render((0,0),self.char[8])
        self.char_render((self.width-CELL_SIZE[0],0),self.char[9])
        self.char_render((0,self.height-CELL_SIZE[1]),self.char[7])
        self.char_render((self.width-CELL_SIZE[0],self.height-CELL_SIZE[1]),self.char[10])
        
    def char_render(self, coords, char):
        self.canvas.blit(self.texture,coords,(char[0]*CELL_SIZE[0],char[1]*CELL_SIZE[1],CELL_SIZE[0],CELL_SIZE[1]))

    def render(self, surface):
        surface.blit(self.canvas,(self.x,self.y))
        
