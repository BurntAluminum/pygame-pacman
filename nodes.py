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
        nodeAM = Node(8, 30)
        nodeAN = Node(21, 30.5)
        nodeAO = Node(26, 30.5)
        nodeAP = Node(34, 30.5)
        nodeAQ = Node(40, 30.5)
        nodeAR = Node(51.5, 30)
        nodeAS = Node(8, 33)
        nodeAT = Node(14, 33)
        nodeAU = Node(14, 35.5)
        nodeAV = Node(21, 35.5)
        nodeAW = Node(26, 35.5)
        nodeAX = Node(34, 35.5)
        nodeAY = Node(40, 35.5)
        nodeAZ = Node(45, 35.5)
        nodeAAA = Node(45, 33)
        nodeAAB = Node(51.5, 33)
        nodeAAC = Node(4.5, 41)
        nodeAAD = Node(8, 41)
        nodeAAE = Node(14, 41)
        nodeAAF = Node(21, 41)
        nodeAAG = Node(26, 41)
        nodeAAH = Node(34, 41)
        nodeAAI = Node(40, 41)
        nodeAAJ = Node(45, 41)
        nodeAAK = Node(51.5, 41)
        nodeAAL = Node(55, 41)
        nodeAAM = Node(11, 47)
        nodeAAN = Node(14, 47)
        nodeAAO = Node(21, 47)
        nodeAAP = Node(26, 47)
        nodeAAQ = Node(34, 47)
        nodeAAR = Node(40, 47)
        nodeAAS = Node(45, 47)
        nodeAAT = Node(48, 47)
        nodeAAU = Node(4.5, 53)
        nodeAAV = Node(11, 53)
        nodeAAW = Node(26, 53)
        nodeAAX = Node(34, 53)
        nodeAAY = Node(48, 53)
        nodeAAZ = Node(55, 53)

        nodeA.neighbors[RIGHT] = nodeB
        nodeA.neighbors[DOWN] = nodeO

        nodeB.neighbors[LEFT] = nodeA
        nodeB.neighbors[RIGHT] = nodeC
        nodeB.neighbors[DOWN] = nodeG

        nodeC.neighbors[LEFT] = nodeB
        nodeC.neighbors[RIGHT] = nodeD
        nodeC.neighbors[DOWN] = nodeI

        nodeD.neighbors[LEFT] = nodeC
        nodeD.neighbors[RIGHT] = nodeE
        nodeD.neighbors[DOWN] = nodeL

        nodeE.neighbors[LEFT] = nodeD
        nodeE.neighbors[RIGHT] = nodeF
        nodeE.neighbors[DOWN] = nodeN

        nodeF.neighbors[LEFT] = nodeE
        nodeF.neighbors[DOWN] = nodeX

        nodeG.neighbors[UP] = nodeB
        nodeG.neighbors[RIGHT] = nodeH

        nodeH.neighbors[LEFT] = nodeG
        nodeH.neighbors[RIGHT] = nodeI
        nodeH.neighbors[DOWN] = nodeQ

        nodeI.neighbors[UP] = nodeC
        nodeI.neighbors[DOWN] = nodeR
        nodeI.neighbors[LEFT] = nodeH

        nodeJ.neighbors[RIGHT] = nodeK
        nodeJ.neighbors[DOWN] = nodeS

        nodeK.neighbors[LEFT] = nodeJ
        nodeK.neighbors[DOWN] = nodeT

        nodeL.neighbors[DOWN] = nodeU
        nodeL.neighbors[RIGHT] = nodeM
        nodeL.neighbors[UP] = nodeD

        nodeM.neighbors[LEFT] = nodeL
        nodeM.neighbors[RIGHT] = nodeN
        nodeM.neighbors[DOWN] = nodeV

        nodeN.neighbors[LEFT] = nodeM
        nodeN.neighbors[UP] = nodeE

        nodeO.neighbors[RIGHT] = nodeP
        nodeO.neighbors[UP] = nodeA

        nodeP.neighbors[RIGHT] = nodeQ
        nodeP.neighbors[DOWN] = nodeY
        nodeP.neighbors[LEFT] = nodeO

        nodeQ.neighbors[UP] = nodeH
        nodeQ.neighbors[LEFT] = nodeP

        nodeR.neighbors[UP] = nodeI
        nodeR.neighbors[RIGHT] = nodeS

        nodeS.neighbors[UP] = nodeJ
        nodeS.neighbors[LEFT] = nodeR
        nodeS.neighbors[DOWN] = nodeAB

        nodeT.neighbors[UP] = nodeK
        nodeT.neighbors[RIGHT] = nodeU
        nodeT.neighbors[DOWN] = nodeAC

        nodeU.neighbors[UP] = nodeL
        nodeU.neighbors[LEFT] = nodeU

        nodeV.neighbors[UP] = nodeM
        nodeV.neighbors[RIGHT] = nodeW
        
        nodeW.neighbors[LEFT] = nodeV
        nodeW.neighbors[RIGHT] = nodeX
        nodeW.neighbors[DOWN] = nodeAF

        nodeX.neighbors[UP] = nodeF
        nodeX.neighbors[LEFT] = nodeW

        nodeY.neighbors[UP] = nodeP
        nodeY.neighbors[RIGHT] = nodeZ
        nodeY.neighbors[DOWN] = nodeAG

        nodeZ.neighbors[LEFT] = nodeY
        nodeZ.neighbors[DOWN] = nodeAH

        nodeAA.neighbors[RIGHT] = nodeAB
        nodeAA.neighbors[DOWN] = nodeAI

        nodeAB.neighbors[RIGHT] = nodeAC
        nodeAB.neighbors[UP] = nodeS
        nodeAB.neighbors[LEFT] = nodeAA

        nodeAC.neighbors[RIGHT] = nodeAD
        nodeAC.neighbors[UP] = nodeT
        nodeAC.neighbors[LEFT] = nodeAB

        nodeAD.neighbors[DOWN] = nodeAJ
        nodeAD.neighbors[LEFT] = nodeAC

        nodeAE.neighbors[RIGHT] = nodeAF
        nodeAE.neighbors[DOWN] = nodeAK
        
        nodeAF.neighbors[UP] = nodeW
        nodeAF.neighbors[DOWN] = nodeAL
        nodeAF.neighbors[LEFT] = nodeAE

        nodeAG.neighbors[UP] = nodeY
        nodeAG.neighbors[LEFT] = nodeAL
        
        nodeAH.neighbors[UP] = nodeZ
        nodeAH.neighbors[RIGHT] = nodeAI
        nodeAH.neighbors[DOWN] = nodeAT

        nodeAI.neighbors[UP] = nodeAA
        nodeAI.neighbors[LEFT] = nodeAH
        nodeAI.neighbors[DOWN] = nodeAN
        
        nodeAJ.neighbors[UP] = nodeAD
        nodeAJ.neighbors[DOWN] = nodeAQ
        nodeAJ.neighbors[RIGHT] = nodeAK

        nodeAK.neighbors[UP] = nodeAE
        nodeAK.neighbors[LEFT] = nodeAJ
        nodeAK.neighbors[DOWN] = nodeAAA

        nodeAL.neighbors[UP] = nodeAF
        nodeAL.neighbors[RIGHT] = nodeAG

        nodeAM.neighbors[DOWN] = nodeAS
        nodeAM.neighbors[LEFT] = nodeAR

        nodeAN.neighbors[UP] = nodeAI
        nodeAN.neighbors[RIGHT] = nodeAO

        nodeAO.neighbors[LEFT] = nodeAN
        nodeAO.neighbors[DOWN] = nodeAW
        nodeAO.neighbors[RIGHT] = nodeAP

        nodeAP.neighbors[LEFT] = nodeAO
        nodeAP.neighbors[RIGHT] = nodeAQ
        nodeAP.neighbors[DOWN] = nodeAX

        nodeAQ.neighbors[UP] = nodeAJ
        nodeAQ.neighbors[LEFT] = nodeAP

        nodeAR.neighbors[RIGHT] = nodeAM
        nodeAR.neighbors[DOWN] = nodeAAB

        nodeAS.neighbors[UP] = nodeAM
        nodeAS.neighbors[RIGHT] = nodeAT
        nodeAS.neighbors[DOWN] = nodeAAD

        nodeAT.neighbors[LEFT] = nodeAS
        nodeAT.neighbors[UP] = nodeAH
        nodeAT.neighbors[DOWN] = nodeAU

        nodeAU.neighbors[UP] = nodeAT
        nodeAU.neighbors[RIGHT] = nodeAV

        nodeAV.neighbors[LEFT] = nodeAU
        nodeAV.neighbors[RIGHT] = nodeAW
        nodeAV.neighbors[DOWN] = nodeAAF
        
        nodeAW.neighbors[UP] = nodeAO
        nodeAW.neighbors[LEFT] = nodeAV
        nodeAW.neighbors[DOWN] = nodeAAG

        nodeAX.neighbors[UP] = nodeAP
        nodeAX.neighbors[RIGHT] = nodeAY
        nodeAX.neighbors[DOWN] = nodeAAH

        nodeAY.neighbors[LEFT] = nodeAX
        nodeAY.neighbors[RIGHT] = nodeAZ
        nodeAY.neighbors[DOWN] = nodeAAI

        nodeAZ.neighbors[UP] = nodeAAA
        nodeAZ.neighbors[LEFT] = nodeAY

        nodeAAA.neighbors[UP] = nodeAK
        nodeAAA.neighbors[DOWN] = nodeAZ
        nodeAAA.neighbors[RIGHT] = nodeAAB

        nodeAAB.neighbors[UP] = nodeAR
        nodeAAB.neighbors[LEFT] = nodeAAA
        nodeAAB.neighbors[DOWN] = nodeAAK
        
        nodeAAC.neighbors[RIGHT] = nodeAAD
        nodeAAC.neighbors[DOWN] = nodeAAU
        
        nodeAAD.neighbors[UP] = nodeAS
        nodeAAD.neighbors[LEFT] = nodeAAC
        nodeAAD.neighbors[RIGHT] = nodeAAE

        nodeAAE.neighbors[LEFT] = nodeAAD
        nodeAAE.neighbors[RIGHT] = nodeAAF
        nodeAAE.neighbors[DOWN] = nodeAAN
        
        nodeAAF.neighbors[UP] = nodeAV
        nodeAAF.neighbors[LEFT] = nodeAAE
        nodeAAF.neighbors[DOWN] = nodeAAO

        nodeAAG.neighbors[UP] = nodeAW
        nodeAAG.neighbors[RIGHT] = nodeAAH

        nodeAAH.neighbors[UP] = nodeAX
        nodeAAH.neighbors[LEFT] = nodeAAG

        nodeAAI.neighbors[UP] = nodeAY
        nodeAAI.neighbors[DOWN] = nodeAAR
        nodeAAI.neighbors[RIGHT] = nodeAAJ

        nodeAAJ.neighbors[LEFT] = nodeAAI
        nodeAAJ.neighbors[RIGHT] = nodeAAK
        nodeAAJ.neighbors[DOWN] = nodeAAS

        nodeAAK.neighbors[UP] = nodeAAB
        nodeAAK.neighbors[LEFT] = nodeAAJ
        nodeAAK.neighbors[RIGHT] = nodeAAL

        nodeAAL.neighbors[DOWN] = nodeAAZ
        nodeAAL.neighbors[LEFT] = nodeAAK

        nodeAAM.neighbors[RIGHT] = nodeAAN
        nodeAAM.neighbors[DOWN] = nodeAAV

        nodeAAN.neighbors[UP] = nodeAAE
        nodeAAN.neighbors[LEFT] = nodeAAM

        nodeAAO.neighbors[UP] = nodeAAF
        nodeAAO.neighbors[RIGHT] = nodeAAP

        nodeAAP.neighbors[DOWN] = nodeAAW
        nodeAAP.neighbors[LEFT] = nodeAAO
        nodeAAP.neighbors[RIGHT] = nodeAAQ

        nodeAAQ.neighbors[DOWN] = nodeAAX
        nodeAAQ.neighbors[LEFT] = nodeAAP
        nodeAAQ.neighbors[RIGHT] = nodeAAR

        nodeAAR.neighbors[UP] = nodeAAI
        nodeAAR.neighbors[LEFT] = nodeAAQ

        nodeAAS.neighbors[UP] = nodeAAJ
        nodeAAS.neighbors[RIGHT] = nodeAAT

        nodeAAT.neighbors[DOWN] = nodeAAY
        nodeAAT.neighbors[LEFT] = nodeAAS

        nodeAAU.neighbors[UP] = nodeAAC
        nodeAAU.neighbors[RIGHT] = nodeAAV
        
        nodeAAV.neighbors[UP] = nodeAAM
        nodeAAV.neighbors[LEFT] = nodeAAM
        nodeAAV.neighbors[RIGHT] = nodeAAW

        nodeAAW.neighbors[UP] = nodeAAP
        nodeAAW.neighbors[LEFT] = nodeAAV

        nodeAAX.neighbors[UP] = nodeAAQ
        nodeAAX.neighbors[RIGHT] = nodeAAY
        
        nodeAAY.neighbors[UP] = nodeAAT
        nodeAAY.neighbors[LEFT] = nodeAAX
        nodeAAY.neighbors[RIGHT] = nodeAAZ

        nodeAAZ.neighbors[UP] = nodeAAL
        nodeAAZ.neighbors[LEFT] = nodeAAY

        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM, nodeN, nodeO, nodeP, nodeQ, nodeR, nodeS, nodeT, nodeU, nodeV, nodeW, nodeX, nodeY, nodeZ, nodeAA, nodeAB, nodeAC, nodeAD, nodeAE, nodeAF, nodeAG, nodeAH, nodeAI, nodeAJ, nodeAK, nodeAL, nodeAM, nodeAN, nodeAO, nodeAP, nodeAQ, nodeAR, nodeAS, nodeAT, nodeAU, nodeAV, nodeAW, nodeAX, nodeAY, nodeAZ, nodeAAA, nodeAAB, nodeAAC, nodeAAD, nodeAAE, nodeAAF, nodeAAE, nodeAAG, nodeAAH, nodeAAI, nodeAAJ, nodeAAK, nodeAAL, nodeAAM, nodeAAN, nodeAAO, nodeAAP, nodeAAQ, nodeAAR, nodeAAS, nodeAAT, nodeAAU, nodeAAV, nodeAAW, nodeAAX, nodeAAY, nodeAAZ]

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)