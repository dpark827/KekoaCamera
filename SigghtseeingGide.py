from mcpi.minecraft import Minecraft
mc = Minecraft.create()


places = {'shrine': (0,50,0), 
         'lake': (23,34,-12),
         'mountian': (-40,41,32),
         'river': (8,31,-42)}

choice = " "

while choice != "exit":
    choice = input("Enter a location, type exit to close | ")
    if choice in places:
        location = places[choice]
        
        x = location[0]
        y = location[1]
        z = location[2]
        
        mc.player.setTilePos(x, y, z) 
