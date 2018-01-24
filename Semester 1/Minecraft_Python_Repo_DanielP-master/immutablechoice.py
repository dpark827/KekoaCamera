from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Do you want blocks to be immutable? Y/N")

if answer == "Y":
    print("World is now immutable")
    mc.setting("world_immutable", True)
    mc.postToChat("World Is Now Immutable")
else:
    print("World is now breakable.")
    mc.setting("world_immutable", False)
    mc.postToChat("World is now breakable.")
