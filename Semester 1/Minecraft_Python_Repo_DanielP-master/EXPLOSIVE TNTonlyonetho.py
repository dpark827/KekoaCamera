from mcpi.minecraft import Minecraft
from time import sleep
import random
mc = Minecraft.create()

while True:
    #block = 51
    #mc.setBlocks(-1,20,-1,11,30,11,block)
    pos = mc.player.getPos()
    block = 46
    state = 1
    x = random.randint(-100,100)
    y = random.randint(-50,50)
    z = random.randint(-100,100)
    mc.setBlock(x,y,z,block,state)
    print(x)
    print(y)
    print(z)
