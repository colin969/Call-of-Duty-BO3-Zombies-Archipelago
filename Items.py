import typing
from BaseClasses import Item
from . import Weapons
from .Names import ItemName, Maps

from typing import Dict, Set

item_groups: Dict[str, Set[str]] = {}

def gen_map_specific_list(mapString, items, category):
    map_specific_set = [ItemData(mapString + " " + item[0], item[1]) for item in items]
    category_name = mapString + " " + category
    if category_name not in item_groups.keys():
        item_groups[category_name] = set()
    for item in map_specific_set:
        item_groups[category_name].add(item.name)
    return map_specific_set

class BO3ZombiesItemCategory():
    BLOCKER = "Blocker"
    WALLBUY = "Wallbuy"
    POWER = "Power"
    EASTER_EGG = "Easter Egg"
    MACHINE = "Perk"
    MISC = "Misc"
    VICTORY = "Victory"
    GIFT = "Gift"
    TRAP = "Trap"
    PROGRESSIVE = "Progressive"
    SPECIAL_WEAPON = "Special Weapon"
    CRAFTABLE = "Craftable"
    REGULAR_WEAPON = "Regular Weapon"
    MAP_UNLOCK = "Map Unlock"
    SHOP_ITEMS = "Shop Item"

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
]]

The_Giant_Machines_Specific = gen_map_specific_list(Maps.The_Giant_Map_String, The_Giant_Machines, "Perk")

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

Castle_Machines_Specific = gen_map_specific_list(Maps.Castle_Map_String, Castle_Machines, "Perk")

Castle_Shield = gen_map_specific_list(Maps.Castle_Map_String, ShieldParts, "Shield")

Castle_Craftable_GravitySpikes = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Castle_Craftable_GravitySpikes_Body,
    ItemName.Castle_Craftable_GravitySpikes_Guards,
    ItemName.Castle_Craftable_GravitySpikes_Handle
]]
_castle_gravity_spikes_group = {x.name for x in Castle_Craftable_GravitySpikes}
item_groups[Maps.Castle_Map_String + " Ragnarok DG-4"] = _castle_gravity_spikes_group
item_groups[Maps.Castle_Map_String + " Gravity Spikes"] = _castle_gravity_spikes_group

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

Shadows_Machines_Specific = gen_map_specific_list(Maps.Shadows_Map_String, Shadows_Machines, "Perk")

Shadows_Shield = gen_map_specific_list(Maps.Shadows_Map_String, ShieldParts, "Shield")

Shadows_Craftable_ApothiconServant = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Shadows_Craftable_ApothiconServant_Heart,
    ItemName.Shadows_Craftable_ApothiconServant_Skeleton,
    ItemName.Shadows_Craftable_ApothiconServant_Xenomatter,
]]
item_groups[Maps.Shadows_Map_String + " Apothicon Servant"] = {x.name for x in Shadows_Craftable_ApothiconServant}

Shadows_Craftable_CivilProtector = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Shadows_Craftable_CivilProtector_Fuse01,
    ItemName.Shadows_Craftable_CivilProtector_Fuse02,
    ItemName.Shadows_Craftable_CivilProtector_Fuse03,
]]
_soe_civil_protector_group = {x.name for x in Shadows_Craftable_CivilProtector}
item_groups[Maps.Shadows_Map_String + " Civil Protector"] = _soe_civil_protector_group
item_groups[Maps.Shadows_Map_String + " Fuse"] = _soe_civil_protector_group

# Zetsubou No Shima

Zetsubou_Shield = gen_map_specific_list(Maps.Zetsubou_Map_String, ShieldParts, "Shield")

Zetsubou_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
    ItemName.Machine_Juggernog,
    ItemName.Machine_QuickRevive,
    ItemName.Machine_SpeedCola,
    ItemName.Machine_DoubleTap,
    ItemName.Machine_MuleKick,
    ItemName.Machine_StaminUp,
]]

Zetsubou_Machines_Specific = gen_map_specific_list(Maps.Zetsubou_Map_String, Zetsubou_Machines, "Perk")

