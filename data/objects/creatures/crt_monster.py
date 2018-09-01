import pygame, math
from data.objects.obj_creature import *
from data.dta_constants import *

class Crt_Monster(Obj_Creature):
    def __init__(self, coords):
        self.CHAR = CRE_CHAR
        Obj_Creature.__init__(self, coords, self.CHAR)
        self.AI= True
        self.speed_points = 100
        self.fov = 20
    