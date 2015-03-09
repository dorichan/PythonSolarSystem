import maya.cmds as mc
import math

frames = 500
mc.playbackOptions(min = 0, max = frames)
bounceEx = "translateY = sin(time*10) + 1.5;" + "scaleY = sin(time*5);"
systemStr = cmds.internalVar(uwd=True)
texture = systemStr + "default//sourceimages//BasketballColor.jpg"
ball = mc.polySphere
position = 2

def createFileTexture(filename) :
    file = mc.shadingNode('file', asShader = True)
    placement = mc.shadingNode('place2dTexture', asUtility = True)
    mc.connectAttr(placement + ".coverage", file + ".coverage", f = True)
    mc.setAttr (file + ".ftn", filename, type = "string")
    return file

def createBall(exp, shape, tex, pos):
    fileNode = createFileTexture(tex)
    lambert = mc.shadingNode('lambert', n = "myMat", asShader = True)
    mc.connectAttr(fileNode + ".outColor", lambert + ".color", force = True);
    mySG = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = lambert+"SG")
    mc.connectAttr(lambert + ".outColor", mySG + ".surfaceShader", f = True)

    ball = shape(name = "Ball", radius = 1)
    mc.sets(ball[0], e = True, forceElement = mySG)
    mc.move(pos, 0, pos)
    mc.expression(object = ball[0], string = exp, name = "bounceExpression")

createBall(bounceEx, ball, texture, position)