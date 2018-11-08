from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

water = 8
air = 0
sand = 13
sslab = 44
qblock = 155
qcolumn = 155,2
qstair = 156
qstairZp = 156,2
qstairYn = 156,6
glassp = 102
def init():
	mc = Minecraft.create("127.0.0.1",4711)
	x, y, z = mc.player.getPos()
	return mc
def center1(mc,x,y,z):
	mc.setBlocks(x,y,z,x,y+4,z,qblock)
def wall1(mc,x,y,z):
	mc.setBlocks(x-7,y,z,x+7,y+4,z,qblock)
	mc.setBlocks(x-2,y+4,z,x+2,y+2,z,qcolumn)
	mc.setBlocks(x-6,y+1,z,x+6,y+2,z,glassp)
	mc.setBlocks(x-6,y,z,x+6,y,z,qstairZp)
	mc.setBlocks(x-6,y+3,z,x+6,y+3,z,qstairYn)
	mc.setBlocks(x-4,y,z,x+4,y+4,z,qblock)
	mc.setBlocks(x-2,y+1,z,x+2,y+2,z,glassp)
	mc.setBlocks(x-2,y+3,z,x+2,y+3,z,qstairYn)
	mc.setBlocks(x-2,y,z,x+2,y,z,qstairZp)
	
		
	#mc.setBlocks(x-4,y,z,x+4,y+5,z+8,qblock)
	#mc.setBlocks(x-2,y,z,x+2,y+5,z+8,qcolumn)
	#mc.setBlocks(x-2,y+3,z+8,x+2,y+3,z+8,qstairYn)
	#mc.setBlocks(x-2,y,z+8,x+2,y+2,z+8,glassp)
	#mc.setBlocks(x-2,y,z+8,x+2,y,z+8,qstairZp)		
	#mc.setBlocks(x-5,y,z,x+5,y+5,z+7,air)
def main():
	mc = init()
	# mc.player.setPos(0,30,0)
	x, y, z = mc.player.getPos()
	#mc.player.setPos(x, y, z)
	wall1(mc,x,y,z+8)
	center1(mc,x,y,z+8)
main()


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
