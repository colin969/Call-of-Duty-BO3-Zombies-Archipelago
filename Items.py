import typing
from BaseClasses import Item
from . import Weapons
from .Names import ItemName, Maps

from typing import Dict, Set

def gen_map_specific_list(mapString, items):
    map_specific_set = [ItemData(mapString + " " + item[0], item[1]) for item in items]
    return map_specific_set

class BO3ZombiesItemCategory():
    BLOCKER = "Blockers"
    WALLBUY = "Wallbuys"
    POWER = "Power"
    EASTER_EGG = "Easter Egg"
    MACHINE = "Machines"
    MISC = "Misc"
    VICTORY = "Victory"
    GIFT = "Gifts"
    TRAP = "Traps"
    PROGRESSIVE = "Progressive"
    SPECIAL_WEAPON = "Special Weapons"
    CRAFTABLE = "Craftables"
    REGULAR_WEAPON = "Regular Weapons"
    MAP_UNLOCK = "Map Unlocks"
    SHOP_ITEMS = "Shop Items"

class ItemData(typing.NamedTuple):
    name: str
    category: str

class BO3ZombiesItem(Item):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {item_data.name: id for id, item_data in enumerate(all_items, base_id)}

ShieldParts = [ItemData(row, BO3ZombiesItemCategory.PROGRESSIVE) for row in[
    ItemName.ShieldPart_Door,
    ItemName.ShieldPart_Dolly,
    ItemName.ShieldPart_Clamp,
]]

# The Giant Items

The_Giant_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_MuleKick,
    ItemName.Machine_PhdFlopper,
]]

The_Giant_Machines_Specific = gen_map_specific_list(Maps.The_Giant_Map_String, The_Giant_Machines)

# Castle Items

Castle_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
    ItemName.Machine_DeadShot,
    ItemName.Machine_ElectricCherry,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_PhdFlopper,
]]

Castle_Machines_Specific = gen_map_specific_list(Maps.Castle_Map_String, Castle_Machines)

Castle_Shield = gen_map_specific_list(Maps.Castle_Map_String, ShieldParts)

Castle_Craftables = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
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

Shadows_Shield = gen_map_specific_list(Maps.Shadows_Map_String, ShieldParts)

Shadows_Craftables = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Shadows_Craftable_ApothiconServant_Heart,
    ItemName.Shadows_Craftable_ApothiconServant_Skeleton,
    ItemName.Shadows_Craftable_ApothiconServant_Xenomatter,
    ItemName.Shadows_Craftable_CivilProtector_Fuse01,
    ItemName.Shadows_Craftable_CivilProtector_Fuse02,
    ItemName.Shadows_Craftable_CivilProtector_Fuse03,
]]

# Zetsubou No Shima

Zetsubou_Shield = gen_map_specific_list(Maps.Zetsubou_Map_String, ShieldParts)

Zetsubou_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_MuleKick,
    ItemName.Machine_StaminUp,
    ItemName.Machine_DeadShot,
    ItemName.Machine_ElectricCherry,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_PhdFlopper,
]]

Zetsubou_Machines_Specific = gen_map_specific_list(Maps.Zetsubou_Map_String, Zetsubou_Machines)

Zetsubou_Craftables_Gasmask = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Zetsubou_Craftable_Gasmask_Visor,
    ItemName.Zetsubou_Craftable_Gasmask_Filter,
    ItemName.Zetsubou_Craftable_Gasmask_Strap,
]]

# Gorod Krovi

GorodKrovi_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_MuleKick,
    ItemName.Machine_StaminUp,
    ItemName.Machine_DeadShot,
    ItemName.Machine_ElectricCherry,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_PhdFlopper,
]]

GorodKrovi_Machines_Specific = gen_map_specific_list(Maps.GorodKrovi_Map_String, GorodKrovi_Machines)

GorodKrovi_Shield = gen_map_specific_list(Maps.GorodKrovi_Map_String, ShieldParts)

GorodKrovi_Craftables_Dragonride = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.GorodKrovi_Craftable_Dragonride_Transmitter,
    ItemName.GorodKrovi_Craftable_Dragonride_Codes,
    ItemName.GorodKrovi_Craftable_Dragonride_Map,
]]

# Revelations

Revelations_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_DeadShot,
    ItemName.Machine_ElectricCherry,
    ItemName.Machine_PhdFlopper,
]]

Revelations_Machines_Specific = gen_map_specific_list(Maps.Revelations_Map_String, Revelations_Machines)

Revelations_Shield = gen_map_specific_list(Maps.Revelations_Map_String, ShieldParts)

# === Zombie Chronicles ===

# Kino der Toten

