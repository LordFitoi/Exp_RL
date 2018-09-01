import pygame
import libtcodpy as libtcod
from data.dta_constants import *

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
        self.pause = True