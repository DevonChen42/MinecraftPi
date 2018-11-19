from mcpi.minecraft import Minecraft
from mcpi import block

water = 8
glass = 20
sslab = 44
iron = 42

mc = Minecraft.create("10.183.0.67",4711)

mc.postToChat("Hallo, here's Sphere")

radius = 20
radius1 = 17

playerPos = mc.player.getPos()

for x in range(radius*-1,radius): #Creates box
	for y in range(radius*-1, radius):
		for z in range(radius*-1,radius):
			if x**2 + y**2 + z**2 < radius**2: #Creates curvature for the sphere
				mc.setBlock(playerPos.x + x, playerPos.y + y + radius, playerPos.z - z - 10, glass) #Sets spawn position for the sphere
				
for x in range(radius1*-1,radius1):
	for y in range(radius1*-1, radius1):
		for z in range(radius1*-1,radius1):
			if x**2 + y**2 + z**2 < radius1**2:
				mc.setBlock(playerPos.x + x, playerPos.y + y + radius, playerPos.z - z - 10, iron)

