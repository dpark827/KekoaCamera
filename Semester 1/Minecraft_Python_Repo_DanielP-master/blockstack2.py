from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=6
y=5
z=28
blocktype =103
up=1
mc.setBlock(x,y,z,blocktype)
mc.setBlock(x,y+up,z,blocktype)
