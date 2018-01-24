from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x,y,z):
    mc.setBlocks(x,y,z,x,y+4,z,17)
    mc.setBlocks(x-3,y+3,z-3,x+3,y+6,z+3,18)