Zetsubou_Craftables_Gasmask = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Zetsubou_Craftable_Gasmask_Visor,
    ItemName.Zetsubou_Craftable_Gasmask_Filter,
    ItemName.Zetsubou_Craftable_Gasmask_Strap,
]]
item_groups[Maps.Zetsubou_Map_String + " Gasmask"] = {x.name for x in Zetsubou_Craftables_Gasmask}

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

GorodKrovi_Machines_Specific = gen_map_specific_list(Maps.GorodKrovi_Map_String, GorodKrovi_Machines, "Perk")

GorodKrovi_Shield = gen_map_specific_list(Maps.GorodKrovi_Map_String, ShieldParts, "Shield")

GorodKrovi_Craftables_Dragonride = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.GorodKrovi_Craftable_Dragonride_Transmitter,
    ItemName.GorodKrovi_Craftable_Dragonride_Codes,
    ItemName.GorodKrovi_Craftable_Dragonride_Map,
]]
item_groups[Maps.GorodKrovi_Map_String + " Dragonride"] = {x.name for x in GorodKrovi_Craftables_Dragonride}

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

Revelations_Machines_Specific = gen_map_specific_list(Maps.Revelations_Map_String, Revelations_Machines, "Perk")

Revelations_Shield = gen_map_specific_list(Maps.Revelations_Map_String, ShieldParts, "Shield")

# === Zombie Chronicles ===

# Nacht der Untoten

Nacht_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
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

Nacht_Machines_Specific = gen_map_specific_list(Maps.Nacht_Map_String, Nacht_Machines, "Perk")

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

Kino_Machines_Specific = gen_map_specific_list(Maps.Kino_Map_String, Kino_Machines, "Perk")

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

Moon_Machines_Specific = gen_map_specific_list(Maps.Moon_Map_String, Moon_Machines, "Perk")

# Origins

Origins_Machines = [ItemData(row, BO3ZombiesItemCategory.MACHINE) for row in [
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

Origins_Machines_Specific = gen_map_specific_list(Maps.Origins_Map_String, Origins_Machines, "Perk")

Origins_Shield = gen_map_specific_list(Maps.Origins_Map_String, ShieldParts, "Shield")

Origins_MaxisDrone = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in [
    ItemName.Origins_Craftable_MaxisDrone_Body,
    ItemName.Origins_Craftable_MaxisDrone_Brain,
    ItemName.Origins_Craftable_MaxisDrone_Engine
]]
item_groups[Maps.Origins_Map_String + " Maxis Drone"] = {x.name for x in Origins_MaxisDrone}

Origins_Discs = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in [
    ItemName.Origins_Craftable_Gramophone_FireDisc,
    ItemName.Origins_Craftable_Gramophone_IceDisc,
    ItemName.Origins_Craftable_Gramophone_WindDisc,
    ItemName.Origins_Craftable_Gramophone_LightningDisc
]]
_origins_discs_group = {x.name for x in Origins_Discs}
item_groups[Maps.Origins_Map_String + " Disc"] = _origins_discs_group
item_groups[Maps.Origins_Map_String + " Gramophone Part"] = _origins_discs_group
item_groups[Maps.Origins_Map_String + " Gramophone Disc"] = _origins_discs_group

# === Modded Maps ===

# Wanted

Wanted_Shield = gen_map_specific_list(Maps.Wanted_Map_String, ShieldParts, "Shield")

Wanted_Craftable_Acidgat = [ItemData(row, BO3ZombiesItemCategory.CRAFTABLE) for row in[
    ItemName.Wanted_Craftable_Acidgat_Engine,
    ItemName.Wanted_Craftable_Acidgat_Acid,
]]
item_groups[Maps.Wanted_Map_String + " Acidgat"] = {x.name for x in Wanted_Craftable_Acidgat}

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

Wanted_Machines_Specific = gen_map_specific_list(Maps.Wanted_Map_String, Wanted_Machines, "Perk")

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
    Maps.Nacht_Map_String + ItemName.Victory,
    Maps.Kino_Map_String + ItemName.Victory,
    Maps.Moon_Map_String + ItemName.Victory,
    Maps.Moon_Map_String + ItemName.EE_Victory,
    Maps.Origins_Map_String + ItemName.Victory,
    Maps.Origins_Map_String + ItemName.EE_Victory,
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
    ItemName.Map_Nacht,
    ItemName.Map_Kino,
    ItemName.Map_Moon,
    ItemName.Map_Origins,
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

