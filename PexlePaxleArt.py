from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
x,y,z=pos.x,pos.y,pos.z

blocks = [[01,01,16,16,01,01,01],
          [02,02,02,02,02,01,01],
          [35,17,35,35,35,02,02],
          [18,18,18,35,35,35,35]]
for row in reversed(blocks):
    for block in row:
        mc.setBlock(x,y,z,block)
        x += 1
    y += 1
    x = pos.x
