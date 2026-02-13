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
    SPECIAL_WEAPON = 15
    CRAFTABLE = 16
    REGULAR_WEAPON = 17


class ItemData(typing.NamedTuple):
    name: str
    category: BO3ZombiesItemCategory

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
]]

The_Giant_Wallbuys = [ItemData(ItemName.Wallbuy + row, BO3ZombiesItemCategory.WALLBUY) for row in[
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

The_Giant_MysteryBox = [ItemData(Maps.The_Giant_Map_String + " " + ItemName.MysteryBox + row, BO3ZombiesItemCategory.SPECIAL_WEAPON) for row in[
    ItemName.Weapon_Raygun,
    ItemName.Weapon_Wunderwaffe,
    ItemName.Weapon_MonkeyBombs,
]]

The_Giant_MysteryBox_Regular = [ItemData(ItemName.MysteryBox + row, BO3ZombiesItemCategory.REGULAR_WEAPON) for row in[
    ItemName.Weapon_Drakon,
    ItemName.Weapon_Locus,
    ItemName.Weapon_ManoWar,
    ItemName.Weapon_HVK,
    ItemName.Weapon_ICR,
    ItemName.Weapon_Haymaker,
    ItemName.Weapon_Brecci,
    ItemName.Weapon_Dingo,
    ItemName.Weapon_Dredge,
    ItemName.Weapon_RPK,
    ItemName.Weapon_VMP,
]]

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
]]

Castle_Wallbuys = [ItemData(ItemName.Wallbuy + row, BO3ZombiesItemCategory.WALLBUY) for row in [
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

Castle_Shield = gen_map_specific_list(Maps.Castle_Map_String, ShieldParts)

Castle_Craftables = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Castle_Craftable_GravitySpikes_Body,
    ItemName.Castle_Craftable_GravitySpikes_Guards,
    ItemName.Castle_Craftable_GravitySpikes_Handle
]]

Castle_MysteryBox = [ItemData(Maps.Castle_Map_String + " " + ItemName.MysteryBox + row, BO3ZombiesItemCategory.SPECIAL_WEAPON) for row in[
    ItemName.Weapon_Raygun,
    ItemName.Weapon_MonkeyBombs,
]]

Castle_MysteryBox_Regular = [ItemData(ItemName.MysteryBox + row, BO3ZombiesItemCategory.REGULAR_WEAPON) for row in[
    ItemName.Weapon_Drakon,
    ItemName.Weapon_Locus,
    ItemName.Weapon_ManoWar,
    ItemName.Weapon_HVK,
    ItemName.Weapon_ICR,
    ItemName.Weapon_Haymaker,
    ItemName.Weapon_Brecci,
    ItemName.Weapon_Dingo,
    ItemName.Weapon_Dredge,
    ItemName.Weapon_RPK,
    ItemName.Weapon_VMP,
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

Shadows_Wallbuys = [ItemData(ItemName.Wallbuy + row, BO3ZombiesItemCategory.WALLBUY) for row in[
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

Shadows_Shield = gen_map_specific_list(Maps.Shadows_Map_String, ShieldParts)

Shadows_Craftables = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Shadows_Craftable_ApothiconServant_Heart,
    ItemName.Shadows_Craftable_ApothiconServant_Skeleton,
    ItemName.Shadows_Craftable_ApothiconServant_Xenomatter,
    ItemName.Shadows_Craftable_CivilProtector_Fuse01,
    ItemName.Shadows_Craftable_CivilProtector_Fuse02,
    ItemName.Shadows_Craftable_CivilProtector_Fuse03,
]]

Shadows_MysteryBox = [ItemData(Maps.Shadows_Map_String + " " + ItemName.MysteryBox + row, BO3ZombiesItemCategory.SPECIAL_WEAPON) for row in[
    ItemName.Weapon_Raygun,
    ItemName.Weapon_LilArnies,
    ItemName.Weapon_ApothiconServant,
]]

Shadows_MysteryBox_Regular = [ItemData(ItemName.MysteryBox + row, BO3ZombiesItemCategory.REGULAR_WEAPON) for row in[
    ItemName.Weapon_Drakon,
    ItemName.Weapon_Locus,
    ItemName.Weapon_ManoWar,
    ItemName.Weapon_HVK,
    ItemName.Weapon_ICR,
    ItemName.Weapon_Haymaker,
    ItemName.Weapon_Brecci,
    ItemName.Weapon_Dingo,
    ItemName.Weapon_Dredge,
]]

# Zetsubou No Shima

Zetsubou_Shield = gen_map_specific_list(Maps.Zetsubou_Map_String, ShieldParts)

Zetsubou_Machines = []

Zetsubou_Wallbuys = []

Zetsubou_Machines_Specific = gen_map_specific_list(Maps.Zetsubou_Map_String, Zetsubou_Machines)
Zetsubou_Wallbuys_Specific = gen_map_specific_list(Maps.Zetsubou_Map_String, Zetsubou_Wallbuys)

Zetsubou_Craftables_Gasmask = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Zetsubou_Craftable_Gasmask_Visor,
    ItemName.Zetsubou_Craftable_Gasmask_Filter,
    ItemName.Zetsubou_Craftable_Gasmask_Strap,
]]