Kino_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_DeadShot,
    ItemName.Machine_PhdFlopper,
]]

Kino_Machines_Specific = gen_map_specific_list(Maps.Kino_Map_String, Kino_Machines)

# Moon

Moon_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_DeadShot,
    ItemName.Machine_PhdFlopper,
]]

Moon_Machines_Specific = gen_map_specific_list(Maps.Moon_Map_String, Moon_Machines)


# === Modded Maps ===

# Wanted

Wanted_Shield = gen_map_specific_list(Maps.Wanted_Map_String, ShieldParts)

Wanted_Craftable_Acidgat = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Wanted_Craftable_Acidgat_Engine,
    ItemName.Wanted_Craftable_Acidgat_Acid,
]]

Wanted_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_StaminUp,
    ItemName.Machine_MuleKick,
    ItemName.Machine_WidowsWine,
    ItemName.Machine_DeadShot,
    ItemName.Machine_ElectricCherry,
    ItemName.Machine_PhdFlopper,
]]

Wanted_Machines_Specific = gen_map_specific_list(Maps.Wanted_Map_String, Wanted_Machines)

# Progressives

Progressive_PerkLimitIncrease = ItemData(ItemName.Progressive_PerkLimitIncrease, BO3ZombiesItemCategory.PROGRESSIVE)
Progressive_PackAPunch = ItemData(ItemName.Progressive_PackAPunch, BO3ZombiesItemCategory.PROGRESSIVE)
Progressive_StartingPoints500 = ItemData(ItemName.Progressive_StartingPoints500, BO3ZombiesItemCategory.PROGRESSIVE)

Progressive_Items = [
    Progressive_PerkLimitIncrease,
    Progressive_PackAPunch,
    Progressive_StartingPoints500,
]

# Point Drop Items

Points_1500 = ItemData(ItemName.Points1500, BO3ZombiesItemCategory.MISC)

# Victory

Weapon_Victory_Items = [ItemData(row, BO3ZombiesItemCategory.VICTORY) for row in [
    ItemName.Shadows_Victory_ApothiconSwordLvl2,
    ItemName.Shadows_Victory_Upgraded_LilArnies,
    ItemName.Shadows_Victory_Upgraded_DoughnutMines,
    ItemName.Castle_Victory_ElementalBow_Storm,
    ItemName.Castle_Victory_ElementalBow_Wolf,
    ItemName.Castle_Victory_ElementalBow_Fire,
    ItemName.Castle_Victory_ElementalBow_Void,
    ItemName.GorodKrovi_Victory_DragonGauntlets,
    ItemName.GorodKrovi_Victory_TiamatsMaw,
    ItemName.GorodKrovi_Victory_Upgraded_Dragonstrikes,
    ItemName.GorodKrovi_Victory_Upgraded_MonkeyBombs,
    ItemName.Revelations_Victory_Upgrade_ApothiconServant,
    ItemName.Revelations_Victory_Upgraded_LilArnies,
    ItemName.Zetsubou_Victory_Masamune,
    ItemName.Zetsubou_Victory_Skull,
    # == Modded Maps ===
    ItemName.Wanted_Victory_Magmagat,
    ItemName.Wanted_Victory_GreatScott,
]]

Victory_Items = [ItemData(row, BO3ZombiesItemCategory.VICTORY) for row in [
    Maps.Shadows_Map_String + ItemName.Victory,
    Maps.Shadows_Map_String + ItemName.EE_Victory,
    Maps.The_Giant_Map_String + ItemName.Victory,
    # Only used in emergency
    Maps.The_Giant_Map_String + ItemName.EE_Victory,
    Maps.Castle_Map_String + ItemName.Victory,
    Maps.Castle_Map_String + ItemName.EE_Victory,
    Maps.Zetsubou_Map_String + ItemName.Victory,
    Maps.Zetsubou_Map_String + ItemName.EE_Victory,
    Maps.GorodKrovi_Map_String + ItemName.Victory,
    Maps.GorodKrovi_Map_String + ItemName.EE_Victory,
    Maps.Revelations_Map_String + ItemName.Victory,
    Maps.Revelations_Map_String + ItemName.EE_Victory,
    Maps.Kino_Map_String + ItemName.Victory,
    Maps.Moon_Map_String + ItemName.Victory,
    Maps.Moon_Map_String + ItemName.EE_Victory,
    # == Modded Maps ==
    Maps.Wanted_Map_String + ItemName.Victory,
    Maps.Wanted_Map_String + ItemName.EE_Victory,
]]

# Misc/Filler Items

Misc_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points200, BO3ZombiesItemCategory.MISC)
]]

# Gifts

