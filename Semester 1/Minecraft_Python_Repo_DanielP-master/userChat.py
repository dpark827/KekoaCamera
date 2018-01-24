from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input("message.")
mc.postToChat(message)