Zetsubou_MysteryBox = [ItemData(Maps.Zetsubou_Map_String + " " + ItemName.MysteryBox + row, BO3ZombiesItemCategory.SPECIAL_WEAPON) for row in[
    ItemName.Weapon_Raygun,
    ItemName.Weapon_MonkeyBombs,
    ItemName.Weapon_KT4,
]]

Zetsubou_MysteryBox_Regular = [ItemData(ItemName.MysteryBox + row, BO3ZombiesItemCategory.REGULAR_WEAPON) for row in[
    ItemName.Weapon_Drakon,
    ItemName.Weapon_Locus,
    ItemName.Weapon_ManoWar,
    ItemName.Weapon_HVK,
    ItemName.Weapon_ICR,
    ItemName.Weapon_Haymaker,
    ItemName.Weapon_Brecci,
    ItemName.Weapon_Dingo,
    ItemName.Weapon_Dredge,
    ItemName.Weapon_VMP,
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
]]

GorodKrovi_Wallbuys = [ItemData(ItemName.Wallbuy + row, BO3ZombiesItemCategory.WALLBUY) for row in[
    ItemName.Weapon_RK5,
    ItemName.Weapon_Sheiva,
    ItemName.Weapon_Pharo,
    ItemName.Weapon_LCAR,
    ItemName.Weapon_KRM,
    ItemName.Weapon_Kuda,
    ItemName.Weapon_VMP,
    ItemName.Weapon_Vesper,
    ItemName.Weapon_Argus,
    ItemName.Weapon_KN44,
    ItemName.Weapon_ICR,
    ItemName.Weapon_M8A7,
    ItemName.Weapon_HVK,
    ItemName.Weapon_BowieKnife,
]]

GorodKrovi_Machines_Specific = gen_map_specific_list(Maps.GorodKrovi_Map_String, GorodKrovi_Machines)
GorodKrovi_Wallbuys_Specific = gen_map_specific_list(Maps.GorodKrovi_Map_String, GorodKrovi_Wallbuys)

GorodKrovi_Shield = gen_map_specific_list(Maps.GorodKrovi_Map_String, ShieldParts)

GorodKrovi_Craftables_Dragonride = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.GorodKrovi_Craftable_Dragonride_Transmitter,
    ItemName.GorodKrovi_Craftable_Dragonride_Codes,
    ItemName.GorodKrovi_Craftable_Dragonride_Map,
]]

GorodKrovi_MysteryBox = [ItemData(Maps.GorodKrovi_Map_String + " " + ItemName.MysteryBox + row, BO3ZombiesItemCategory.SPECIAL_WEAPON) for row in[
    ItemName.Weapon_Raygun,
    ItemName.Weapon_MonkeyBombs,
    ItemName.Weapon_RaygunMk3,
]]

GorodKrovi_MysteryBox_Regular = [ItemData(ItemName.MysteryBox + row, BO3ZombiesItemCategory.REGULAR_WEAPON) for row in[
    ItemName.Weapon_FFAR,
    ItemName.Weapon_Drakon,
    ItemName.Weapon_Locus,
    ItemName.Weapon_ManoWar,
    ItemName.Weapon_HVK,
    ItemName.Weapon_ICR,
    ItemName.Weapon_Haymaker,
    ItemName.Weapon_Brecci,
    ItemName.Weapon_Dingo,
    ItemName.Weapon_Dredge,
    ItemName.Weapon_RPK,
    ItemName.Weapon_VMP,
    ItemName.Weapon_Vesper
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
]]

Revelations_Wallbuys = [ItemData(ItemName.Wallbuy + row, BO3ZombiesItemCategory.WALLBUY) for row in[
    ItemName.Weapon_RK5,
    ItemName.Weapon_Sheiva,
    ItemName.Weapon_Pharo,
    ItemName.Weapon_LCAR,
    ItemName.Weapon_KRM,
    ItemName.Weapon_Kuda,
    ItemName.Weapon_VMP,
    ItemName.Weapon_Vesper,
    ItemName.Weapon_Argus,
    ItemName.Weapon_KN44,
    ItemName.Weapon_ICR,
    ItemName.Weapon_M8A7,
    ItemName.Weapon_HVK,
    ItemName.Weapon_BowieKnife,
]]

Revelations_Machines_Specific = gen_map_specific_list(Maps.Revelations_Map_String, Revelations_Machines)
Revelations_Wallbuys_Specific = gen_map_specific_list(Maps.Revelations_Map_String, Revelations_Wallbuys)

