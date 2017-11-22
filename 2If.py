from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import threading
wood = 17
woodp = 5
air = 0
sslab = 44
bslab = 44,5
dsslab = 43
dbslab = 43,5
sstairs = 67
wslab = 44,2
sbrick = 98


def init():
	mc = Minecraft.create("127.0.0.1",4711)
	x, y, z = mc.player.getPos()
	return mc
	
def chest(mc,x,y,z):
	mc.setBlocks(x+2,y+3,z+7,x,y,z,wood)#body
	mc.setBlocks(x+2,y+3,z+6,x,y,z,woodp)
	mc.setBlocks(x+2,y+3,z,x,y,z,wood)
	mc.setBlocks(x+3,y+3,z+7,x+5,y,z,woodp)
	mc.setBlocks(x+3,y+3,z+6,x+5,y,z,air)
	mc.setBlocks(x+6,y+3,z+7,x,y,z,wood)
	mc.setBlocks(x+6,y+3,z+6,x,y,z,woodp)
	mc.setBlocks(x+6,y+3,z,x,y,z,wood)
	
	mc.setBlocks(x+2,y+5,z+7,x,y,z,dsslab)#ring
	mc.setBlocks(x+2,y+5,z+4,x,y,z,sbrick)
	mc.setBlocks(x+2,y+5,z+3,x,y,z,dsslab)
	mc.setBlocks(x+3,y+5,z+7,x+6,y,z,dsslab)
	mc.setBlocks(x+4,y+5,z+6,x+5,y,z,air)
	mc.setBlocks(x+6,y+5,z+7,x,y,z,dsslab)
	mc.setBlocks(x+6,y+5,z+6,x,y,z,dbslab)
	mc.setBlocks(x+6,y+5,z+5,x,y,z,dsslab)
	mc.setBlocks(x+6,y+5,z+2,x,y,z,dbslab)
	mc.setBlocks(x+6,y+5,z,x,y,z,dsslab)
	mc.setBlocks(x+2,y+6,z+7,x,y,z,wood)#lid
	mc.setBlocks(x+2,y+6,z+6,x,y,z,woodp)
	mc.setBlocks(x+2,y+6,z,x,y,z,wood)
	mc.setBlocks(x+3,y+6,z+7,x+5,y,z,woodp)
	mc.setBlocks(x+6,y+6,z+7,x,y,z,wood)
	mc.setBlocks(x+6,y+6,z+6,x,y,z,woodp)
	mc.setBlocks(x+6,y+6,z,x,y,z,wood)
	mc.setBlocks(x+3,y+7,z+7,x+5,y,z,wood)
	mc.setBlocks(x+3,y+7,z+6,x+5,y,z,woodp)
	mc.setBlocks(x+3,y+7,z,x+5,y,z,wood)

def openChest(mc,x,y,z):
	mc.setBlocks(x+2,y+3,z+7,x,y,z,wood)#body
	mc.setBlocks(x+2,y+3,z+6,x,y,z,woodp)
	mc.setBlocks(x+2,y+3,z,x,y,z,wood)
	mc.setBlocks(x+3,y+3,z+7,x+5,y,z,woodp)
	mc.setBlocks(x+3,y+3,z+6,x+5,y,z,air)
	mc.setBlocks(x+3,y+3,z,x+5,y,z,woodp)
	mc.setBlocks(x+6,y+3,z+7,x,y,z,wood)
	mc.setBlocks(x+6,y+3,z+6,x,y,z,woodp)
	mc.setBlocks(x+6,y+3,z,x,y,z,wood)
	#mc.setBlocks(x+2,y,z,x+6,y+22,z,woodp)Check
	mc.setBlocks(x+2,y+5,z+7,x,y,z,sslab)#ring
	mc.setBlocks(x+2,y+5,z+4,x,y,z,sstairs)
	mc.setBlocks(x+2,y+5,z+3,x,y,z,sslab)
	mc.setBlocks(x+3,y+5,z+7,x+6,y,z,sslab)
	mc.setBlocks(x+4,y+5,z+6,x+5,y,z,air)
	mc.setBlocks(x+6,y+5,z+7,x,y,z,sslab)
	mc.setBlocks(x+6,y+5,z+6,x,y,z,bslab)
	mc.setBlocks(x+6,y+5,z+5,x,y,z,sslab)
	mc.setBlocks(x+6,y+5,z+2,x,y,z,bslab)
	mc.setBlocks(x+6,y+5,z,x,y,z,dsslab)
	mc.setBlocks(x+2,y+5,z+7,x+6,y+5,z,air)#lid gone
	mc.setBlocks(x,y,z,x,y,z,woodp)#lid open

def main():
	mc = init()
	x, y, z = mc.player.getPos()
	chest(mc,x,y+10,z)
	openChest(mc,x,y,z+10)	
main()	
