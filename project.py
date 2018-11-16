from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
water = 8
air = 0
sand = 13
sslab = 44
glass = 20
def init():
	mc = Minecraft.create("127.0.0.1",4711)
	x, y, z = mc.player.getPos()
	return mc
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.player.setPos(mc,x, y, z)
	mc.setBlocks(x+6,y-6,z-6,x+16,y+6,z+6,glass)
	mc.setBlocks(x+7,y-2,z-5,x+15,y+5,z+5,water)

main()	
