from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

while True:
    x += random.uniform(-2,2)#these numbers are normally -0.2,0.2, but
    z += random.uniform(-2,2)#these numbers make for a fun experience.
    y = mc.getHeight(x,z)

    mc.player.setPos(x,y,z)
    time.sleep(0.1)
