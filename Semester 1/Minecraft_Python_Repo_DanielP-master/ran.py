from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Do you want blocks to be immutable? Y/N")

if answer == "Y":
    print("world is now immutable")

mc.setting("world_immutable", False)
mc.postToChat("World Is Immutable")
