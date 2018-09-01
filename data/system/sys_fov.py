import pygame
import libtcodpy as libtcod
from data.dta_constants import *

class Sys_Fov:
    def __init__(self):
        self.fov_color = (0,0,0)
        self.fov_alpha = 150
        self.map_fov = [[True for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    
    def get_fov(self, coords ,map, distance):
        map_fov = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                libtcod.map_set_properties(map_fov, x, y, not map.cells[y][x].block_path, not map.cells[y][x].block_path)
        libtcod.map_compute_fov(map_fov, coords[0], coords[1], distance,True,not libtcod.FOV_BASIC)
        return map_fov

    def render(self, surface, map_fov):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                cell_fov = pygame.Surface((CELL_SIZE[0],CELL_SIZE[1]))
                cell_fov.fill(self.fov_color)
                if not libtcod.map_is_in_fov(map_fov,x,y):
                    if not self.map_fov[y][x]: cell_fov.set_alpha(self.fov_alpha)
                    surface.blit(cell_fov,(x*CELL_SIZE[0],y*CELL_SIZE[1]))
                else: self.map_fov[y][x] = False