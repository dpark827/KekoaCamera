from mcpi.minecraft import Minecraft
from time import sleep
mc=Minecraft.create()
flower=351
while True:
        x,y,z = mc.player.getPos()
        mc.setBlock(x,y-1,z,flower)
        sleep(0)
