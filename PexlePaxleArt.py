from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
x,y,z=pos.x,pos.y,pos.z

blocks = [[1,1,16,16,1,1,1,1],
          [2,2,2,2,2,3,1,1],
          [35,17,35,35,35,2,2,2],
          [18,18,18,35,35,35,35,35],
          [18,18,18,35,35,35,35,35]]
for row in blocks:
    for block in row:
        mc.setBlock(x,y,z,block)
        x += 1
    y += 1
    x = pos.x
