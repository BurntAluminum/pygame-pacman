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
        nodeC = Node(21, 4)
        nodeD = Node(40, 4)
        nodeE = Node(50 ,4)
        nodeF = Node(55, 4)
        nodeG = Node(11, 10)
        nodeH = Node(14, 10)
        nodeI = Node(21, 10)
        nodeJ = Node(26, 10)
        nodeK = Node(34, 10)
        nodeL = Node(40, 10)
        nodeM = Node(45, 10)
        nodeN = Node(50, 10)
        nodeP = Node(4.5, 15)

        nodeA.neighbors[RIGHT] = nodeB
        nodeA.neighbors[DOWN] = nodeP

        nodeB.neighbors[RIGHT] = nodeC
        nodeB.neighbors[DOWN] = nodeG

        nodeC.neighbors[RIGHT] = nodeD
        nodeC.neighbors[DOWN] = nodeI

        nodeD.neighbors[RIGHT] = nodeE
        nodeD.neighbors[DOWN] = nodeL

        nodeE.neighbors[RIGHT] = nodeF
        nodeE.neighbors[DOWN] = nodeN

        nodeG.neighbors[RIGHT] = nodeH

        nodeH.neighbors[RIGHT] = nodeI

        #nodeI.neighbors[] =

        nodeJ.neighbors[RIGHT] = nodeK

        nodeK.neighbors[LEFT] = nodeJ

        nodeL.neighbors[RIGHT] = nodeM

        nodeM.neighbors[RIGHT] = nodeN

        nodeP.neighbors[RIGHT] = nodeO

        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM, nodeN, nodeP]

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)