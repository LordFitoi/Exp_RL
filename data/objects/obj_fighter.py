import pygame
import libtcodpy as libtcod
from data.dta_constants import *

class Obj_Fighter:
    def __init__(self, stats):
        self.health_points = stats["Health"]
        self.defense_points = stats["Defense"]
        self.speed_points = stats["Speed"]
        self.hit_points = stats["Hit"]
        self.energy_amount = ENERGY_CAP
        self.fov = 10

    def get_energy(self):
        speed_amount = libtcod.random_get_int(0,100,self.speed_points)
        self.energy_amount = ENERGY_CAP-speed_amount


    def get_block_amount(self):
        return libtcod.random_get_int(0,1,self.defense_points)

    def get_damage_amount(self):
        return libtcod.random_get_int(0,1,self.health_points)

    def get_miss_amount(self, other):
        speed_amount = other.speed_points - self.speed_points
        if speed_amount > 0:
            if libtcod.random_get_int(0,0,speed_amount) < speed_amount:
                return True
        return False

    def attack(self, other, console):
        damage_amount = self.get_damage_amount()
        block_amount = other.get_block_amount()
        total_amount = damage_amount - block_amount
        console.add_text(str(self.ID)+" attacks "+str(other.ID))
        if other.get_miss_amount(self):
            if total_amount > 0:
                console.add_text(str(other.ID)+" recive "+str(total_amount)+" of damage.")
                return total_amount
            else: console.add_text(str(other.ID)+" blocks the attack.")
        else: console.add_text(str(self.ID)+" miss the attack.")
        return 0
            