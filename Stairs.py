from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()
x,y,z = pos.x, pos.y, pos.z

l = 0

while True:
    #pos = mc.player.getTilePos()
    #x,y,z = pos.x, pos.y, pos.z

    stairBlock = 53
    
    step = 0
    while step < 1000:
        mc.setBlock(x+step+l,y+step,z,stairBlock)
        step += 1
    x -= 1
