from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
<<<<<<< HEAD
<<<<<<< HEAD
#while True:
pos =mc.player.getPos()
mc.setBlocks(-200,50,-200,200,100,200,12)
=======
while True:
    pos =mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd
=======
while True:
    pos =mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd
