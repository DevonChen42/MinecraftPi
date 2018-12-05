from mcpi.minecraft import Minecraft
from mcpi import block

water = 8
glass = 20
sslab = 44
iron = 42
gstone = 89
lava = 10
air = 0
gobsidian = 246
ncore = 247,1
lapisb = 22

mc = Minecraft.create("10.183.3.22",4711)

mc.postToChat("Get oofed on")
#planet1
radius = 10 #glass
radius1 = 8 #lava
radius2 = 15 #air
radius3 = 17 #glowstone

#planet2
radius4 = 9
radius5 = 5

#planet3
radius6 = 11
radius7 = 9
radius8 = 7


playerPos = mc.player.getPos()
def planet1():
	for x in range(radius3*-1,radius3):#glowstone
		for y in range(radius3*-1, radius3):
			for z in range(radius3*-1,radius3):
				if x**2 + y**2 + z**2 < radius3**2: 
					mc.setBlock(playerPos.x + x, playerPos.y + y + 60, playerPos.z - z + 50, gstone)
					
	for x in range(radius2*-1,radius2):#air
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2:
					mc.setBlock(playerPos.x + x, playerPos.y + y + 60, playerPos.z - z + 50, air)

	for x in range(radius*-1,radius): #Creates box | glass
		for y in range(radius*-1, radius):
			for z in range(radius*-1,radius):
				if x**2 + y**2 + z**2 < radius**2: #Creates curvature for the sphere
					mc.setBlock(playerPos.x + x, playerPos.y + y + 60, playerPos.z - z + 50, glass) #Sets spawn position for the sphere
					
	for x in range(radius1*-1,radius1):#lava
		for y in range(radius1*-1, radius1):
			for z in range(radius1*-1,radius1):
				if x**2 + y**2 + z**2 < radius1**2:
					mc.setBlock(playerPos.x + x, playerPos.y + y + 60, playerPos.z - z + 50, lava)
planet1()

def planet2():
		for x in range(radius4*-1,radius4):#glass
			for y in range(radius4*-1, radius4):
				for z in range(radius4*-1,radius4):
					if x**2 + y**2 + z**2 < radius4**2: 
						mc.setBlock(playerPos.x + x, playerPos.y + y + 45, playerPos.z - z - 45, glass)
		for x in range(radius5*-1,radius5):#glowing obsidian
			for y in range(radius5*-1, radius5):
				for z in range(radius5*-1,radius5):
					if x**2 + y**2 + z**2 < radius5**2: 
						mc.setBlock(playerPos.x + x, playerPos.y + y + 45, playerPos.z - z - 45, gobsidian)
planet2()

def planet3():
	for x in range(radius3*-1,radius3):#glowstone
		for y in range(radius3*-1, radius3):
			for z in range(radius3*-1,radius3):
				if x**2 + y**2 + z**2 < radius3**2: 
					mc.setBlock(playerPos.x + x + 40, playerPos.y + 30, playerPos.z - z + 20, ncore)
						
	for x in range(radius2*-1,radius2):#air
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2:
					mc.setBlock(playerPos.x + x + 40, playerPos.y + 30, playerPos.z - z + 20, air)
	for x in range(radius*-1,radius): #Creates box | glass
		for y in range(radius*-1, radius):
			for z in range(radius*-1,radius):
				if x**2 + y**2 + z**2 < radius**2: #Creates curvature for the sphere
					mc.setBlock(playerPos.x + x + 40, playerPos.y + y + 30, playerPos.z - z + 20, gstone) #Sets spawn position for the sphere
						
planet3()


