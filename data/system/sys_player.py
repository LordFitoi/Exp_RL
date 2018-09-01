import pygame
from data.dta_constants import *

class Sys_Player:
    def __init__(self):
        self.description = {
            "History" : None
        }
        self.stats = {
            "Attribute": {
                "Strength" : {
                    "Label" : "Str",
                    "Points" : 10,
                    "Bonus" : 0
                },
                "Learning" : {
                    "Label" : "Lrn",
                    "Points" : 10,
                    "Bonus" : 0
                },
                "Dexterity" : {
                    "Label" : "Dxt",
                    "Points" : 10,
                    "Bonus" : 0
                },
                "Percepcion" : {
                    "Label" : "Prc",
                    "Points" : 10,
                    "Bonus" : 0
                },
            },
            "Status": {
                "Health" : {
                    "Label" : "Hp",
                    "Points" : 20,
                },
                "Speed" : {
                    "Label" : "Spd",
                    "Points" : 100,
                },
            }
        }
        self.inventory = []
        self.actor = None
        
    def get_actor(self, map):
        for creature in map.creatures:
            if creature.ID == "Actor":
                self.actor = creature
                break