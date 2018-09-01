import pygame
from data.dta_constants import *

class Sys_Player:
    def __init__(self):
        self.description = {
            "History" : None
        }
        self.stats = {
            "Health" : 20,
            "Defense" : 10,
            "Speed" : 100,
            "Hit" : 10 
        }
        self.inventory = []
