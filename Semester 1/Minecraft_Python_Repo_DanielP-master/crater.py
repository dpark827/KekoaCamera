from mcpi.minecraft import Minecraft
mc = Minecraft.create()
Answer = "Y"
attempt = input("create a crater? Y/N ")
if attempt == Answer:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x+1,pos.y+1,pos.z+1,pos.x-1,pos.y-1,pos.z-1)
    mc.postToChat("Boom!")
else: mc.postToChat("NoCraterToday!")
