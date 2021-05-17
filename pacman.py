import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Pacman(object):
    def __init__(self):
        self.name = "pacman"
        self.position = Vector2(200, 400)
        self.direction = STOP
        self.speed = 2
        self.radius = 10
        self.color = YELLOW

    def update(self, dt):
        self.position += self.direction*self.speed
        direction = self.getValidKey()
        if direction:
            self.moveByKey(direction)
        else:
            self.direction = STOP

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            return UP
        if key_pressed[pygame.K_DOWN]:
            return DOWN
        if key_pressed[pygame.K_LEFT]:
            return LEFT
        if key_pressed[pygame.K_RIGHT]:
            return RIGHT
        return None

    def moveByKey(self, direction):
        self.direction = direction

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)