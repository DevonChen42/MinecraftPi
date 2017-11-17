#Ship 
from mcpi.minecraft import Minecraft
from mcpi import*

mc = Minecraft.create()
air = 0
stone = 1
iron = 42
dirt = 3
gold = 41
wood = 17
woodp = 5
leaf = 18
door = 64
stonebrick = 98

x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()  

#circlesize 27
def init():
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()
	return mc
def makedeck():
	mc = init()
	x, y, z = mc.player.getPos()
	mc.setBlocks(x,y-13,z,x,y,z, woodp)
	#mc.setBlocks(x+13,y,z-25,x,y,z+25, woodp)
	mc.setBlocks(x-13,y,z-25,x,y,z+25, woodp)#circle cross
	#mc.setBlocks(x+3,y+13,z,x-3,y+13,z, stonebrick) #up
	#mc.setBlocks(x+4,y-13,z-25,x-4,y-13,z+25, woodp) #down
	#mc.setBlocks(x+13,y+2,z-25,x+13,y-3,z+25, woodp) #right
	#mc.setBlocks(x+13,y,z-25,x+13,y,z+25, wood)
	#mc.setBlocks(x-13,y+2,z-25,x-13,y-3,z+25, woodp) #left
	#mc.setBlocks(x-13,y,z-25,x-13,y,z+25, wood)

	#mc.setBlocks(x+12,y-6,z-25,x+12,y-3,z+25, woodp) #6 #lower left
	#mc.setBlocks(x+11,y-8,z-25,x+11,y-6,z+25, woodp) #8
	#mc.setBlocks(x+10,y-9,z-25,x+10,y-7,z+25, woodp) #9 
	#mc.setBlocks(x+9,y-10,z-25,x+9,y-8,z+25, woodp) #10
	#mc.setBlocks(x+8,y-11,z-25,x+8,y-10,z+25, woodp) #11
	#mc.setBlocks(x+7,y-12,z-25,x+7,y-11,z+25, woodp) #12
	#mc.setBlocks(x+6,y-13,z-25,x+6,y-11,z+25, woodp) #13
	#mc.setBlocks(x+5,y-13,z-25,x+5,y-12,z+25, woodp) #13


	#mc.setBlocks(x-12,y-6,z-25,x-12,y-3,z+25, woodp) #6 #lower right
	#mc.setBlocks(x-11,y-8,z-25,x-11,y-6,z+25, woodp) #8
	#mc.setBlocks(x-10,y-9,z-25,x-10,y-7,z+25, woodp) #9
	#mc.setBlocks(x-9,y-10,z-25,x-9,y-8,z+25, woodp) #10
	#mc.setBlocks(x-8,y-11,z-25,x-8,y-10,z+25, woodp) #11
	#mc.setBlocks(x-7,y-12,z-25,x-7,y-11,z+25, woodp) #12
	#mc.setBlocks(x-6,y-13,z-25,x-6,y-11,z+25, woodp) #13
	#mc.setBlocks(x-5,y-13,z-25,x-5,y-12,z+25, woodp) #13
makedeck()
def main():
	mc = init()
	# mc.player.setPos(0,30,0)
	x, y, z = mc.player.getPos()
	#mc.player.setPos(x, y, z)
	makedeck(mc,x,y,z+20)
main()
#def makenose():
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247

Non-API Blocks
=======================
PAINTING            321
STONE_STAIRS         67
OAK_STAIRS           53
OAK_STAIRS           59
NETHERRACK           87
TRAPDOOR             96
MELON_SEEDS         105
BRICK_STAIRS        108
SANDSTONE_STAIRS    128
STONE_BRICK_STAIRS  109
NETHER_BRICK        112
NETHER_BRICK_STAIRS 114
QUARTZ_BLOCK        155
QUARTZ_STAIRS       156
STONE_CUTTER        245
BONE_MEAL           351
"""