Revelations_Shield = gen_map_specific_list(Maps.Revelations_Map_String, ShieldParts)

Revelations_MysteryBox = [ItemData(Maps.Revelations_Map_String + " " + ItemName.MysteryBox + row, BO3ZombiesItemCategory.SPECIAL_WEAPON) for row in[
    ItemName.Weapon_Raygun,
    ItemName.Weapon_LilArnies,
    ItemName.Weapon_ApothiconServant,
    ItemName.Weapon_Thundergun,
    ItemName.Weapon_Ragnaroks,
]]

Revelations_MysteryBox_Regular = [ItemData(ItemName.MysteryBox + row, BO3ZombiesItemCategory.REGULAR_WEAPON) for row in[
    ItemName.Weapon_Drakon,
    ItemName.Weapon_Locus,
    ItemName.Weapon_ManoWar,
    ItemName.Weapon_HVK,
    ItemName.Weapon_ICR,
    ItemName.Weapon_Haymaker,
    ItemName.Weapon_Brecci,
    ItemName.Weapon_Dingo,
    ItemName.Weapon_Dredge,
    ItemName.Weapon_VMP,
]]

# Progressives

Progressive_PerkLimitIncrease = ItemData(ItemName.Progressive_PerkLimitIncrease, BO3ZombiesItemCategory.PROGRESSIVE)
Progressive_Items = [
    Progressive_PerkLimitIncrease
]

# Point Drop Items

Points_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points500, BO3ZombiesItemCategory.MISC)
]]

# Victory

Weapon_Victory_Items = [ItemData(row, BO3ZombiesItemCategory.VICTORY) for row in [
    ItemName.Shadows_Victory_ApothiconSwordLvl2,
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
]]

Victory_Items = [ItemData(row, BO3ZombiesItemCategory.VICTORY) for row in [
    Maps.Shadows_Map_String + ItemName.Victory,
    Maps.Shadows_Map_String + ItemName.EE_Victory,
    Maps.The_Giant_Map_String + ItemName.Victory,
    Maps.Castle_Map_String + ItemName.Victory,
    Maps.Castle_Map_String + ItemName.EE_Victory,
    Maps.Zetsubou_Map_String + ItemName.Victory,
    Maps.Zetsubou_Map_String + ItemName.EE_Victory,
    Maps.GorodKrovi_Map_String + ItemName.Victory,
    Maps.GorodKrovi_Map_String + ItemName.EE_Victory,
    Maps.Revelations_Map_String + ItemName.Victory,
    Maps.Revelations_Map_String + ItemName.EE_Victory,
]]

# Misc/Filler Items

Misc_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points50, BO3ZombiesItemCategory.MISC)
]]

PapItem = ItemData(ItemName.PapMachine, BO3ZombiesItemCategory.MACHINE)

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

base_items = Points_Items

all_items = (
    Progressive_Items + Points_Items + Weapon_Victory_Items + Victory_Items + Gift_Items + Trap_Items + Misc_Items
    + [PapItem]
    # The Giant
    + The_Giant_Machines + The_Giant_Machines_Specific
    + The_Giant_Wallbuys + The_Giant_Wallbuys_Specific
    + The_Giant_MysteryBox + The_Giant_MysteryBox_Regular
    # Castle
    + Castle_Machines + Castle_Machines_Specific
    + Castle_Wallbuys + Castle_Wallbuys_Specific
    + Castle_Craftables + Castle_Shield
    + Castle_MysteryBox + Castle_MysteryBox_Regular
    # Shadows of Evil
    + Shadows_Machines + Shadows_Machines_Specific
    + Shadows_Wallbuys + Shadows_Wallbuys_Specific
    + Shadows_Craftables + Shadows_Shield
    + Shadows_MysteryBox + Shadows_MysteryBox_Regular
    # Zetsubou No Shima
    + Zetsubou_Machines + Zetsubou_Machines_Specific
    + Zetsubou_Wallbuys + Zetsubou_Wallbuys_Specific
    + Zetsubou_Craftables_Gasmask + Zetsubou_Shield
    + Zetsubou_MysteryBox + Zetsubou_MysteryBox_Regular
    # Gorod Krovi
    + GorodKrovi_Machines + GorodKrovi_Machines_Specific
    + GorodKrovi_Wallbuys + GorodKrovi_Wallbuys_Specific
    + GorodKrovi_Craftables_Dragonride + GorodKrovi_Shield
    + GorodKrovi_MysteryBox + GorodKrovi_MysteryBox_Regular
    # Revelations
    + Revelations_Machines + Revelations_Machines_Specific
    + Revelations_Wallbuys + Revelations_Wallbuys_Specific
    + Revelations_Shield
    + Revelations_MysteryBox + Revelations_MysteryBox_Regular
)

all_items_dict = {item_data.name: item_data for item_data in all_items}
