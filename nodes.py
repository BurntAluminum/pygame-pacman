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
        nodeO = Node(4.5, 15.5)
        nodeP = Node(8, 15.5)
        nodeQ = Node(14, 15.5)
        nodeR = Node(21, 15.5)
        nodeS = Node(26, 15.5)
        nodeT = Node(34, 15.5)
        nodeU = Node(40, 15.5)
        nodeV = Node(45, 15.5)
        nodeW = Node(51.5, 15.5)
        nodeX = Node(55, 15.5)
        nodeY = Node(8, 21.5)
        nodeZ = Node(14, 21.5)
        nodeAA = Node(21, 21.5)
        nodeAB = Node(26, 21.5)
        nodeAC = Node(34, 21.5)
        nodeAD = Node(40, 21.5)
        nodeAE = Node(45, 21.5)
        nodeAF = Node(51.5, 21.5)
        nodeAG = Node(8, 25)
        nodeAH = Node(14, 27)
        nodeAI = Node(21, 27)
        nodeAJ = Node(40, 27)
        nodeAK = Node(45, 27)
        nodeAL = Node(51.5, 25)

        nodeA.neighbors[RIGHT] = nodeB
        nodeA.neighbors[DOWN] = nodeO

        nodeB.neighbors[RIGHT] = nodeC
        nodeB.neighbors[DOWN] = nodeG

        nodeC.neighbors[RIGHT] = nodeD
        nodeC.neighbors[DOWN] = nodeI

        nodeD.neighbors[RIGHT] = nodeE
        nodeD.neighbors[DOWN] = nodeL

        nodeE.neighbors[RIGHT] = nodeF
        nodeE.neighbors[DOWN] = nodeN

        nodeF.neighbors[DOWN] = nodeX

        nodeG.neighbors[RIGHT] = nodeH

        nodeH.neighbors[RIGHT] = nodeI
        nodeH.neighbors[DOWN] = nodeQ

        nodeI.neighbors[UP] = nodeC
        nodeI.neighbors[DOWN] = nodeR
        nodeI.neighbors[LEFT] = nodeH

        nodeJ.neighbors[RIGHT] = nodeK

        nodeK.neighbors[LEFT] = nodeJ

        nodeL.neighbors[DOWN] = nodeU
        nodeL.neighbors[RIGHT] = nodeM

        nodeM.neighbors[RIGHT] = nodeN

        nodeO.neighbors[RIGHT] = nodeP

        nodeP.neighbors[RIGHT] = nodeQ

        nodeQ.neighbors[UP] = nodeH

        nodeR.neighbors[UP] = nodeI

        nodeS.neighbors[UP] = nodeJ
        nodeS.neighbors[LEFT] = nodeR
        nodeS.neighbors[DOWN] = nodeAB

        nodeT.neighbors[UP] = nodeK
        nodeT.neighbors[RIGHT] = nodeU

        nodeU.neighbors[UP] = nodeL
        nodeU.neighbors[LEFT] = nodeU

        nodeV.neighbors[UP] = nodeM
        nodeV.neighbors[RIGHT] = nodeW
        
        nodeW.neighbors[LEFT] = nodeV
        nodeW.neighbors[RIGHT] = nodeX

        nodeX.neighbors[UP] = nodeF

        nodeY.neighbors[UP] = nodeP

        nodeZ.neighbors[LEFT] = nodeY

        nodeAA.neighbors[RIGHT] = nodeAB

        nodeAB.neighbors[RIGHT] = nodeAC

        nodeAC.neighbors[RIGHT] = nodeAD

        nodeAD.neighbors[DOWN] = nodeAJ

        nodeAE.neighbors[RIGHT] = nodeAF
        
        nodeAF.neighbors[UP] = nodeW

        nodeAG.neighbors[UP] = nodeY
        
        nodeAH.neighbors[UP] = nodeZ

        nodeAI.neighbors[UP] = nodeAA
        
        nodeAJ.neighbors[UP] = nodeAD

        nodeAK.neighbors[UP] = nodeAE

        nodeAL.neighbors[UP] = nodeAF

        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM, nodeN, nodeO, nodeP, nodeQ, nodeR, nodeS, nodeT, nodeU, nodeV, nodeW, nodeX, nodeY, nodeZ, nodeAA, nodeAB, nodeAC, nodeAD, nodeAE, nodeAF, nodeAG, nodeAH, nodeAI, nodeAJ, nodeAK, nodeAL]

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)