Gift_Items = [ItemData(row, BO3ZombiesItemCategory.GIFT) for row in [
    ItemName.Gift_UnlimitedSprint,
    ItemName.Gift_Carpenter_Powerup,
    ItemName.Gift_Double_Points_Powerup,
    ItemName.Gift_InstaKill_Powerup,
    ItemName.Gift_Fire_Sale_Powerup,
    ItemName.Gift_Max_Ammo_Powerup,
    ItemName.Gift_Free_Perk_Powerup,
]]

# Traps

Trap_Items = [ItemData(row, BO3ZombiesItemCategory.TRAP) for row in [
    ItemName.Trap_ThirdPersonMode,
    ItemName.Trap_Nuke_Powerup,
    ItemName.Trap_GrenadeParty,
    ItemName.Trap_KnuckleCrack,
]]

# Map Unlocks
Map_Unlocks = [ItemData(row, BO3ZombiesItemCategory.MAP_UNLOCK) for row in [
    ItemName.Map_Shadows,
    ItemName.Map_Castle,
    ItemName.Map_Zetsubou,
    ItemName.Map_GorodKrovi,
    ItemName.Map_Revelations,
    ItemName.Map_The_Giant,
    ItemName.Map_Kino,
    ItemName.Map_Moon,
    ItemName.Map_Wanted,
]]

# Shop items
Shop_Items = [ItemData(row, BO3ZombiesItemCategory.SHOP_ITEMS) for row in [
    ItemName.Shop_PerkToken,
    ItemName.Shop_MegaGumToken,
    ItemName.Shop_RareGumToken,
    ItemName.Shop_LegendaryGumToken,
    ItemName.Shop_CheckpointToken,
]]

def gen_weapon_box_items():
    items = []
    seen_items = set()
    for map in Maps.all_maps:
        if map in Weapons.map_weapon_data_sets:
            map_set = Weapons.map_weapon_data_sets[map]
            for weapon_key, weapon_data in map_set.vanilla.items():
                if weapon_data.item_name not in seen_items:
                    items.append(ItemData(weapon_data.item_name, BO3ZombiesItemCategory.REGULAR_WEAPON))
                    seen_items.add(weapon_data.item_name)
            for weapon_key, weapon_data in map_set.expanded.items():
                if weapon_data.item_name not in seen_items:
                    items.append(ItemData(weapon_data.item_name, BO3ZombiesItemCategory.REGULAR_WEAPON))
                    seen_items.add(weapon_data.item_name)
            for weapon_key, weapon_data in map_set.wallbuys.items():
                if weapon_data.item_name not in seen_items:
                    items.append(ItemData(weapon_data.item_name, BO3ZombiesItemCategory.REGULAR_WEAPON))
                    seen_items.add(weapon_data.item_name)
            for weapon_key, weapon_data in map_set.special.items():
                items.append(ItemData(weapon_data.item_name, BO3ZombiesItemCategory.SPECIAL_WEAPON))
    return items

WeaponBox_Items = gen_weapon_box_items() 

all_items = (
    Shop_Items + Progressive_Items + [Points_1500] + Weapon_Victory_Items + Victory_Items + Gift_Items + Trap_Items + Misc_Items + Map_Unlocks
    + WeaponBox_Items
    # The Giant
    + The_Giant_Machines + The_Giant_Machines_Specific
    # Castle
    + Castle_Machines + Castle_Machines_Specific
    + Castle_Craftables + Castle_Shield
    # Shadows of Evil
    + Shadows_Machines + Shadows_Machines_Specific
    + Shadows_Craftables + Shadows_Shield
    # Zetsubou No Shima
    + Zetsubou_Machines + Zetsubou_Machines_Specific
    + Zetsubou_Craftables_Gasmask + Zetsubou_Shield
    # Gorod Krovi
    + GorodKrovi_Machines + GorodKrovi_Machines_Specific
    + GorodKrovi_Craftables_Dragonride + GorodKrovi_Shield
    # Revelations
    + Revelations_Machines + Revelations_Machines_Specific
    + Revelations_Shield
    # == Zombie Chronicles ==
    # Kino
    + Kino_Machines + Kino_Machines_Specific
    # Moon
    + Moon_Machines + Moon_Machines_Specific
    # == Modded Maps ==
    # Wanted
    + Wanted_Machines + Wanted_Machines_Specific
    + Wanted_Shield + Wanted_Craftable_Acidgat
)

all_items_dict = {item_data.name: item_data for item_data in all_items}

item_groups: Dict[str, Set[str]] = {}
# Maps
for item in all_items_dict.keys():
    category = all_items_dict[item].category
    if category not in item_groups.keys():
        item_groups[category] = set()
    item_groups[category].add(all_items_dict[item].name)
