import maya.cmds as cmds

def printConnectedNodes(node):
    # get the source and NOT destination connections
    src_connections = cmds.listConnections(node, s= True, d = False)
    print 'src: '
    for c in src_connections:
        print c + ','
        print "\n"

# create two nodes
sp=cmds.sphere( n= "mysphere")
cmds.move(3,0,0)
cn=cmds.cone (n ="mycone")

# connect the attributes of the position of the sphere to the #scale of # the cone
cmds.connectAttr(sp[0] + ".tx", cn[0] + ".sy", f=True)
cmds.connectAttr(sp[0] + ".ry", cn[0] + ".ry", f=True)

nodes = cmds.ls(sl=True)
for node in nodes:
    printConnectedNodes(node)