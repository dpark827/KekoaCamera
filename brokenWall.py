from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

pos = mc.player.getTilePos()
x,y,z=pos.x,pos.y,pos.z

walllength = 10
wallheight = 5

xcounter=0
ycounter=0

for walllength:
    brokenBlocks = [48,67,4,4,4,4]
    block = random.choice(brokenBlocks)
    mc.setBlock(x+xcounter,y,z,block)
    xcounter+=1
