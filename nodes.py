import pygame
from vector import Vector2
from constants import *

class Node(object):
    def __init__(self, x, y):
        self.row, self.column = x, y
        self.position = Vector2(x*TILEWIDTH, y*TILEHEIGHT)
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None}

    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)


class NodeGroup(object):
    def __init__(self):
        self.nodeList = []

    def setupTestNodes(self):
        nodeA = Node(4.5, 4)
        nodeB = Node(11, 4)
        nodeC = Node(11, 10)
        nodeD = Node(4.5, 15.5)
        nodeE = Node(8, 15.5)
        nodeF = Node(14, 15.5)
        nodeG = Node(20, 13)
        
        nodeA.neighbors[RIGHT] = nodeB
        nodeA.neighbors[DOWN] = nodeD
        nodeB.neighbors[DOWN] = nodeC
        nodeD.neighbors[RIGHT] = nodeE
        nodeE.neighbors[RIGHT] = nodeF
        

        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)