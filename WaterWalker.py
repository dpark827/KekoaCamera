from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    blockquestionmark = mc.getBlock(pos.x,pos.y-1,pos.z)
    if blockquestionmark == 2:
        mc.setBlock(pos.x, pos.y-1, pos.z, 3)
    if blockquestionmark == 1:
        mc.setBlock(pos.x, pos.y-1, pos.z, 4)
    if blockquestionmark == 12:
        mc.setBlock(pos.x, pos.y-1, pos.z, 13)
    if blockquestionmark == 13:
        mc.setBlock(pos.x, pos.y-1, pos.z, 12)
