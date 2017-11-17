from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
woodp = 5
air = 0



def init():
	mc = Minecraft.create("127.0.0.1",4711)
	x, y, z = mc.player.getPos()
	return mc
	
def hull(mc,x,y,z):
	mc.setBlocks(x,y,z,x,y,z,woodp)
	mc.setBlocks(x-3,y+1,z,x+3,y+1,z,woodp)
	mc.setBlocks(x-5,y+2,z,x+5,y+2,z,woodp)
	mc.setBlocks(x-2,y+2,z,x+2,y+2,z,air)
	mc.setBlocks(x-8,y+3,z,x+8,y+3,z,woodp)
	mc.setBlocks(x-4,y+3,z,x+4,y+3,z,air)
	mc.setBlocks(x-9,y+4,z,x+9,y+4,z,woodp)
	mc.setBlocks(x-7,y+4,z,x+7,y+4,z,air)
	mc.setBlocks(x-10,y+5,z,x+10,y+5,z,woodp)
	mc.setBlocks(x-8,y+5,z,x+8,y+5,z,air)
	mc.setBlocks(x-10,y+6,z,x+10,y+6,z,woodp)
	mc.setBlocks(x-9,y+6,z,x+9,y+6,z,air)
	mc.setBlocks(x-10,y+7,z,x+10,y+7,z,woodp)
	mc.setBlocks(x-9,y+7,z,x+9,y+7,z,air)
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	hull(mc,x,y,z+8)	
main()
