import pygame
from data.objects.obj_creature import *
from data.dta_constants import *

class Crt_Actor(Obj_Creature):
    def __init__(self, coords):
        self.CHAR = ACTOR_CHAR
        Obj_Creature.__init__(self, coords, self.CHAR)
        self.name = "Juansito"
        self.ID = "Actor"

    def control(self, event, map):
        for input in self.MOVE_LABEL:
            for key in INPUTS["Move"][input]:
                if event.key == key:
                    self.actions["Move"] = self.MOVE_LABEL[input]
