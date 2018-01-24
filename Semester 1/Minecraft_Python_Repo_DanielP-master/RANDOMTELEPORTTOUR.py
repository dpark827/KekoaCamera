import random
from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 1
while count <=200000000:
    print(count)
    
    x = random.randint(-127,127)
    y = random.randint(50, 64)
    z = random.randint(-127,127)

    mc.player.setTilePos(x,y,z)

    count += 1

    sleep(0.1)

    #start water code
    pos=mc.player.getPos()
    mc.setBlock(pos.x,pos.y,pos.z,8)

    print("loop Finished")
