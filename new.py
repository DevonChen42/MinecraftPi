from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

water = 8
glass = 20
sslab = 44
iron = 42
gstone = 89
lava = 10
air = 0
gobsidian = 246
ncore = 247,1
lapisb = 22
snow = 78

mc = Minecraft.create("127.0.0.1",4711)

mc.postToChat("Get oofed on")
#planet1
radius = 10 #glass
radius1 = 8 #lava
radius2 = 15 #air
radius3 = 17 #glowstone

#planet2
radius4 = 9
radius5 = 7

#planet3
radius6 = 11
radius7 = 9
radius8 = 7


playerPos = mc.player.getPos()


class walking:
	def walk():

		while True:
			x, y, z = mc.player.getPos()
			mc.setBlock(x, y, z-1, snow)
	walk()
	def wipe():
		
		while True:
			x, y, z = mc.player.getPos()
			mc.setBlock(x, y, z-1, x, y, z, air)
			sleep()
	
