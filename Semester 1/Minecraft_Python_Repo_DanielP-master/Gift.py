from mcpi.minecraft import Minecraft
import time
from time import sleep
mc = Minecraft.create()
x = 10
y = 11
z = 12
gift = mc.getBlock(x,y,z)
print (gift)
while True:
    if gift == 57:
        mc.postToChat("Diamonds To You!")
        time.sleep(3)
    elif gift == 6:
        mc.postToChat("Thats An Alright Gift, I Guess?")
        time.sleep(3)
    else:
        mc.postToChat("Bring A Gift To " + str(x) + "," +str(y) + "," + str(z) + ".")
        mc.setBlock(x,y,z,1)
        time.sleep(3)
