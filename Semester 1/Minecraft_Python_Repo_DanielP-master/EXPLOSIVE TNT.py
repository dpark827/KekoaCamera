from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

#while True:
#block = 51
#mc.setBlocks(-1,20,-1,11,30,11,block)
pos = mc.player.getPos()
block = 46
state = 1
setblock(x+1,y+1,z,block,state)
