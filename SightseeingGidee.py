from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'lake': (0,5,0), 
         'river': (32,-43,21),
         'valley': (-4,-14,-23),
         'statue': (8,13,24)}
choice = " "
while choice != "exit":
    choice = input("Enter a location or you can Enter exit to close : ")
    if choice in places:
        location = places[choice]

        x = location[0]
        y = location[1]
        z = location[2]
         
        mc.player.setTilePos(x, y, z) 
