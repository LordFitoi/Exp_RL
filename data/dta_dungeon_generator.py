import pygame
import libtcodpy as libtcod
from data.dta_constants import *
from data.dta_system import *
from data.objects.creatures.crt_actor import *
from data.objects.creatures.crt_monster import *

class Tile:
    def __init__(self, block_path):
        self.block_path = block_path

class Corridor:
    def __init__(self, coords, length):
        self.x, self.y = round(coords[0]), round(coords[1])
        self.LENGTH = round(length)
class Corridor_V(Corridor):
    def __init__(self, coords1, coords2, offsetx):
        length = coords2[1] - coords1[1]
        coords = [coords1[0]+offsetx,coords1[1]]
        Corridor.__init__(self, coords, length)
    def create_floor(self, dungeon):
        for length in range(abs(self.LENGTH)):
            try: 
                if self.LENGTH > 0: dungeon.cells[self.y+length][self.x].block_path = False
                elif self.LENGTH < 0: dungeon.cells[self.y-length][self.x].block_path = False
            except IndexError: pass
class Corridor_H(Corridor):
    def __init__(self, coords1, coords2, offsety):
        length = coords2[0] - coords1[0]
        coords = [coords1[0],coords1[1]+offsety]
        Corridor.__init__(self, coords, length)
    def create_floor(self, dungeon):
        for length in range(abs(self.LENGTH)):
            try: 
                if self.LENGTH > 0: dungeon.cells[self.y][self.x+length].block_path = False
                elif self.LENGTH < 0: dungeon.cells[self.y][self.x-length].block_path = False
            except IndexError: pass

class Room:
    def __init__(self, coords, size):
        self.x, self.y = coords[0], coords[1]
        self.size = [size[0], size[1]]
        self.x2, self.y2 = self.x+self.size[0],self.y+self.size[1]
        coords = [self.x*CELL_SIZE[0],self.y*CELL_SIZE[1]]
        size = [self.size[0]*CELL_SIZE[0],self.size[1]*CELL_SIZE[1]]
        self.rect = pygame.Rect(coords[0],coords[1],size[0],size[1])
        self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    def get_center(self):
        center = [round((self.x+self.x2)/2),round((self.y+self.y2)/2)]
        return center

    def create_floor(self, dungeon):
        for row in range(self.size[1]):
            for column in range(self.size[0]):
                dungeon.cells[self.y+row][self.x+column].block_path = False
            
class Dungeon:
    def __init__(self):
        self.cells = [[Tile(True) for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
        self.rooms = []
        self.corridors = []
        self.creatures = []
        self.map_fov = None 

    def char_render(self, surface, texture, size, coords, offset):
        surface.blit(texture, (coords[0]*size[0], coords[1]*size[1]), (offset[0]*size[0],offset[1]*size[1],size[0],size[1]))

    def map_render(self, surface):
        x, y = 0, 0
        for row in self.cells:
            for column in row:
                if column.block_path == True:
                    self.char_render(surface,FONT,CELL_SIZE,(x,y),WALL_CHAR)
                else:
                    self.char_render(surface,FONT,CELL_SIZE,(x,y),FLOOR_CHAR)
                x += 1
            y += 1
            x = 0

    def obj_render(self, surface):
        for creature in self.creatures:
            if libtcod.map_is_in_fov(self.map_fov,creature.x,creature.y):
                creature.render(surface)

    def fov_render(self, id, system):
        for creature in self.creatures:
            if creature.ID == id:
                map_fov = system.fov.get_fov((creature.x,creature.y),self,creature.fov)
                system.fov.render(system.screen, map_fov)
                self.map_fov = map_fov
                break

    def all_render(self, system):
        self.map_render(system.screen)
        self.obj_render(system.screen)
        self.fov_render("Actor", system)
        
    def get_player(self):
        for creature in self.creatures:
            if creature.ID == "Actor":
                return creature

    def update(self):
        for creature in self.creatures:
            creature.get_energy()
            if creature.health_points <= 0:
                self.creatures.remove(creature)

class Dta_Dungeon_Generator:
    def __init__(self):
        self.MAX_ROOMS = MAX_ROOMS
        self.MAX_SIZE = MAX_SIZE
        self.MIN_SIZE = MIN_SIZE

    def create_rooms(self, dungeon):
        for num in range(self.MAX_ROOMS):
            size = [
                libtcod.random_get_int(0,MIN_SIZE,MAX_SIZE),
                libtcod.random_get_int(0,MIN_SIZE,MAX_SIZE)
            ]
            coords = [
                libtcod.random_get_int(0,1,MAP_WIDTH-size[0]-1),
                libtcod.random_get_int(0,1,MAP_HEIGHT-size[1]-1)
            ]
            new_room = Room(coords, size)
            is_intersect = False
            for room in dungeon.rooms:
                if new_room.rect.colliderect(room.rect):
                    is_intersect = True
                    break
            if not is_intersect:
                dungeon.rooms.append(new_room)
                current_center = new_room.get_center()
                if len(dungeon.rooms) != 0:
                    previous_center = dungeon.rooms[len(dungeon.rooms)-2].get_center()
                    direction= libtcod.random_get_int(0,0,1)
                    if direction == 1:
                        corridor_v = Corridor_V(current_center,previous_center,0)
                        corridor_h = Corridor_H(current_center,previous_center,corridor_v.LENGTH)
                    else:
                        corridor_h = Corridor_H(current_center,previous_center,0)
                        corridor_v = Corridor_V(current_center,previous_center,corridor_h.LENGTH)
                    dungeon.corridors.append(corridor_h)
                    dungeon.corridors.append(corridor_v)
                    
    def create_floor(self, dungeon):
        for room in dungeon.rooms:
            room.create_floor(dungeon)
        for corridor in dungeon.corridors:
            corridor.create_floor(dungeon)

    def create_creatures(self, dungeon):
        dungeon.creatures.append(Crt_Actor(dungeon.rooms[0].get_center()))
        num = random.randrange(0,len(dungeon.rooms))
        dungeon.creatures.append(Crt_Monster(dungeon.rooms[num].get_center()))

    def create_dungeon(self):
        new_dungeon = Dungeon()
        self.create_rooms(new_dungeon)
        self.create_floor(new_dungeon)
        self.create_creatures(new_dungeon)
        return new_dungeon

    