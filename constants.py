import pygame
from pygame.locals import *
import os
from vector import Vector2

TILEWIDTH = 16
TILEHEIGHT = 16
NROWS = 57
NCOLS = 60
SCREENWIDTH = NCOLS * TILEWIDTH
SCREENHEIGHT = NROWS * TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
BLACK = (0, 0, 0)
FPS = 60

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)
STOP = Vector2()

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

LEVEL = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'paclevel.png')), (SCREENWIDTH, SCREENHEIGHT))