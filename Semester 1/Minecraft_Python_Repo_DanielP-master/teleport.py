from mcpi.minecraft import Minecraft
mc= Minecraft.create()
x=10
y=110
z=12
mc.player.setTilePos(x,y,z)
import time
mc.player.setTilePos(x+5,y+5,z+5)
time.sleep(5)
mc.player.setTilePos(x+10,y,z+10)
time.sleep(5)
