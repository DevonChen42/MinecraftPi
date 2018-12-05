from mcpi.minecraft import Minecraft
from mcpi import block

water = 8
glass = 20
sslab = 44
iron = 42
gobsidian = 246
gstone = 89
air = 0
lapisb = 22
ncore = 247,1

#center = lapis, glass ring = glowstone

mc = Minecraft.create("10.183.3.22",4711)

mc.postToChat("Hallo, here's Sphere, behind you?")

#planet1
radius = 10 #glass
radius1 = 8 #lava
radius2 = 15 #air
radius3 = 17 #glowstone

#planet2
radius4 = 9
radius5 = 5

#planet3
radius6 = 11
radius7 = 9
radius8 = 7

playerPos = mc.player.getPos()
def planet5():
	for x in range(radius2*-1,radius2):
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2: 
					mc.setBlock(playerPos.x + x - 40, playerPos.y + 30, playerPos.z - z + 20, gstone)
						
	for x in range(radius2*-1,radius2):
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2:
					mc.setBlock(playerPos.x + x - 48, playerPos.y + 30, playerPos.z - z + 20, air)
					
	for x in range(radius4*-1,radius4):
			for y in range(radius4*-1, radius4):
				for z in range(radius4*-1,radius4):
					if x**2 + y**2 + z**2 < radius4**2:
						mc.setBlock(playerPos.x + x - 42, playerPos.y + y + 30, playerPos.z - z + 20, glass)
						
	for x in range(radius8*-1,radius8): 
		for y in range(radius8*-1, radius8):
			for z in range(radius8*-1,radius8):
				if x**2 + y**2 + z**2 < radius8**2: 
					mc.setBlock(playerPos.x + x - 42, playerPos.y + y + 30, playerPos.z - z + 20, lapisb) 
						
planet5()
