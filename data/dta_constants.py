import pygame, sys, os, random

GAME_DIR = os.path.dirname(sys.argv[0])
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

MAP_WIDTH = 50
MAP_HEIGHT = 40

BACKGROUND_COLOR = (0,0,0)

FONT = pygame.image.load(os.path.join(GAME_DIR,"arial12x12.png"))
CELL_SIZE = [12, 12]

ACTOR_CHAR = [0, 1]
CRE_CHAR = [12,3]
WALL_CHAR = [13, 1]
FLOOR_CHAR = [14, 0]

INPUTS = {
    "Move" : {
        "North" : [pygame.K_KP8,pygame.K_UP],
        "South" : [pygame.K_KP2,pygame.K_DOWN],
        "East" : [pygame.K_KP6,pygame.K_RIGHT],
        "West" : [pygame.K_KP4,pygame.K_LEFT],
        "North_East" : [pygame.K_KP9,None],
        "North_West" : [pygame.K_KP7,None],
        "South_East" : [pygame.K_KP3,None],
        "South_West" : [pygame.K_KP1,None],
        "Wait" : [pygame.K_KP5,None]
    }
}

MAX_ROOMS = 10
MAX_SIZE = 10
MIN_SIZE = 4
VALUE_SIGN = lambda i:(1,-1)[i<0] 
ENERGY_CAP = 1000
FOV_COLOR = (0,0,0)
FOV_ALPHA = 150
CONSOLE_ALPHA = 190