import typing
from enum import IntEnum
from BaseClasses import Item
from .Names import ItemName, Maps

def gen_map_specific_list(mapString, items):
    map_specific_set = [ItemData(mapString + " " + item[0], item[1]) for item in items]
    return map_specific_set

class BO3ZombiesItemCategory(IntEnum):
    BLOCKER = 5
    WALLBUY = 6
    POWER = 7
    EASTER_EGG = 8
    MACHINE = 9
    MISC = 10
    VICTORY = 11
    GIFT = 12
    TRAP = 13
    PROGRESSIVE = 14


class ItemData(typing.NamedTuple):
    name: str
    category: BO3ZombiesItemCategory

class BO3ZombiesItem(Item):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {item_data.name: id for id, item_data in enumerate(all_items, base_id)}

# The Giant Items

The_Giant_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_MuleKick,
]]

The_Giant_Wallbuys = [ItemData(row, BO3ZombiesItemCategory.WALLBUY) for row in[
    # Teleporter A
    ItemName.Weapon_M8A7,
    # Teleporter B
    ItemName.Weapon_HVK,
    # Teleporter C
    ItemName.Weapon_KN44,
    ItemName.Weapon_BowieKnife,
    # Starting Area
    ItemName.Weapon_Sheiva,
    ItemName.Weapon_RK5,
    # Garage
    ItemName.Weapon_VMP,
    ItemName.Weapon_KRM,
    # Animal Testing
    ItemName.Weapon_Kuda,
    ItemName.Weapon_LCAR,
]]

The_Giant_Wallbuys_Specific = gen_map_specific_list(Maps.The_Giant_Map_String, The_Giant_Wallbuys)
The_Giant_Machines_Specific = gen_map_specific_list(Maps.The_Giant_Map_String, The_Giant_Machines)

# Castle Items

Castle_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
]]

Castle_Wallbuys = [ItemData(row, BO3ZombiesItemCategory.WALLBUY) for row in [
    # Gondola
    ItemName.Weapon_RK5,
    ItemName.Weapon_Sheiva,
    # Gate House (Upper)
    ItemName.Weapon_LCAR,
    # Lower Courtyard and Trophy Room
    ItemName.Weapon_KRM,
    # Mission Control
    ItemName.Weapon_M8A7,
    # Inside Castle?
    ItemName.Weapon_HVK,
    # Upper Courtyard?
    ItemName.Weapon_Kuda,
    # Rocket Platform
    ItemName.Weapon_VMP,
    # Supply Room
    ItemName.Weapon_Vesper,
    # Living Quarters and Juggernog Room
    ItemName.Weapon_KN44,
    # Undercroft
    ItemName.Weapon_BRM,
    # Armory
    ItemName.Weapon_BowieKnife
]]

Castle_Wallbuys_Specific = gen_map_specific_list(Maps.Castle_Map_String, Castle_Wallbuys)
Castle_Machines_Specific = gen_map_specific_list(Maps.Castle_Map_String, Castle_Machines)

Castle_Craftables = [ItemData(row, BO3ZombiesItemCategory.MISC) for row in[
    ItemName.Castle_Craftable_GravitySpikes_Body,
    ItemName.Castle_Craftable_GravitySpikes_Guards,
    ItemName.Castle_Craftable_GravitySpikes_Handle
]]

# Shadows of Evil

Shadows_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
    ItemName.Machine_WidowsWine,
]]

Shadows_Machines_Specific = gen_map_specific_list(Maps.Shadows_Map_String, Shadows_Machines)

Shadows_Wallbuys = [ItemData(row, BO3ZombiesItemCategory.WALLBUY) for row in[
    ItemName.Weapon_RK5,
    ItemName.Weapon_Sheiva,
    ItemName.Weapon_LCAR,
    ItemName.Weapon_KRM,
    ItemName.Weapon_HVK,
    ItemName.Weapon_M8A7,
    ItemName.Weapon_Kuda,
    ItemName.Weapon_VMP,
    ItemName.Weapon_Vesper,
    ItemName.Weapon_KN44,
    ItemName.Weapon_Bootlegger,
    ItemName.Weapon_BowieKnife,
]]

Shadows_Wallbuys_Specific = gen_map_specific_list(Maps.Shadows_Map_String, Shadows_Wallbuys)

Shadows_Craftables = [ItemData(row, BO3ZombiesItemCategory.MISC) for row in[
    ItemName.Shadows_Craftable_ApothiconServant_Heart,
    ItemName.Shadows_Craftable_ApothiconServant_Skeleton,
    ItemName.Shadows_Craftable_ApothiconServant_Xenomatter,
    ItemName.Shadows_Craftable_CivilProtector_Fuse01,
    ItemName.Shadows_Craftable_CivilProtector_Fuse02,
    ItemName.Shadows_Craftable_CivilProtector_Fuse03,
]]

# Progressives

Progressive_PerkLimitIncrease = ItemData(ItemName.Progressive_PerkLimitIncrease, BO3ZombiesItemCategory.PROGRESSIVE)
Progressive_Items = [
    Progressive_PerkLimitIncrease
]

# Craftables

ShieldParts = [ItemData(row, BO3ZombiesItemCategory.PROGRESSIVE) for row in[
    ItemName.ShieldPart_Door,
    ItemName.ShieldPart_Dolly,
    ItemName.ShieldPart_Clamp,
]]

# Point Drop Items

Points_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points500, BO3ZombiesItemCategory.MISC)
]]

# Victory

Victory_Items = [ItemData(row[0], row[1]) for row in [
    (Maps.Shadows_Map_String + " Victory", BO3ZombiesItemCategory.VICTORY),
    (Maps.The_Giant_Map_String + " Victory", BO3ZombiesItemCategory.VICTORY),
    (Maps.Castle_Map_String + " Victory", BO3ZombiesItemCategory.VICTORY)
]]

# Misc/Filler Items

Misc_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points50, BO3ZombiesItemCategory.MISC)
]]

PapItem = ItemData(ItemName.PapMachine, BO3ZombiesItemCategory.MACHINE)

# Gifts

Gift_Items = [ItemData(row, BO3ZombiesItemCategory.GIFT) for row in [
    ItemName.Gift_Carpenter_Powerup,
    ItemName.Gift_Double_Points_Powerup,
    ItemName.Gift_InstaKill_Powerup,
    ItemName.Gift_Fire_Sale_Powerup,
    ItemName.Gift_Max_Ammo_Powerup,
    ItemName.Gift_Nuke_Powerup,
    ItemName.Gift_Free_Perk_Powerup,
]]

# Traps

Trap_Items = [ItemData(row, BO3ZombiesItemCategory.TRAP) for row in [
    ItemName.Trap_ThirdPersonMode,
]]

base_items = Points_Items

all_items = (
    Progressive_Items + ShieldParts + Points_Items + Victory_Items + Gift_Items + Trap_Items + Misc_Items
    + [PapItem]
    # The Giant
    + The_Giant_Machines + The_Giant_Machines_Specific
    + The_Giant_Wallbuys + The_Giant_Wallbuys_Specific
    # Castle
    + Castle_Machines + Castle_Machines_Specific
    + Castle_Wallbuys + Castle_Wallbuys_Specific
    + Castle_Craftables
    # Shadows of Evil
    + Shadows_Machines + Shadows_Machines_Specific
    + Shadows_Wallbuys + Shadows_Wallbuys_Specific
    + Shadows_Craftables
)

all_items_dict = {item_data.name: item_data for item_data in all_items}
