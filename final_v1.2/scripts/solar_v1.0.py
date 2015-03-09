import maya.cmds as mc
import math
from random import uniform as rand

sunSize = 10.0
sunSpeed = 3.0
planetNum = 9
frames = 1500
mc.playbackOptions(loop = "continuous", min = 400, max = frames)
spinEx = "rotateY = time*10.0;"

planetSize = [0.2, 0.4, 0.5, 0.3, 2.5, 2.0, 1.5, 1.5, 0.4]

planetName = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "L573"]

orbitEx = ["translateX = 15 * cos(time*1.8);" + "translateZ = 15 * sin(time*1.8);", # Mercury
           "translateX = 20 * cos(time*1.5);" + "translateZ = 20 * sin(time*1.5);", # Venus
           "translateX = 24 * cos(time);" + "translateZ = 24 * sin(time);",         # Earth
           "translateX = 28 * cos(time/2.0);" + "translateZ = 28 * sin(time/2.0);", # Mars
           "translateX = 40 * cos(time/2.5);" + "translateZ = 40 * sin(time/2.5);", # Jupiter
           "translateX = 50 * cos(time/3.0);" + "translateZ = 50 * sin(time/3.0);", # Saturn
           "translateX = 60 * cos(time/3.5);" + "translateZ = 60 * sin(time/3.5);", # Uranus
           "translateX = 68 * cos(time/4.0);" + "translateZ = 68 * sin(time/4.0);", # Neptune
           "translateX = 70 * cos(time/4.5);" + "translateZ = 15 * sin(time/4.5);" + "translateY = 25 * cos(time/4.5);"] # L573
           
systemStr = mc.internalVar(uwd = True)
textures = [systemStr + "default//sourceimages//sun.jpg",
            systemStr + "default//sourceimages//mercury.jpg",
            systemStr + "default//sourceimages//venus.jpg",
            systemStr + "default//sourceimages//earth.jpg",
            systemStr + "default//sourceimages//mars.jpg",
            systemStr + "default//sourceimages//jupiter.jpg",
            systemStr + "default//sourceimages//saturn.jpg",
            systemStr + "default//sourceimages//uranus.jpg",
            systemStr + "default//sourceimages//neptune.png",
            systemStr + "default//sourceimages//pluto.jpg"]

def createFileTexture(filename):
    f = mc.shadingNode('file', asShader = True)
    placement = mc.shadingNode('place2dTexture', asUtility = True)
    mc.connectAttr(placement + ".coverage", f + ".coverage", f = True)
    mc.setAttr (f + ".ftn", filename, type = "string")
    return f

def createSun():
    sun = mc.polySphere(name = planetName[0], radius=sunSize)
    mc.expression(object = sun[0], string = spinEx, name = "sunSpinExpression")
    
    fileNode = createFileTexture(textures[0])
    lambert = mc.shadingNode('lambert', n = "myMat", asShader = True)
    mc.connectAttr(fileNode + ".outColor", lambert + ".color", force = True);
    mySG = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = lambert+"SG")
    mc.connectAttr(lambert + ".outColor", mySG + ".surfaceShader", f=True)
    mc.sets(sun[0], edit = True, forceElement=mySG)

def createPlanet():
    for i in range(planetNum):
        planet = mc.polySphere(name = planetName[i+1], radius = planetSize[i])
        mc.expression(object = planet[0], string = spinEx, name = "planetSpinExpression")
        
        fileNode = createFileTexture(textures[i+1])
        lambert = mc.shadingNode('lambert', n = "myMat", asShader = True)
        mc.connectAttr(fileNode + ".outColor", lambert + ".color", force = True);
        mySG = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = lambert+"SG")
        mc.connectAttr(lambert + ".outColor", mySG + ".surfaceShader", f=True)
        mc.sets(planet[0], edit = True, forceElement=mySG)

def orbitPlanets():
    for i in range(planetNum):
        mc.expression(object = planetName[i+1], string = orbitEx[i], name = str(planetName[i+1]) + "_orbit")

createSun()
createPlanet()
orbitPlanets()