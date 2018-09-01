import pygame
from data.dta_constants import * 

class Dta_Object:
    def __init__(self, coords, char):
        self.x , self.y = coords[0], coords[1]
        self.texture = FONT
        self.char = char
        self.ID = "Object"
        
    def move(self, move_direction):
         self.x += move_direction[0]
         self.y += move_direction[1]

    def render(self, surface):
        size = CELL_SIZE
        offset = [self.char[0]*size[0],self.char[1]*size[1]]
        coords = [self.x*size[0],self.y*size[1]]
        surface.blit(self.texture, coords, (offset[0],offset[1],size[0],size[1]))