WEAPON_TYPE_NAMES: dict[str, str] = {
    "ar":        "Assault Rifle",
    "smg":       "Submachine Gun",
    "lmg":       "Light Machine Gun",
    "sniper":    "Sniper Rifle",
    "shotgun":   "Shotgun",
    "pistol":    "Pistol",
    "launcher":  "Launcher",
    "melee":     "Melee",
    "wonder":    "Wonder Weapon",
    "equipment": "Equipment",
    "other":     "Other",
}

# Feels silly to build and delete, but it's probably fine
WeaponBox_Items = []
_seen_weapon_items = set()

for _weapon_type_name in WEAPON_TYPE_NAMES.values():
    item_groups[_weapon_type_name] = set()

for _map in Maps.all_maps:
    if _map in Weapons.map_weapon_data_sets:
        _map_set = Weapons.map_weapon_data_sets[_map]
        for _weapon_key, _weapon_data in [
            *_map_set.vanilla.items(),
            *_map_set.expanded.items(),
            *_map_set.wallbuys.items(),
        ]:
            if _weapon_data.item_name not in _seen_weapon_items:
                WeaponBox_Items.append(ItemData(_weapon_data.item_name, BO3ZombiesItemCategory.REGULAR_WEAPON))
                _seen_weapon_items.add(_weapon_data.item_name)
            if _weapon_data.category not in WEAPON_TYPE_NAMES:
                raise KeyError(f"Unknown weapon category '{_weapon_data.category}' for weapon '{_weapon_data.item_name}'. Add it to WEAPON_TYPE_NAMES.")
            item_groups[WEAPON_TYPE_NAMES[_weapon_data.category]].add(_weapon_data.item_name)

        for _weapon_key, _weapon_data in _map_set.special.items():
            WeaponBox_Items.append(ItemData(_weapon_data.item_name, BO3ZombiesItemCategory.SPECIAL_WEAPON))
            if _weapon_data.category not in WEAPON_TYPE_NAMES:
                raise KeyError(f"Unknown weapon category '{_weapon_data.category}' for weapon '{_weapon_data.item_name}'. Add it to WEAPON_TYPE_NAMES.")
            item_groups[WEAPON_TYPE_NAMES[_weapon_data.category]].add(_weapon_data.item_name)

del _seen_weapon_items, _map, _map_set, _weapon_key, _weapon_data, _weapon_type_name

all_items = (
    Shop_Items + Progressive_Items + [Points_1500] + Weapon_Victory_Items + Victory_Items + Gift_Items + Trap_Items + Misc_Items + Map_Unlocks
    + WeaponBox_Items
    # The Giant
    + The_Giant_Machines + The_Giant_Machines_Specific
    # Castle
    + Castle_Machines + Castle_Machines_Specific
    + Castle_Craftable_GravitySpikes + Castle_Shield
    # Shadows of Evil
    + Shadows_Machines + Shadows_Machines_Specific
    + Shadows_Craftable_ApothiconServant + Shadows_Craftable_CivilProtector + Shadows_Shield
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
    # Nacht der Untoten
    + Nacht_Machines + Nacht_Machines_Specific
    # Kino der Toten
    + Kino_Machines + Kino_Machines_Specific
    # Moon
    + Moon_Machines + Moon_Machines_Specific
    # Origins
    + Origins_Machines + Origins_Machines_Specific
    + Origins_Discs + Origins_MaxisDrone + Origins_Shield
    # == Modded Maps ==
    # Wanted
    + Wanted_Machines + Wanted_Machines_Specific
    + Wanted_Shield + Wanted_Craftable_Acidgat
)

all_items_dict = {item_data.name: item_data for item_data in all_items}

# Maps
for item in all_items_dict.keys():
    category = all_items_dict[item].category
    if category not in item_groups.keys():
        item_groups[category] = set()
    item_groups[category].add(all_items_dict[item].name)
