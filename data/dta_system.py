import pygame
import libtcodpy as libtcod
from data.dta_constants import *
class Sys_Console:
    def __init__(self, coords, size):
        self.font = pygame.font.SysFont("Arial",15)
        self.log = []
        self.x, self.y = coords[0], coords[1] 
        self.canvas = pygame.Surface((size[0],size[1]))
        self.font_color = (255,255,255)
        self.font_background_color = (5,5,5)
        self.background_color = (5,5,5)

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
        for text in self.log:
            text_render = self.text_render(text)
            self.canvas.blit(text_render[0],(0,text_render[2]*current_text))
            current_text += 1
        if len(self.log) > 6:
            self.log.pop(0)
        surface.blit(self.canvas,(self.x,self.y))

class Sys_Fov:
    def __init__(self):
        self.fov_color = (0,0,0)

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
                if not libtcod.map_is_in_fov(map_fov,x,y):
                    rect = pygame.Rect(x*CELL_SIZE[0],y*CELL_SIZE[1],CELL_SIZE[0],CELL_SIZE[1])
                    pygame.draw.rect(surface,self.fov_color,rect)

class Sys_Turn:
    def __init__(self):
        self.creatures = []
        self.time = 0
        self.pause = False
        
    def update(self, map, console):
        self.creatures.sort(key=lambda creature: creature.energy_amount)
        if self.pause == False: 
            for index in range(len(self.creatures)):
                if self.creatures[index].ID != "Actor":
                    self.time = 0
                    limit = 1
                    delta_speed = 0
                    for creature in self.creatures:
                        if creature.ID == "Actor":
                            delta_speed = self.creatures[index].speed_points-creature.speed_points
                    
                    while self.time < limit:
                        extra_turn = libtcod.random_get_int(0,1,100)
                        
                        if extra_turn < abs(delta_speed):
                            if delta_speed > 0: limit += 1
                            elif delta_speed < 0: break
                        self.creatures[index].update(map, console)
                        self.time += 1
                    
                elif self.creatures[index].ID == "Actor":
                    self.creatures[index].update(map, console)
                print(self.creatures[index].ID,self.creatures[index].health_points)
        self.pause = True
        