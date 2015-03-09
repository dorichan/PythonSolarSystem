import maya.cmds as mc

scaleNum=2

nodes=[]
allNodes=[]
wheelNodes=[]

def SelectMeshes():
    mc.select(ado=True)
    
def CreatePolygons():
    mc.polyCube(n="Cube1")
    mc.polyCube(n="Cube2")
    mc.move(4,0,0)
    mc.polyCylinder(n="Cylinder1")
    mc.move(8,0,0)
    mc.polyCone(n="Cone1")
    mc.move(-4,0,0)
    
def CreateWheel():
    wheelNodes=mc.polyCylinder(n="Wheel")
    mc.addAttr(ln="Size", sn="fa", at="float")
    mc.addAttr(ln="isFlat", sn="ba", at="bool")
    
    mc.setAttr(wheelNodes[0] + ".fa", 5.0)
    mc.setAttr(wheelNodes[0] + ".ba", False)
    mc.move(0,5,0)
    print(mc.listAttr(st=["Size","isFlat"]))

#Create some polygons in the scene
CreatePolygons()

#Fill allNodes with everything in the scene
allNodes=mc.ls()
#Print out everything in the scene
print(allNodes)
#Print out the object that matches "Cube1"
print (mc.ls("Cube1",ap=True)) #ap=all paths

SelectMeshes()
nodes=mc.ls(selection=True)
#Scale the selected meshes by 2
mc.scale(scaleNum,scaleNum,scaleNum,nodes)
    
for node in nodes:
    type=mc.nodeType(node)
    print ("\nSelected Node: "+node+" | Type: "+type+"\n")
    
CreateWheel()
