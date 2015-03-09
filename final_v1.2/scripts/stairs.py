import maya.cmds as mc
import math

#Straight staircase variables
numOfStairs=25
stairWidth=5
radiusOfPoles=0.2
heightOfPoles=3
widthOfHandrail=0.3
heightOfHandrail=35
depthOfHandrail=0.5

#Spiral staircase variables
spiralHeight=25
spiralRadius=0.5
spiralY=12

#Rotation variables
rY=45
rX=90
rZ=90

#Movement variables
xMove=2
yMove=16
zMove=12

isSpiral=False
isStraight=False

#Create UI
mainWindow=mc.window(visible=True, title="Staircase Tool v1.0 by Dori C.")
mc.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=250)


def CreateStraightStaircase():
    for i in range(numOfStairs):
        #Creating 25 stairs
         mc.polyCube(name="stairs", width=stairWidth)
         mc.move(0,i,i)
         #Creating the supports for the hand rails
         mc.polyCylinder(name="poles", radius=radiusOfPoles, height=heightOfPoles)
         mc.move(2,i+2,i)
         mc.polyCylinder(name="poles", radius=radiusOfPoles, height=heightOfPoles)
         mc.move(-2,i+2,i)

    #Creating the hand rails
    mc.polyCube(name="handrail", width=widthOfHandrail, height=heightOfHandrail, depth=depthOfHandrail)
    mc.move(xMove,yMove,zMove)
    mc.rotate(rX,rY,rZ)
    mc.polyCube(name="handrail", width=widthOfHandrail, height=heightOfHandrail, depth=depthOfHandrail)
    mc.move(-xMove,yMove,zMove)
    mc.rotate(rX,rY,rZ)

def CreateSpiralStaircase():
    #Creating the steps for the spiral staircase
    for i in range(spiralHeight):
        mc.polyCube(name="spiral", width=stairWidth)
        mc.move(math.sin(1+180),i,0)
        mc.xform(ws=True, rp=(0,0,0))
        mc.rotate(0,i,0)
    
    #Creating the center support for the spiral staircase
    mc.polyCylinder(name="center", radius=spiralRadius, height=spiralHeight)
    mc.move(0,spiralY,0)
    
if isStraight==True:
    CreateStraightStaircase()
    
if isSpiral==True:
    CreateSpiralStaircase()