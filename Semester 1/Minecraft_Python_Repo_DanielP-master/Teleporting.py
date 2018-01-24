import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 11
y = 50
z = 2

mc.player.setTilePos(x, y, z)

time.sleep(10)


x = 21
y = 69
z = 1

mc.player.setTilePos(x, y, z)
