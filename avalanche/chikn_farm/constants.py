from decimal import Decimal

CHIKN_RARITY_LIST = [
    "Unique",
    "Legendary",
    "Elite",
    "Rare",
    "Nice",
    "Common",
]

FARMLAND_TILE_DICT = {
    "pyramid_Annuit": {
        "name": "Annuit Cœptis",
        "chance": 0.00148038490007402,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Pyramid_B_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Pyramid_B_0000.png",
        "resources": [{"name": "Dark Matter", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "pyramid_Avax": {
        "name": "AVAX Pyramid",
        "chance": 0.00148038490007402,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Pyramid_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Pyramid_A_0000.png",
        "resources": [{"name": "Avaxium", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "BoneDaddy": {
        "name": "Bone Daddy",
        "chance": 0.00148038490007402,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_BoneDaddy_0003.png",
        "image": "/api/farmland/tiles/image/Farmland_05_BoneDaddy_0003.png",
        "resources": [{"name": "Gold", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Goldmine": {
        "name": "Abandoned Mine",
        "chance": 0.00296076980014804,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Goldmine_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Goldmine_0000.png",
        "resources": [{"name": "Gold", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "ChiknMountain": {
        "name": "chikn Mountain",
        "chance": 0.00296076980014804,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_ChiknMountain_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_ChiknMountain_0000.png",
        "resources": [{"name": "Mana", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Excalibur": {
        "name": "Excalibur",
        "chance": 0.00296076980014804,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Excalibur_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Excalibur_0000.png",
        "resources": [{"name": "Tungsten", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Meteor": {
        "name": "Space Rock",
        "chance": 0.00296076980014804,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Meteor_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Meteor_0000.png",
        "resources": [{"name": "Dark Matter", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Tungsten": {
        "name": "Tungsten Cube",
        "chance": 0.00296076980014804,
        "rarity": "Legendary",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Tungsten_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Tungsten_0000.png",
        "resources": [{"name": "Tungsten", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Ruin": {
        "name": "Ancient Ruins",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Ruin_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Ruin_A_0000.png",
        "resources": [{"name": "Mana", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Red_Windmill": {
        "name": "Big Red Windmill",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Windmill_B_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Windmill_B_0000.png",
        "resources": [{"name": "Avaxium", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Golf": {
        "name": "Birdie",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Golf_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Golf_0000.png",
        "resources": [{"name": "Avaxium", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Graveyard": {
        "name": "Haunted Graveyard",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Graveyard_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Graveyard_0000.png",
        "resources": [{"name": "Gold", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "HelicopterPad": {
        "name": "Helipad",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_HelicopterPad_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_HelicopterPad_0000.png",
        "resources": [{"name": "Gold", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Mountain_Crystal": {
        "name": "Mana Mountain",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Mountain_Crystal_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Mountain_Crystal_0000.png",
        "resources": [{"name": "Mana", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "BigHole": {
        "name": "Mysterious Hole",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_BigHole_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_BigHole_0000.png",
        "resources": [{"name": "Dark Matter", "chance": Decimal(0.55), "fertilizing_bonus": Decimal(0.1), "fert_cost": 5000}],
    },
    "Old_Windmill": {
        "name": "Old Windmill",
        "chance": 0.00592153960029608,
        "rarity": "Elite",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Windmill_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Windmill_A_0000.png",
        "resources": [{"name": "Mech", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Water": {
        "name": "Water",
        "chance": 0.00888230940044412,
        "rarity": "Rare",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Water_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Water_A_0000.png",
        "resources": [{"name": "Liquidium", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "SmallFarm_Wheat_Fence": {
        "name": "Fenced Feed Patch",
        "chance": 0.0118430792005922,
        "rarity": "Rare",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_SmallFarm_Wheat_Fence_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_SmallFarm_Wheat_Fence_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Mountain": {
        "name": "Mountain",
        "chance": 0.0118430792005922,
        "rarity": "Rare",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Mountain_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Mountain_0000.png",
        "resources": [{"name": "Mech", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Pond_Circle": {
        "name": "Quaint Pond",
        "chance": 0.0118430792005922,
        "rarity": "Rare",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Pond_Circle_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Pond_Circle_0000.png",
        "resources": [{"name": "Liquidium", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Pond_Corner": {
        "name": "Rock Pool",
        "chance": 0.0118430792005922,
        "rarity": "Rare",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Pond_Corner_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Pond_Corner_0000.png",
        "resources": [{"name": "Liquidium", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Corn": {
        "name": "Bitcorn",
        "chance": 0.0236861584011843,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Corn_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Corn_A_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "SmallFarm_Corn": {
        "name": "Bitcorn Patch",
        "chance": 0.0236861584011843,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Corn_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Corn_A_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "SmallFarm_Corn_Fence": {
        "name": "Fenced Bitcorn Patch",
        "chance": 0.0236861584011843,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Corn_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Corn_A_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "SmallFarm_Cabbage": {
        "name": "Cabbage Patch",
        "chance": 0.0296076980014804,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_SmallFarm_Cabbage_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_SmallFarm_Cabbage_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "SmallFarm_Cabbage_Fence": {
        "name": "Fenced Cabbage Patch",
        "chance": 0.0296076980014804,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_SmallFarm_Cabbage_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_SmallFarm_Cabbage_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "SmallFarm_Empty": {
        "name": "Empty Patch",
        "chance": 0.0296076980014804,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_SmallFarm_Empty_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_SmallFarm_Empty_0000.png",
        "resources": [{"name": "Mech", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "Grass_Mushrooms": {
        "name": "Fairy Ring",
        "chance": 0.0296076980014804,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Grass_Mushrooms_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Grass_Mushrooms_0000.png",
        "resources": [{"name": "Mana", "chance": Decimal(0.60), "fertilizing_bonus": Decimal(0.1), "fert_cost": 3000}],
    },
    "SmallFarm_Wheat": {
        "name": "Feed Patch",
        "chance": 0.0296076980014804,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_SmallFarm_Wheat_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_SmallFarm_Wheat_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Wheat": {
        "name": "Wheat",
        "chance": 0.0296076980014804,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_SmallFarm_Wheat_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_SmallFarm_Wheat_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Woods": {
        "name": "Woodlands",
        "chance": 0.0355292376017764,
        "rarity": "Nice",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Woods_B_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Woods_B_0000.png",
        "resources": [{"name": "Lumber", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Roqs": {
        "name": "Roqs",
        "chance": 0.043079200592154,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Rocks_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Rocks_A_0000.png",
        "resources": [{"name": "Stone", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "CoqRoqs": {
        "name": "Coq Roqs",
        "chance": 0.0444115470022206,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Rocks_B_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Rocks_B_0000.png",
        "resources": [{"name": "Stone", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Tasty Feed": {
        "name": "Tasty Feed",
        "chance": 0.0473723168023686,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Wheat_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Wheat_A_0000.png",
        "resources": [{"name": "Veg", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Orchard": {
        "name": "Orchard",
        "chance": 0.0592153960029608,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Orchard_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Orchard_A_0000.png",
        "resources": [{"name": "Lumber", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Hills": {
        "name": "Rolling Hills",
        "chance": 0.0781643227239082,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Hills_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Hills_A_0000.png",
        "resources": [],
    },
    "Meadow": {
        "name": "Flower Meadow",
        "chance": 0.0781643227239082,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Meadow_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Meadow_A_0000.png",
        "resources": [],
    },
    "Grass_Trees": {
        "name": "Scattered Trees",
        "chance": 0.0781643227239082,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Grass_Trees_A_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Grass_Trees_A_0000.png",
        "resources": [{"name": "Lumber", "chance": Decimal(0.65), "fertilizing_bonus": Decimal(0.1), "fert_cost": 1500}],
    },
    "Grass_Full": {
        "name": "Healthy Lawn",
        "chance": 0.0888230940044412,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Grass_Full_01_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Grass_Full_01_0000.png",
        "resources": [],
    },
    "Grass_Thin": {
        "name": "Grass",
        "chance": 0.133234641006662,
        "rarity": "Common",
        "thumb": "/api/farmland/tiles/thumb/Farmland_05_Grass_Thin_01_0000.png",
        "image": "/api/farmland/tiles/image/Farmland_05_Grass_Thin_01_0000.png",
        "resources": [],
    },
}

FARMLAND_CSV_HEADER_ROW = [
    "ID",
    "Name",
    "Rarity",
    "Rarest Tile",
    "For Sale",
    "Sale Price",
    "Dark Matter",
    "Avaxium",
    "Gold",
    "Mana",
    "Tungsten",
    "Mech",
    "Liquidium",
    "Veg",
    "Lumber",
    "Stone",
    "pyramid_Annuit",
    "pyramid_Avax",
    "BoneDaddy",
    "Goldmine",
    "ChiknMountain",
    "Excalibur",
    "Meteor",
    "Tungsten",
    "Last Price",
    "# Resources",
    "# Unique Resources",
    "# Unique Foragable Tiles",
    "Bigness",
    "Size",
    "Fertility",
    "Multiplier",
    "Score",
    "Avg/Tile",
    "Ruin",
    "Red_Windmill",
    "Golf",
    "Graveyard",
    "HelicopterPad",
    "Mountain_Crystal",
    "BigHole",
    "Old_Windmill",
    "Water",
    "SmallFarm_Wheat_Fence",
    "Mountain",
    "Pond_Circle",
    "Pond_Corner",
    "Corn",
    "SmallFarm_Corn",
    "SmallFarm_Corn_Fence",
    "SmallFarm_Cabbage",
    "SmallFarm_Cabbage_Fence",
    "SmallFarm_Empty",
    "Grass_Mushrooms",
    "SmallFarm_Wheat",
    "Wheat",
    "Woods",
    "Roqs",
    "CoqRoqs",
    "Tasty Feed",
    "Orchard",
    "Hills",
    "Meadow",
    "Grass_Trees",
    "Grass_Full",
    "Grass_Thin",
]