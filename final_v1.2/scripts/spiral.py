import maya.cmds as maya
import math

for i in range(360):
    maya.polyCube(name="mathtest", width=i + math.sin(i))
    maya.move(0,i,math.cos(i))
    maya.xform(ws=True, rp=(0,0,0))
    maya.rotate(0,i,0)