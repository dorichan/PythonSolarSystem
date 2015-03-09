#UI/DAGnode Classwork (Week 5-6)
import maya.cmds as mc
from functools import partial

mc.group(em=True,name="Group1")

#Create window
mc.window(title="Classwork (UI)", widthHeight=(500,200))
mc.columnLayout(columnAttach=("left", 2))

def CreateCylinder():
    cy=mc.polyCylinder(name="Cylinder")
    mc.parent(cy, "Group1")

def GetChildren(DAGnode, *args):
    print("Selected " + str(DAGnode))
    for node in DAGnode:
        children=mc.listRelatives(DAGnode, type="transform", c=True)
        print(children)
        return children
    
def GetParents(DAGnode, *args):
    print("Selected " + str(DAGnode))
    for node in DAGnode:
        parents=mc.listRelatives(DAGnode, type="transform", p=True)
        print(parents)
        return parents
    
def AddFloats(*args):
    result = mc.intField(first, q=True, v=True) + mc.intField(second, q=True, v=True)
    print(result)
    Update(result)
    
def Update(result):
    mc.text("\nResult")
    mc.intField(value=result)
    
def DeleteAll(*args):
    mc.select(all=True)
    mc.delete()
   
#Slider controls
yScale=mc.floatSliderGrp(label="Y Scale", field= True, value = 0)
mc.connectControl(yScale, "Cylinder" + ".scaleY")

#Int entry for simple addition
mc.text("First")
first=mc.intField(value=1, changeCommand=AddFloats)
mc.text("Second")
second=mc.intField(value=0, changeCommand=AddFloats)

mc.button(l="Find Children",width=110, command=partial(GetChildren, mc.ls(sl=True)))
mc.button(l="Find Parents",width=110, command=partial(GetParents, mc.ls(sl=True)))
mc.button(l="Delete All",width=110, command=DeleteAll)

#Display window
mc.showWindow()

#Create polygon
CreateCylinder()
CreateCylinder()
mc.move(2,0,0)