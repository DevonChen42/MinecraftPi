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
	mc.setBlocks(x,y,z,x,y,z+15,woodp)#0
	mc.setBlocks(x-1,y,z,x+1,y,z+13,woodp)
	mc.setBlocks(x-4,y+1,z+11,x+4,y+1,z+11,woodp)#1
	mc.setBlocks(x-3,y+1,z+13,x+3,y+1,z+13,woodp)
	mc.setBlocks(x-2,y+1,z+14,x+2,y+1,z+14,woodp)
	mc.setBlocks(x-1,y+1,z+16,x+2,y+1,z+16,woodp)
	mc.setBlocks(x,y+1,z+18,x,y+1,z+18,woodp)
	mc.setBlocks(x-7,y+2,z+3,x+7,y+2,z+3,woodp)#2
	mc.setBlocks(x-6,y+2,z+8,x+6,y+2,z+8,woodp)
	mc.setBlocks(x-5,y+2,z+10,x+5,y+2,z+10,woodp)
	mc.setBlocks(x-4,y+2,z+13,x+4,y+2,z+13,woodp)
	mc.setBlocks(x-3,y+2,z+15,x+3,y+2,z+15,woodp)
	mc.setBlocks(x-2,y+2,z+16,x+2,y+2,z+16,woodp)
	mc.setBlocks(x-1,y+2,z+17,x+1,y+2,z+17,woodp)
	mc.setBlocks(x,y+2,z+20,x,y,z,woodp)
	mc.setBlocks(x-8,y+3,z+3,x+8,y+3,z+3,woodp)#3
	mc.setBlocks(x-7,y+3,z+8,x+7,y+3,z+8,woodp)
	mc.setBlocks(x-7,y+3,z+3,x+7,y+3,z+3,air)
	mc.setBlocks(x-6,y+3,z+11,x+6,y+3,z+11,woodp)
	mc.setBlocks(x-6,y+3,z+8,x+6,y+3,z+8,air)
	mc.setBlocks(x-5,y+3,z+14,x+5,y+3,z+14,woodp)
	mc.setBlocks(x-5,y+3,z+10,x+5,y+3,z+20,air)
	mc.setBlocks(x-4,y+3,z+16,x+4,y+3,z+16,woodp)
	mc.setBlocks(x-4,y+3,z+13,x+4,y+3,z+13,air)
	mc.setBlocks(x-3,y+3,z+18,x+3,y+3,z+18,woodp)
	mc.setBlocks(x-3,y+3,z+15,x+3,y+3,z+15,air)
	mc.setBlocks(x-2,y+3,z+19,x+2,y+3,z+19,woodp)
	mc.setBlocks(x-2,y+3,z+16,x+2,y+3,z+16,air)
	mc.setBlocks(x-1,y+3,z+20,x+1,y+3,z+20,woodp)
	mc.setBlocks(x-1,y+3,z+17,x+1,y+3,z+17,air)
	mc.setBlocks(x,y+3,z+21,x,y,z,woodp)
	mc.setBlocks(x,y+3,z+20,x,y,z,air)
	mc.setBlocks(x-9,y+4,z+2,x+9,y+4,z+2,woodp)#4
	mc.setBlocks(x-8,y+4,z+8,x+8,y+4,z+8,woodp)
	mc.setBlocks(x-8,y+4,z+2,x+8,y+4,z+2,air)
	mc.setBlocks(x-7,y+4,z+12,x+7,y+4,z+12,woodp)
	mc.setBlocks(x-7,y+4,z+8,x+7,y+4,z+8,air)
	mc.setBlocks(x-6,y+4,z+15,x+6,y+4,z+15,woodp)
	mc.setBlocks(x-6,y+4,z+11,x+6,y+4,z+11,air)
	mc.setBlocks(x-5,y+4,z+17,x+5,y+4,z+17,woodp)
	mc.setBlocks(x-5,y+4,z+14,x+5,y+4,z+14,air)
	mc.setBlocks(x-4,y+4,z+19,x+4,y+4,z+19,woodp)
	mc.setBlocks(x-4,y+4,z+16,x+4,y+4,z+16,air)
	mc.setBlocks(x-3,y+4,z+20,x+3,y+4,z+20,woodp)
	mc.setBlocks(x-3,y+4,z+18,x+3,y+4,z+18,air)
	mc.setBlocks(x-2,y+4,z+21,x+2,y+4,z+21,woodp)
	mc.setBlocks(x-2,y+4,z+19,x+2,y+4,z+19,air)
	mc.setBlocks(x-1,y+4,z+22,x+1,y+4,z+22,woodp)
	mc.setBlocks(x-1,y+4,z+20,x+1,y+4,z+20,air)
	mc.setBlocks(x,y+4,z+23,x,y+4,z+23,woodp)
	mc.setBlocks(x,y+4,z+22,x,y+4,z+22,air)
	mc.setBlocks(x-9,y+5,z+9,x+9,y+5,z+9,woodp)#5
	mc.setBlocks(x-8,y+5,z+12,x+8,y+5,z+12,woodp)
	mc.setBlocks(x-8,y+5,z+8,x+8,y+5,z+8,air)
	mc.setBlocks(x-7,y+5,z+15,x+7,y+5,z+15,woodp)
	mc.setBlocks(x-7,y+5,z+12,x+7,y+5,z+12,air)
	mc.setBlocks(x-6,y+5,z+17,x+6,y+5,z+17,woodp)
	mc.setBlocks(x-6,y+5,z+15,x+6,y+5,z+15,air)
	mc.setBlocks(x-5,y+5,z+19,x+5,y+5,z+19,woodp)
	mc.setBlocks(x-5,y+5,z+17,x+5,y+5,z+17,air)
	mc.setBlocks(x-4,y+5,z+20,x+4,y+5,z+20,woodp)
	mc.setBlocks(x-4,y+5,z+19,x+4,y+5,z+19,air)
	mc.setBlocks(x-3,y+5,z+21,x+3,y+5,z+21,woodp)
	mc.setBlocks(x-3,y+5,z+20,x+3,y+5,z+20,air)
	mc.setBlocks(x-2,y+5,z+22,x+2,y+5,z+22,woodp)
	mc.setBlocks(x-2,y+5,z+21,x+2,y+5,z+21,air)
	mc.setBlocks(x-1,y+5,z+23,x+1,y+5,z+23,woodp)
	mc.setBlocks(x-1,y+5,z+22,x+1,y+5,z+22,air)
	mc.setBlocks(x,y+5,z+24,x,y,z,woodp)
	mc.setBlocks(x,y+5,z+23,x,y,z,air)
	mc.setBlocks(x-10,y+6,z+7,x+10,y+6,z+7,woodp)#6
	mc.setBlocks(x-9,y+6,z+10,x+9,y+6,z+7,woodp)
	mc.setBlocks(x-9,y+6,z+7,x+9,y+6,z+7,air)
	mc.setBlocks(x-8,y+6,z+15,x+8,y+6,z+15,woodp)
	mc.setBlocks(x-8,y+6,z+12,x+8,y+6,z+12,air)
	mc.setBlocks(x-7,y+6,z+17,x+7,y+6,z+17,woodp)
	mc.setBlocks(x-7,y+6,z+15,x+7,y+6,z+15,air)
	mc.setBlocks(x-6,y+6,z+19,x+6,y+6,z+19,woodp)
	mc.setBlocks(x-6,y+6,z+19,x+6,y+6,z+19,air)
	mc.setBlocks(x-5,y+6,z+20,x+5,y+6,z+20,woodp)
	mc.setBlocks(x-5,y+6,z+19,x+5,y+6,z+19,air)
	mc.setBlocks(x-4,y+6,z+21,x+4,y+6,z+21,woodp)
	mc.setBlocks(x-4,y+6,z+20,x+4,y+6,z+20,air)
	mc.setBlocks(x-3,y+6,z+22,x+3,y+6,z+22,woodp)
	mc.setBlocks(x-3,y+6,z+21,x+3,y+6,z+21,air)
	mc.setBlocks(x-2,y+6,z+23,x+2,y+6,z+23,woodp)
	mc.setBlocks(x-2,y+6,z+22,x+2,y+6,z+22,air)
	mc.setBlocks(x-1,y+6,z+24,x+1,y+6,z+24,woodp)
	mc.setBlocks(x-1,y+6,z+23,x+1,y+6,z+23,air)
	mc.setBlocks(x,y+6,z+25,x,y+6,z,woodp)
	mc.setBlocks(x,y+6,z+24,x,y+6,z,air)
	mc.setBlocks(x-10,y+7,z+10,x+10,y+7,z+10,woodp)#7
	mc.setBlocks(x-9,y+7,z+13,x+9,y+7,z+13,woodp)
	mc.setBlocks(x-9,y+7,z+10,x+9,y+7,z+10,air)
	mc.setBlocks(x-8,y+7,z+16,x+8,y+7,z+16,woodp)
	mc.setBlocks(x-8,y+7,z+15,x+8,y+7,z+15,air)
	mc.setBlocks(x-7,y+7,z+18,x+7,y+7,z+18,woodp)
	mc.setBlocks(x-7,y+7,z+17,x+7,y+7,z+17,air)
	mc.setBlocks(x-6,y+7,z+20,x+6,y+7,z+20,woodp)
	mc.setBlocks(x-6,y+7,z+19,x+6,y+7,z+19,air)
	mc.setBlocks(x-5,y+7,z+21,x+5,y+7,z+21,woodp)
	mc.setBlocks(x-5,y+7,z+20,x+5,y+7,z+20,air)
	mc.setBlocks(x-4,y+7,z+22,x+4,y+7,z+22,woodp)
	mc.setBlocks(x-4,y+7,z+21,x+4,y+7,z+21,air)
	mc.setBlocks(x-3,y+7,z+23,x+3,y+7,z+23,woodp)
	mc.setBlocks(x-3,y+7,z+22,x+3,y+7,z+22,air)
	mc.setBlocks(x-2,y+7,z+24,x+2,y+7,z+24,woodp)
	mc.setBlocks(x-2,y+7,z+23,x+2,y+7,z+23,air)
	mc.setBlocks(x-1,y+7,z+25,x+1,y+7,z+25,woodp)
	mc.setBlocks(x-1,y+7,z+24,x+1,y+7,z+24,air)
	mc.setBlocks(x,y+7,z+26,x,y+7,z,woodp)
	mc.setBlocks(x,y+7,z+25,x,y+7,z,air)
	mc.setBlocks(x-11,y+8,z+6,x+11,y+8,z+6,woodp)#8
	mc.setBlocks(x-10,y+8,z+11,x+10,y+8,z+11,woodp)
	mc.setBlocks(x-10,y+8,z+6,x+10,y+8,z+6,air)
	mc.setBlocks(x-9,y+8,z+14,x+9,y+8,z+14,woodp)
	mc.setBlocks(x-9,y+8,z+13,x+9,y+8,z+13,air)
	mc.setBlocks(x-8,y+8,z+17,x+8,y+8,z+17,woodp)
	mc.setBlocks(x-8,y+8,z+16,x+8,y+8,z+16,air)
	mc.setBlocks(x-7,y+8,z+19,x+7,y+8,z+19,woodp)
	mc.setBlocks(x-7,y+8,z+18,x+7,y+8,z+18,air)
	mc.setBlocks(x-6,y+8,z+20,x+6,y+8,z+20,woodp)
	mc.setBlocks(x-6,y+8,z+19,x+6,y+8,z+19,air)
	mc.setBlocks(x-5,y+8,z+21,x+5,y+8,z+21,woodp)
	mc.setBlocks(x-5,y+8,z+20,x+5,y+8,z+20,air)
	mc.setBlocks(x-4,y+8,z+22,x+4,y+8,z+22,woodp)
	mc.setBlocks(x-4,y+8,z+21,x+4,y+8,z+21,air)
	mc.setBlocks(x-3,y+8,z+23,x+3,y+8,z+23,woodp)
	mc.setBlocks(x-3,y+8,z+22,x+3,y+8,z+22,air)
	mc.setBlocks(x-2,y+8,z+24,x+2,y+8,z+24,woodp)
	mc.setBlocks(x-2,y+8,z+23,x+2,y+8,z+23,air)
	mc.setBlocks(x-1,y+8,z+26,x+1,y+8,z+26,woodp)
	mc.setBlocks(x-1,y+8,z+25,x+1,y+8,z+25,air)
	mc.setBlocks(x,y+8,z+27,x,y,z,woodp)
	mc.setBlocks(x,y+8,z+26,x,y,z,air)
	mc.setBlocks(x-11,y+9,z+11,x+11,y+9,z+11,woodp)#9
	mc.setBlocks(x-10,y+9,z+12,x+10,y+9,z+12,woodp)
	mc.setBlocks(x-10,y+9,z+11,x+10,y+9,z+11,air)
	mc.setBlocks(x-9,y+9,z+15,x+9,y+9,z+15,woodp)
	mc.setBlocks(x-9,y+9,z+15,x+9,y+9,z+15,air)
	mc.setBlocks(x-8,y+9,z+18,x+8,y+9,z+18,woodp)
	mc.setBlocks(x-8,y+9,z+17,x+8,y+9,z+17,air)
	mc.setBlocks(x-7,y+9,z+20,x+7,y+9,z+20,woodp)
	mc.setBlocks(x-7,y+9,z+18,x+7,y+9,z+18,air)
	mc.setBlocks(x-6,y+9,z+21,x+6,y+9,z+21,woodp)
	mc.setBlocks(x-6,y+9,z+20,x+6,y+9,z+20,air)
	mc.setBlocks(x-5,y+9,z+22,x+5,y+9,z+22,woodp)
	mc.setBlocks(x-5,y+9,z+21,x+5,y+9,z+21,air)
	mc.setBlocks(x-4,y+9,z+23,x+4,y+9,z+23,woodp)
	mc.setBlocks(x-4,y+9,z+22,x+4,y+9,z+22,air)
	mc.setBlocks(x-3,y+9,z+24,x+3,y+9,z+24,woodp)
	mc.setBlocks(x-3,y+9,z+23,x+3,y+9,z+23,air)
	mc.setBlocks(x-2,y+9,z+25,x+2,y+9,z+25,woodp)
	mc.setBlocks(x-2,y+9,z+24,x+2,y+9,z+24,air)
	mc.setBlocks(x-1,y+9,z+27,x+1,y+9,z+27,woodp)
	mc.setBlocks(x-1,y+9,z+25,x+1,y+9,z+25,air)
	mc.setBlocks(x,y+9,z+28,x,y,z,woodp)
	mc.setBlocks(x,y+9,z+27,x,y,z,air)
	mc.setBlocks(x-11,y+10,z+12,x+11,y+10,z+12,woodp)#10
	mc.setBlocks(x-10,y+10,z+13,x+10,y+10,z+13,woodp)
	mc.setBlocks(x-10,y+10,z+12,x+10,y+10,z+12,air)
	mc.setBlocks(x-9,y+10,z+17,x+9,y+10,z+17,woodp)
	mc.setBlocks(x-9,y+10,z+15,x+9,y+10,z+15,air)
	mc.setBlocks(x-8,y+10,z+19,x+8,y+10,z+19,woodp)
	mc.setBlocks(x-8,y+10,z+17,x+8,y+10,z+17,air)
	mc.setBlocks(x-7,y+10,z+20,x+7,y+10,z+20,woodp)
	mc.setBlocks(x-7,y+10,z+19,x+7,y+10,z+19,air)
	mc.setBlocks(x-6,y+10,z+21,x+6,y+10,z+21,woodp)
	mc.setBlocks(x-6,y+10,z+20,x+6,y+10,z+20,air)
	mc.setBlocks(x-5,y+10,z+23,x+5,y+10,z+23,woodp)
	mc.setBlocks(x-5,y+10,z+21,x+5,y+10,z+21,air)
	mc.setBlocks(x-4,y+10,z+24,x+4,y+10,z+24,woodp)
	mc.setBlocks(x-4,y+10,z+23,x+4,y+10,z+23,air)
	mc.setBlocks(x-3,y+10,z+25,x+3,y+10,z+25,woodp)
	mc.setBlocks(x-3,y+10,z+24,x+3,y+10,z+24,air)
	mc.setBlocks(x-2,y+10,z+26,x+2,y+10,z+26,woodp)
	mc.setBlocks(x-2,y+10,z+25,x+2,y+10,z+25,air)
	mc.setBlocks(x-1,y+10,z+27,x+1,y+10,z+27,woodp)
	mc.setBlocks(x-1,y+10,z+26,x+1,y+10,z+26,air)
	mc.setBlocks(x,y+10,z+28,x,y,z+28,woodp)
	mc.setBlocks(x,y+10,z+28,x,y,z+28,air)
	mc.setBlocks(x-12,y+11,z+7,x+12,y+11,z+7,woodp)#11
	mc.setBlocks(x-11,y+11,z+10,x+11,y+11,z+10,woodp)
	mc.setBlocks(x-11,y+11,z+7,x+11,y+11,z+7,air)
	mc.setBlocks(x-10,y+11,z+15,x+10,y+11,z+15,woodp)
	mc.setBlocks(x-10,y+11,z+12,x+10,y+11,z+12,air)
	mc.setBlocks(x-9,y+11,z+18,x+9,y+11,z+18,woodp)
	mc.setBlocks(x-9,y+11,z+15,x+9,y+11,z+15,air)
	mc.setBlocks(x-8,y+11,z+19,x+8,y+11,z+19,woodp)
	mc.setBlocks(x-8,y+11,z+18,x+8,y+11,z+18,air)
	mc.setBlocks(x-7,y+11,z+20,x+7,y+11,z+20,woodp)
	mc.setBlocks(x-7,y+11,z+19,x+7,y+11,z+19,air)
	mc.setBlocks(x-6,y+11,z+22,x+6,y+11,z+22,woodp)
	mc.setBlocks(x-6,y+11,z+20,x+6,y+11,z+20,air)
	mc.setBlocks(x-5,y+11,z+23,x+5,y+11,z+23,woodp)
	mc.setBlocks(x-5,y+11,z+22,x+5,y+11,z+22,air)
	mc.setBlocks(x-4,y+11,z+24,x+4,y+11,z+24,woodp)
	mc.setBlocks(x-4,y+11,z+23,x+4,y+11,z+23,air)
	mc.setBlocks(x-3,y+11,z+25,x+3,y+11,z+25,woodp)
	mc.setBlocks(x-3,y+11,z+24,x+3,y+11,z+24,air)
	mc.setBlocks(x-2,y+11,z+26,x+2,y+11,z+26,woodp)
	mc.setBlocks(x-2,y+11,z+25,x+2,y+11,z+25,air)
	mc.setBlocks(x-1,y+11,z+27,x+1,y+11,z+27,woodp)
	mc.setBlocks(x-1,y+11,z+26,x+1,y+11,z+26,air)
	mc.setBlocks(x,y+11,z+28,x,y,z,woodp)
	mc.setBlocks(x,y+10,z+27,x,y,z,air)
	mc.setBlocks(x-12,y+12,z+10,x+12,y+12,z+10,woodp)#12
	mc.setBlocks(x-11,y+12,z+11,x+11,y+12,z+11,woodp)
	mc.setBlocks(x-11,y+12,z+11,x+11,y+12,z+11,air)
	mc.setBlocks(x-10,y+12,z+26,x+10,y+12,z+26,woodp)
	mc.setBlocks(x-10,y+12,z+23,x+10,y+12,z+23,air)
	mc.setBlocks(x-9,y+12,z+28,x+9,y+12,z+28,woodp)
	mc.setBlocks(x-9,y+12,z+26,x+9,y+12,z+26,air)
	mc.setBlocks(x-8,y+12,z+20,x+8,y+12,z+20,woodp)
	mc.setBlocks(x-8,y+12,z+18,x+8,y+12,z+18,air)
	mc.setBlocks(x-7,y+12,z+22,x+7,y+12,z+22,woodp)
	mc.setBlocks(x-7,y+12,z+20,x+7,y+12,z+20,air)
	mc.setBlocks(x-6,y+12,z+24,x+6,y+12,z+24,woodp)
	mc.setBlocks(x-6,y+12,z+23,x+6,y+12,z+23,air)
	mc.setBlocks(x-5,y+12,z+25,x+5,y+12,z+25,woodp)
	mc.setBlocks(x-5,y+12,z+24,x+5,y+12,z+24,air)
	mc.setBlocks(x-4,y+12,z+26,x+4,y+12,z+26,woodp)
	mc.setBlocks(x-4,y+12,z+25,x+4,y+12,z+25,air)
	mc.setBlocks(x-3,y+12,z+27,x+3,y+12,z+27,woodp)
	mc.setBlocks(x-3,y+12,z+26,x+3,y+12,z+26,air)
	mc.setBlocks(x-2,y+12,z+28,x+2,y+12,z+28,woodp)
	mc.setBlocks(x-2,y+12,z+27,x+2,y+12,z+27,air)
	mc.setBlocks(x-1,y+12,z+29,x+1,y+12,z+29,woodp)
	mc.setBlocks(x-1,y+12,z+28,x+1,y+12,z+28,air)
	mc.setBlocks(x,y+12,z+30,x,y,z,woodp)
	mc.setBlocks(x,y+12,z+29,x,y,z,air)
	mc.setBlocks(x-12,y+13,z+11,x+12,y+13,z+11,woodp)#13
	mc.setBlocks(x-11,y+13,z+14,x+11,y+13,z+14,woodp)
	mc.setBlocks(x-11,y+13,z+11,x+11,y+13,z+11,air)
	mc.setBlocks(x-10,y+13,z+26,x+10,y+13,z+26,woodp)
	mc.setBlocks(x-10,y+13,z+24,x+10,y+13,z+24,air)
	mc.setBlocks(x-9,y+13,z+19,x+9,y+13,z+19,woodp)
	mc.setBlocks(x-9,y+13,z+16,x+9,y+13,z+16,air)
	mc.setBlocks(x-8,y+13,z+21,x+8,y+13,z+21,woodp)
	mc.setBlocks(x-8,y+13,z+19,x+8,y+13,z+19,air)
	mc.setBlocks(x-7,y+13,z+22,x+7,y+13,z+22,woodp)
	mc.setBlocks(x-7,y+13,z+21,x+7,y+13,z+21,air)
	mc.setBlocks(x-6,y+13,z+23,x+6,y+13,z+23,woodp)
	mc.setBlocks(x-6,y+13,z+22,x+6,y+13,z+22,air)
	mc.setBlocks(x-5,y+13,z+24,x+5,y+13,z+24,woodp)
	mc.setBlocks(x-5,y+13,z+23,x+5,y+13,z+23,air)
	mc.setBlocks(x-4,y+13,z+25,x+4,y+13,z+25,woodp)
	mc.setBlocks(x-4,y+13,z+24,x+4,y+13,z+24,air)
	mc.setBlocks(x-3,y+13,z+26,x+3,y+13,z+26,woodp)
	mc.setBlocks(x-3,y+13,z+25,x+3,y+13,z+25,air)
	mc.setBlocks(x-2,y+13,z+27,x+2,y+13,z+27,woodp)
	mc.setBlocks(x-2,y+13,z+26,x+2,y+13,z+26,air)
	mc.setBlocks(x-1,y+13,z+28,x+1,y+13,z+28,woodp)
	mc.setBlocks(x-1,y+13,z+27,x+1,y+13,z+27,air)
	mc.setBlocks(x,y+13,z+29,x,y,z,woodp)
	mc.setBlocks(x,y+13,z+28,x,y,z,air)
	mc.setBlocks(x-12,y+14,z+12,x+12,y+14,z+12,woodp)#14
	mc.setBlocks(x-11,y+14,z+14,x+11,y+14,z+14,woodp)
	mc.setBlocks(x-11,y+14,z+12,x+11,y+14,z+12,air)
	mc.setBlocks(x-10,y+14,z+17,x+10,y+14,z+17,woodp)
	mc.setBlocks(x-10,y+14,z+14,x+10,y+14,z+14,air)
	mc.setBlocks(x-9,y+14,z+19,x+9,y+14,z+19,woodp)
	mc.setBlocks(x-9,y+14,z+17,x+9,y+14,z+17,air)
	mc.setBlocks(x-8,y+14,z+21,x+8,y+14,z+21,woodp)
	mc.setBlocks(x-8,y+14,z+19,x+8,y+14,z+19,air)
	mc.setBlocks(x-7,y+14,z+22,x+7,y+14,z+22,woodp)
	mc.setBlocks(x-7,y+14,z+21,x+7,y+14,z+21,air)
	mc.setBlocks(x-6,y+14,z+23,x+6,y+14,z+23,woodp)
	mc.setBlocks(x-6,y+14,z+22,x+6,y+14,z+22,air)
	mc.setBlocks(x-5,y+14,z+24,x+5,y+14,z+24,woodp)
	mc.setBlocks(x-5,y+14,z+23,x+5,y+14,z+23,air)
	mc.setBlocks(x-4,y+14,z+25,x+4,y+14,z+25,woodp)
	mc.setBlocks(x-4,y+14,z+24,x+4,y+14,z+24,air)
	mc.setBlocks(x-3,y+14,z+26,x+3,y+14,z+26,woodp)
	mc.setBlocks(x-3,y+14,z+25,x+3,y+14,z+25,air)
	mc.setBlocks(x-2,y+14,z+27,x+2,y+14,z+27,woodp)
	mc.setBlocks(x-2,y+14,z+26,x+2,y+14,z+26,air)
	mc.setBlocks(x-1,y+14,z+28,x+1,y+14,z+28,woodp)
	mc.setBlocks(x-1,y+14,z+27,x+1,y+14,z+27,air)
	mc.setBlocks(x,y+14,z+29,x,y,z,woodp)
	mc.setBlocks(x,y+14,z+28,x,y,z,air)
	mc.setBlocks(x-12,y+15,z+12,x+12,y+15,z+12,woodp)#15
	mc.setBlocks(x-11,y+15,z+14,x+11,y+15,z+14,woodp)
	mc.setBlocks(x-11,y+15,z+12,x+11,y+15,z+12,air)
	mc.setBlocks(x-10,y+15,z+17,x+10,y+15,z+17,woodp)
	mc.setBlocks(x-10,y+15,z+14,x+10,y+15,z+14,air)
	mc.setBlocks(x-9,y+15,z+19,x+9,y+15,z+19,woodp)
	mc.setBlocks(x-9,y+15,z+17,x+9,y+15,z+17,air)
	mc.setBlocks(x-8,y+15,z+21,x+8,y+15,z+21,woodp)
	mc.setBlocks(x-8,y+15,z+19,x+8,y+15,z+19,air)
	mc.setBlocks(x-7,y+15,z+23,x+7,y+15,z+23,woodp)
	mc.setBlocks(x-7,y+15,z+21,x+7,y+15,z+21,air)
	mc.setBlocks(x-6,y+15,z+24,x+6,y+15,z+24,woodp)
	mc.setBlocks(x-6,y+15,z+23,x+6,y+15,z+23,air)
	mc.setBlocks(x-5,y+15,z+25,x+5,y+15,z+25,woodp)
	mc.setBlocks(x-5,y+15,z+24,x+5,y+15,z+24,air)
	mc.setBlocks(x-4,y+15,z+26,x+4,y+15,z+26,woodp)
	mc.setBlocks(x-4,y+15,z+25,x+4,y+15,z+25,air)
	mc.setBlocks(x-3,y+15,z+27,x+3,y+15,z+27,woodp)
	mc.setBlocks(x-3,y+15,z+26,x+3,y+15,z+26,air)
	mc.setBlocks(x-2,y+15,z+28,x+2,y+15,z+28,woodp)
	mc.setBlocks(x-2,y+15,z+27,x+2,y+15,z+27,air)
	mc.setBlocks(x-1,y+15,z+29,x+1,y+15,z+29,woodp)
	mc.setBlocks(x-1,y+15,z+28,x+1,y+15,z+28,air)
	mc.setBlocks(x,y+15,z+30,x,y,z,woodp)
	mc.setBlocks(x,y+15,z+29,x,y,z,air)
	mc.setBlocks(x-12,y+16,z+14,x+12,y+16,z+14,woodp)#16
	mc.setBlocks(x-11,y+16,z+17,x+11,y+16,z+17,woodp)
	mc.setBlocks(x-11,y+16,z+14,x+11,y+16,z+14,air)
	mc.setBlocks(x-10,y+16,z+19,x+10,y+16,z+19,woodp)
	mc.setBlocks(x-10,y+16,z+17,x+10,y+16,z+17,air)
	mc.setBlocks(x-9,y+16,z+21,x+9,y+16,z+21,woodp)
	mc.setBlocks(x-9,y+16,z+19,x+9,y+16,z+19,air)
	mc.setBlocks(x-8,y+16,z+23,x+8,y+16,z+23,woodp)
	mc.setBlocks(x-8,y+16,z+21,x+8,y+16,z+21,air)
	mc.setBlocks(x-7,y+16,z+24,x+7,y+16,z+24,woodp)
	mc.setBlocks(x-7,y+16,z+23,x+7,y+16,z+23,air)
	mc.setBlocks(x-6,y+16,z+25,x+6,y+16,z+25,woodp)
	mc.setBlocks(x-6,y+16,z+24,x+6,y+16,z+24,air)
	mc.setBlocks(x-5,y+16,z+26,x+5,y+16,z+26,woodp)
	mc.setBlocks(x-5,y+16,z+25,x+5,y+16,z+25,air)
	mc.setBlocks(x-4,y+16,z+27,x+4,y+16,z+27,woodp)
	mc.setBlocks(x-4,y+16,z+26,x+4,y+16,z+26,air)
	mc.setBlocks(x-3,y+16,z+28,x+3,y+16,z+28,woodp)
	mc.setBlocks(x-3,y+16,z+27,x+3,y+16,z+27,air)
	mc.setBlocks(x-2,y+16,z+29,x+2,y+16,z+29,woodp)
	mc.setBlocks(x-2,y+16,z+28,x+2,y+16,z+28,air)
	mc.setBlocks(x-1,y+16,z+30,x+1,y+16,z+30,woodp)
	mc.setBlocks(x-1,y+16,z+29,x+1,y+16,z+29,air)
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	hull(mc,x,y-15,z)	
main()	
	
	
	
	
"""
"The id (or type) of block"

AIR                 = Block(0)
STONE               = Block(1)
GRASS               = Block(2)
DIRT                = Block(3)
COBBLESTONE         = Block(4)
WOOD_PLANKS         = Block(5)
SAPLING             = Block(6)
BEDROCK             = Block(7)
WATER_FLOWING       = Block(8)
WATER               = WATER_FLOWING
WATER_STATIONARY    = Block(9)
LAVA_FLOWING        = Block(10)
LAVA                = LAVA_FLOWING
LAVA_STATIONARY     = Block(11)
SAND                = Block(12)
GRAVEL              = Block(13)
GOLD_ORE            = Block(14)
IRON_ORE            = Block(15)
COAL_ORE            = Block(16)
WOOD                = Block(17)
LEAVES              = Block(18)
GLASS               = Block(20)
LAPIS_LAZULI_ORE    = Block(21)
LAPIS_LAZULI_BLOCK  = Block(22)
SANDSTONE           = Block(24)
BED                 = Block(26)
COBWEB              = Block(30)
GRASS_TALL          = Block(31)
WOOL                = Block(35)
FLOWER_YELLOW       = Block(37)
FLOWER_CYAN         = Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
GOLD_BLOCK          = Block(41)
IRON_BLOCK          = Block(42)
STONE_SLAB_DOUBLE   = Block(43)
STONE_SLAB          = Block(44)
BRICK_BLOCK         = Block(45)
TNT                 = Block(46)
BOOKSHELF           = Block(47)
MOSS_STONE          = Block(48)
OBSIDIAN            = Block(49)
TORCH               = Block(50)
FIRE                = Block(51)
STAIRS_WOOD         = Block(53)
CHEST               = Block(54)
DIAMOND_ORE         = Block(56)
DIAMOND_BLOCK       = Block(57)
CRAFTING_TABLE      = Block(58)
FARMLAND            = Block(60)
FURNACE_INACTIVE    = Block(61)
FURNACE_ACTIVE      = Block(62)
DOOR_WOOD           = Block(64)
LADDER              = Block(65)
STAIRS_COBBLESTONE  = Block(67)
DOOR_IRON           = Block(71)
REDSTONE_ORE        = Block(73)
SNOW                = Block(78)
ICE                 = Block(79)
SNOW_BLOCK          = Block(80)
CACTUS              = Block(81)
CLAY                = Block(82)
SUGAR_CANE          = Block(83)
FENCE               = Block(85)
GLOWSTONE_BLOCK     = Block(89)
BEDROCK_INVISIBLE   = Block(95)
STONE_BRICK         = Block(98)
GLASS_PANE          = Block(102)
MELON               = Block(103)
FENCE_GATE          = Block(107)
GLOWING_OBSIDIAN    = Block(246)
NETHER_REACTOR_CORE = Block(247)

.data
"The data (or sub-type) of a block"

Data Values of blocks:
WOOL:
0: White
1: Orange
2: Magenta
3: Light Blue
4: Yellow
5: Lime
6: Pink
7: Grey
8: Light grey
9: Cyan
10: Purple
11: Blue
12: Brown
13: Green
14: Red
15:Black

WOOD:
0: Oak (up/down)
1: Spruce (up/down)
2: Birch (up/down)
(below not on Pi)
3: Jungle (up/down)
4: Oak (east/west)
5: Spruce (east/west)
6: Birch (east/west)
7: Jungle (east/west)
8: Oak (north/south)
9: Spruce (north/south)
10: Birch (north/south)
11: Jungle (north/south)
12: Oak (only bark)
13: Spruce (only bark)
14: Birch (only bark)
15: Jungle (only bark)

WOOD_PLANKS (Not on Pi):
0: Oak
1: Spruce
2: Birch
3: Jungle

SAPLING:
0: Oak
1: Spruce
2: Birch
3: Jungle (Not on Pi)

GRASS_TALL:
0: Shrub
1: Grass
2: Fern
3: Grass (color affected by biome) (Not on Pi)

TORCH:
1: Pointing east
2: Pointing west
3: Pointing south
4: Pointing north
5: Facing up

STONE_BRICK:
0: Stone brick
1: Mossy stone brick
2: Cracked stone brick
3: Chiseled stone brick

STONE_SLAB / STONE_SLAB_DOUBLE:
0: Stone
1: Sandstone
2: Wooden
3: Cobblestone
4: Brick
5: Stone Brick
Below - not on Pi
6: Nether Brick
7: Quartz

Not on Pi
SNOW_BLOCK:
0-7: Height of snow, 0 being the lowest, 7 being the highest.

TNT:
0: Inactive
1: Ready to explode

LEAVES:
1: Oak leaves
2: Spruce leaves
3: Birch leaves

SANDSTONE:
0: Sandstone
1: Chiseled sandstone
2: Smooth sandstone

STAIRS_[COBBLESTONE, WOOD]:
0: Ascending east
1: Ascending west
2: Ascending south
3: Ascending north
4: Ascending east (upside down)
5: Ascending west (upside down)
6: Ascending south (upside down)
7: Ascending north (upside down)

LADDERS, CHESTS, FURNACES, FENCE_GATE:
2: Facing north
3: Facing south
4: Facing west
5: Facing east

[WATER, LAVA]_STATIONARY:
0-7: Level of the water, 0 being the highest, 7 the lowest

NETHER_REACTOR_CORE:
0: Unused
1: Active
2: Stopped / used up
"""