def planet4():
	for x in range(radius2*-1,radius2):
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2: 
					mc.setBlock(playerPos.x + x + 40, playerPos.y + 30, playerPos.z - z + 20, gstone)
						
	for x in range(radius2*-1,radius2):
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2:
					mc.setBlock(playerPos.x + x + 45, playerPos.y + 30, playerPos.z - z + 20, air)
					
	for x in range(radius4*-1,radius4):
			for y in range(radius4*-1, radius4):
				for z in range(radius4*-1,radius4):
					if x**2 + y**2 + z**2 < radius4**2:
						mc.setBlock(playerPos.x + x + 43, playerPos.y + y + 30, playerPos.z - z + 20, glass)
						
	for x in range(radius8*-1,radius8): 
		for y in range(radius8*-1, radius8):
			for z in range(radius8*-1,radius8):
				if x**2 + y**2 + z**2 < radius8**2: 
					mc.setBlock(playerPos.x + x + 43, playerPos.y + y + 30, playerPos.z - z + 20, lapisb) 
						
planet4()
def planet5():
	for x in range(radius2*-1,radius2):
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2: 
					mc.setBlock(playerPos.x + x - 40, playerPos.y + 30, playerPos.z - z + 20, gstone)
						
	for x in range(radius2*-1,radius2):
		for y in range(radius2*-1, radius2):
			for z in range(radius2*-1,radius2):
				if x**2 + y**2 + z**2 < radius2**2:
					mc.setBlock(playerPos.x + x - 48, playerPos.y + 30, playerPos.z - z + 20, air)
					
	for x in range(radius4*-1,radius4):
			for y in range(radius4*-1, radius4):
				for z in range(radius4*-1,radius4):
					if x**2 + y**2 + z**2 < radius4**2:
						mc.setBlock(playerPos.x + x - 42, playerPos.y + y + 30, playerPos.z - z + 20, glass)
						
	for x in range(radius8*-1,radius8): 
		for y in range(radius8*-1, radius8):
			for z in range(radius8*-1,radius8):
				if x**2 + y**2 + z**2 < radius8**2: 
					mc.setBlock(playerPos.x + x - 42, playerPos.y + y + 30, playerPos.z - z + 20, lapisb) 
						
planet5()

'''
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
IRON_SHOVEL = id(256),
            IRON_PICKAXE = id(257),
            IRON_AXE = id(258),
            BOW = id(261),
            ARROW = id(262),
            COAL = id(263),
            DIAMOND = id(264),
            IRON_INGOT = id(265),
            GOLD_INGOT = id(266),
            IRON_SWORD = id(267),
            WOODEN_SWORD = id(268),
            WOODEN_SHOVEL = id(269),
            WOODEN_PICKAXE = id(270),
            WOODEN_AXE = id(271),
            STONE_SWORD = id(272),
            STONE_SHOVEL = id(273),
            STONE_PICKAXE = id(274),
            STONE_AXE = id(275),
            DIAMOND_SWORD = id(276),
            DIAMOND_SHOVEL = id(277),
            DIAMOND_PICKAXE = id(278),
            DIAMOND_AXE = id(279),
            STICK = id(280),
            BOWL = id(281),
            GOLD_SWORD = id(283),
            GOLD_SHOVEL = id(284),
            GOLD_PICKAXE = id(285),
            GOLD_AXE = id(286),
            STRING = id(287),
            FEATHER = id(288),
            GUNPOWDER = id(289),
            FLINT = id(292),
            WHEAT = id(296),
            SIGN = id(323),
            WOODEN_DOOR = id(324),
            IRON_DOOR = id(330),
            SNOWBALL = id(332),
            LEATHER = id(334),
            CLAY_BRICK = id(336),
            CLAY = id(337),
            SUGAR_CANE = id(338),
            PAPER = id(339),
            BOOK = id(340),
            SLIMEBALL = id(341),
            EGG = id(344),
            COMPASS = id(345),
            CLOCK = id(347),
            GLOWSTONE_DUST = id(348),
            DYE = id(351),
            BONE = id(352),
            SUGAR = id(353),
            SHEARS = id(359),
            CAMERA = id(456);
'''
'''
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
'''
