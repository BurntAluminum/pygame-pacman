import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Pacman(object):
    def __init__(self, nodes):
        self.name = "pacman"
        self.direction = STOP
        self.speed = 2
        self.radius = 10
        self.color = YELLOW
        self.nodes = nodes
        self.node = nodes.nodeList[0]
        self.setPosition()
        self.keyDown = False

    def setPosition(self):
        self.position = self.node.position.copy()

    def update(self, dt):
        direction = self.getValidKey()
        if direction:
            self.moveByKey(direction)

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
        if self.node.neighbors[direction] is not None:
            if not self.keyDown:
                self.direction = direction
                self.node = self.node.neighbors[self.direction]
                self.setPosition()
                self.keyDown = True

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)