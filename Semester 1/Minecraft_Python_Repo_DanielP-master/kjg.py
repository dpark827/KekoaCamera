from mcpi.minecraft import Minecraft
mc = Minecraft.create

password = "cats"
attempt = input("Please enter the password: ")
tnt = 1
while attempt != password:
    attempt = input("Please enter the password: ")
    if attempt == password:
        print("Password is correct")
        
    else:
        print("Password is incorrect")
        tnt=tnt+1
    if tnt==10:
        pos=mc.player.getTilePos()
        setblocks(pos.x-10,pos.y-10,pos.z-10,pos.x+10,pos.y+10,pos.z+10,46,1)
print("Program finished")
