from mcpi.minecraft import Minecraft
mc = Minecraft.create()

Pos=mc.player.getPos()

block10=mc.getBlockWithData(Pos.x,Pos.y-1,Pos.z)
block20=mc.getBlockWithData(Pos.x+1,Pos.y-1,Pos.z)
block30=mc.getBlockWithData(Pos.x,Pos.y-1,Pos.z+1)
block40=mc.getBlockWithData(Pos.x+1,Pos.y-1,Pos.z+1)
block11=mc.getBlockWithData(Pos.x,Pos.y,Pos.z)
block21=mc.getBlockWithData(Pos.x+1,Pos.y,Pos.z)
block31=mc.getBlockWithData(Pos.x,Pos.y,Pos.z+1)
block41=mc.getBlockWithData(Pos.x+1,Pos.y,Pos.z+1)
input("Respond to place selected blocks!")
Pos=mc.player.getPos()
mc.setBlock(Pos.x,Pos.y-1,Pos.z,block10)
mc.setBlock(Pos.x+1,Pos.y-1,Pos.z,block20)
mc.setBlock(Pos.x,Pos.y-1,Pos.z+1,block30)
mc.setBlock(Pos.x+1,Pos.y-1,Pos.z+1,block40)
mc.setBlock(Pos.x,Pos.y,Pos.z,block11)
mc.setBlock(Pos.x+1,Pos.y,Pos.z,block21)
mc.setBlock(Pos.x,Pos.y,Pos.z+1,block31)
mc.setBlock(Pos.x+1,Pos.y,Pos.z+1,block41)
#this program will take a 2x2 cube of 4 blocks and copy them
"""
    Diagram
    x = any block, p = player position

    [x][xp] sideview
    [x][x]

    [x][xp] topview
    [x][x]

    [x][xp] backview
    [x][x]
"""
