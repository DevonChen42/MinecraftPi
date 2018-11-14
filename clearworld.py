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
	mc.setBlocks(x-256,y-256,z-256,x+256,y+256,z+256,air)
	mc.setBlocks(x-256,y-64,z-256,x+256,y-64,z+256,sslab)
main()

def platform():
	mc = init()
	mc.player.setPos(0,5,0)
	x, y, z = mc.player.getPos()
	mc.player.setPos(x, y, z)
	mc.setBlocks(x-3,y-1,z-3,x+3,y+0,z+3,sslab)
platform()
