import random
from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
<<<<<<< HEAD
<<<<<<< HEAD
#count = 0

while True:
    #print(count)
=======
=======
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd

count = 1
while count <=200000000:
    print(count)
<<<<<<< HEAD
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd
=======
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd
    
    x = random.randint(-127,127)
    y = random.randint(50, 64)
    z = random.randint(-127,127)

<<<<<<< HEAD
<<<<<<< HEAD
    mc.setBlock(x,y,z,8)
=======
=======
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd
    mc.player.setTilePos(x,y,z)

    count += 1

    sleep(0)

    #start water code
    pos=mc.player.getPos()
    mc.setBlock(pos.x,pos.y,pos.z,8)
<<<<<<< HEAD
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd
=======
>>>>>>> 4d34231367e4a64c88cceef639618b98b11ccdbd

    print("loop Finished")
