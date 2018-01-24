from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
pos = mc.player.getTilePos()
while True:
    pos = mc.player.getTilePos()
    if int(pos.x) == 10:
        mc.setBlocks(10,pos.y-1,pos.z,10,pos.y-300,pos.z,1)
