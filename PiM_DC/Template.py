from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
qblock = 5
def init():
	mc = Minecraft.create("127.0.0.1",4711)
	x, y, z = mc.player.getPos()
	return mc
	
def wall1(mc,x,y,z):
	mc.setBlocks(x,y,z,x,y,z,qblock)


def main():
	mc = init()
	x, y, z = mc.player.getPos()
	wall1(mc,x,y,z+8)	
main()
