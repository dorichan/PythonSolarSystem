import maya.cmds as mc
import math
from random import uniform as rand  

frames = 500
mc.playbackOptions(min = 0, max = frames)

#Bouncing ball section
ball = mc.polySphere(name = "Ball", radius = 1)

bounceEx = "translateY = sin(time*10) + 1.5;"
mc.expression(object = ball[0], string = bounceEx, name = "bounceExpression")
squishEx = "scaleY = sin(time*5);"
mc.expression(object = ball[0], string = squishEx, name = "squishExpression")

#Randomly moving ball section
ball2 = mc.polySphere(name = "Randomly Moving Ball", radius = 2) 

moveEx = "translateX = sin(time*rand(1,3));" + "translateY = cos(time*rand(1,3))+10;" + "translateZ = sin(time*rand(1,3));"
mc.expression(object = ball2[0], string = moveEx, name = "moveExpression")

#Create a turning wheel
wheel = mc.polyCylinder(name = "Turning Wheel", radius = 2)
mc.rotate(0,0,90) 
mc.move(6,0,6)

turnEx = "rotateY = time*20;" + "translateY = 1.5;"
mc.expression(object = wheel[0], string = turnEx, name = "turnExpression")