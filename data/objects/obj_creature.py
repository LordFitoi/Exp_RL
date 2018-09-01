import pygame
import libtcodpy as libtcod
from data.dta_object import *
from data.objects.obj_fighter import *
from data.dta_constants import *

class Obj_Creature(Dta_Object, Obj_Fighter):
    def __init__(self, coords, char):
        Dta_Object.__init__(self, coords, char)
        stats = {
            "Health" : 20,
            "Defense" : 10,
            "Speed" : 100,
            "Hit" : 10
        }
        Obj_Fighter.__init__(self,stats)
        self.MOVE_LABEL = {
            "North" : [0,-1],
            "South" : [0,1],
            "East" : [1,0],
            "West" : [-1,0],
            "North_East" : [1,-1],
            "North_West" : [-1,-1],
            "South_East" : [1,1],
            "South_West" : [-1,1]
        }
        self.name = "Creature"
        self.actions = {
            "Move" : [0,0]
        }
        self.AI = False
        self.ID = "Creature"

    def reset_actions(self):
        self.actions["Move"] = [0,0]

    def move_and_collide(self, move_direction, map, console):
        if map.cells[self.y+move_direction[1]][self.x+move_direction[0]].block_path != True:
            self.move(move_direction)
            for creature in map.creatures:
                if self != creature:
                    if self.x == creature.x and self.y == creature.y:
                        invert_move_direction = [-move_direction[0],-move_direction[1]]
                        if creature.actions["Move"] != [0,0]:
                            if creature.actions["Move"] == invert_move_direction:
                                self.move(invert_move_direction)   
                        else:
                            self.move(invert_move_direction)
                        creature.health_points -= self.attack(creature, console)
        else: console.add_text("You run to the wall. Ouch!")
                        
                        
    def create_path(self, coords, map):
        map_path = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                libtcod.map_set_properties(map_path, x, y, False, not map.cells[y][x].block_path)
        path = libtcod.path_new_using_map(map_path,1.41)
        libtcod.path_compute(path,self.x,self.y,coords[0],coords[1])
        return path

    def read_path(self, path, limit):
        if not libtcod.path_is_empty(path):
            if libtcod.path_size(path) <= limit:
                x, y = libtcod.path_walk(path, True)
                return [x, y]
        libtcod.path_delete(path)

    def get_direction_from_coords(self, coords):
        delta_x = coords[0] - self.x
        delta_y = coords[1] - self.y
        direction = [0,0]
        if delta_x != 0: direction[0] = VALUE_SIGN(delta_x)
        if delta_y != 0: direction[1] = VALUE_SIGN(delta_y)
        return direction

    def update(self, map, console):
        if self.AI == True:
            for creature in map.creatures:
                if creature.ID == "Actor":
                    current_coords = [creature.x, creature.y]
                    new_coords = self.read_path(self.create_path(current_coords, map),self.fov)
                    if new_coords != None:
                        self.actions["Move"] = self.get_direction_from_coords(new_coords)
                    
        self.move_and_collide(self.actions["Move"], map, console)
        self.reset_actions()