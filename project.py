from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
water = 8
air = 0
sand = 13
sslab = 44
def init():
	mc = Minecraft.create("127.0.0.1",4711)
	x, y, z = mc.player.getPos()
	return mc
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.player.setPos(x, y, z)
	mc.setBlocks(x+2,y-5,z-5,x+2,y+5,z+5,water)
	mc.setBlocks(x+3,y-6,z-6,x+3,y+6,z+6,glass)
main()
