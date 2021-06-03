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
        self.target = self.node
        self.setPosition()

    def setPosition(self):
        self.position = self.node.position.copy()

    def update(self, dt):
        self.position += self.direction*self.speed*dt
        direction = self.getValidKey()
        if direction:
            self.moveByKey(direction)
        if self.overshotTarget():
            self.node = self.target
            self.setPosition()
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
        if self.direction is STOP:
            if self.node.neighbors[direction] is not None:
                self.direction = direction
                self.target = self.node.neighbors[direction]
    
    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False

    def render(self, screen):
        p = self.position.asInt()
        screen.blit(LEVEL, (0, 0))
        pygame.draw.circle(screen, self.color, p, self.radius)