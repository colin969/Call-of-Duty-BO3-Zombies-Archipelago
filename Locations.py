import typing
from enum import IntEnum
from .Names import LocationName, Maps

BaseMapIds = {
    Maps.The_Giant_Map_String: 1000,
    Maps.Castle_Map_String: 2000,
    Maps.Shadows_Map_String: 3000,
    Maps.GorodKrovi_Map_String: 4000,
    Maps.Zetsubou_Map_String: 5000,
}

class BO3ZombiesLocationCategory(IntEnum):
    ROUND = 0
    MISC = 10
    CRAFTABLE_PART = 20
    QUEST = 30

class LocationData(typing.NamedTuple):
    name: str
    category: BO3ZombiesLocationCategory
    code: int

def gen_map_round_locations(map_string, count):
    if map_string not in BaseMapIds:
        raise Exception("round location gen - Map string not in base map ids?")
    base_map_id = BaseMapIds[map_string]
    locations = []
    for i in range(1, count + 1):
        location_name = f"{map_string} Round {i:02d}"
        locations.append(LocationData(location_name, BO3ZombiesLocationCategory.ROUND, base_map_id + i))
    return locations

def get_map_victory_location(map_string, goal_round):
    converted = int(goal_round)
    if map_string not in BaseMapIds:
        raise Exception("victory gen - Map string not in base map ids?")
    base_map_id = BaseMapIds[map_string]
    location_name = f"{map_string} Round {converted:02d}"
    return location_name


# Location IDs
# The Giant - 1000 to 1100 rounds, 1100+ to map specific checks
# Castle - 2000 to 2100 rounds, 2100+ to map specific checks
# Shadows of Evil - 3000 to 3100 rounds, 3100+ to map specific checks
# Universal - 9000 to 9999

# The Giant zm_giant

TheGiant_Round_Locations = gen_map_round_locations(Maps.The_Giant_Map_String, 100)

# Castle zm_castle

Castle_Round_Locations = gen_map_round_locations(Maps.Castle_Map_String, 100)

Castle_Craftable_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.CRAFTABLE_PART, row[1]) for row in [
    (LocationName.Castle_Craftable_ShieldPartDolly, 2200),
    (LocationName.Castle_Craftable_ShieldPartDoor, 2201),
    (LocationName.Castle_Craftable_ShieldPartClamp, 2202),
    (LocationName.Castle_Craftable_RagnarokDG4PartBody, 2210),
    (LocationName.Castle_Craftable_RagnarokDG4PartGuards, 2211),
    (LocationName.Castle_Craftable_RagnarokDG4PartHandle, 2212),
]]

Castle_Quest_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_AllSpareChange, 2300),
    (LocationName.Castle_Quest_FeedDragonheads, 2301),
    (LocationName.Castle_Quest_TurnOnLandingPads, 2302),
]]

Castle_Quest_Music_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_Music_DeadAgain, 2400),
    (LocationName.Castle_Quest_Music_Requiem, 2401),
]]

Castle_Quest_ElementalBow_Storm_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_ElementalBow_Storm_TakeArrow, 2500),
    (LocationName.Castle_Quest_ElementalBow_Storm_LightBeacons, 2501),
    (LocationName.Castle_Quest_ElementalBow_Storm_Wallrun, 2502),
    (LocationName.Castle_Quest_ElementalBow_Storm_Batteries, 2503),
    (LocationName.Castle_Quest_ElementalBow_Storm_ChargeBeacons, 2504),
    (LocationName.Castle_Quest_ElementalBow_Storm_RepairArrow, 2505),
    (LocationName.Castle_Quest_ElementalBow_Storm_ForgeBow, 2506),
]]

Castle_Quest_ElementalBow_Wolf_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_ElementalBow_Wolf_Paintings, 2510),
    (LocationName.Castle_Quest_ElementalBow_Wolf_TakeArrow, 2511),
    (LocationName.Castle_Quest_ElementalBow_Wolf_CollectSkull, 2512),
    (LocationName.Castle_Quest_ElementalBow_Wolf_Escort, 2513),
    (LocationName.Castle_Quest_ElementalBow_Wolf_RepairArrow, 2514),
    (LocationName.Castle_Quest_ElementalBow_Wolf_ForgeBow, 2515),
]]

Castle_Quest_ElementalBow_Fire_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_ElementalBow_Fire_TakeArrow, 2520),
    (LocationName.Castle_Quest_ElementalBow_Fire_ShootOrb, 2521),
    (LocationName.Castle_Quest_ElementalBow_Fire_ChargeCircles, 2522),
    (LocationName.Castle_Quest_ElementalBow_Fire_MagmaBall, 2523),
    (LocationName.Castle_Quest_ElementalBow_Fire_RepairArrow, 2524),
    (LocationName.Castle_Quest_ElementalBow_Fire_ForgeBow, 2525),
]]

Castle_Quest_ElementalBow_Void_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_ElementalBow_Void_TakeArrow, 2530),
    (LocationName.Castle_Quest_ElementalBow_Void_RitualSacrifice, 2531),
    (LocationName.Castle_Quest_ElementalBow_Void_CollectSkulls, 2532),
    (LocationName.Castle_Quest_ElementalBow_Void_SacrificeCrawlers, 2533),
    (LocationName.Castle_Quest_ElementalBow_Void_RunePuzzle, 2534),
    (LocationName.Castle_Quest_ElementalBow_Void_RepairArrow, 2535),
    (LocationName.Castle_Quest_ElementalBow_Void_ForgeBow, 2536),
]]

Castle_Quest_MainEE_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Castle_Quest_MainEE_ActivateTeleporter, 2600),
    (LocationName.Castle_Quest_MainEE_UnlockSafe, 2601),
    (LocationName.Castle_Quest_MainEE_RecoverRocket, 2602),
    (LocationName.Castle_Quest_MainEE_OpenMPD, 2603),
    (LocationName.Castle_Quest_MainEE_BossFight, 2604),
    (LocationName.Castle_Quest_MainEE_BlowUpMoon, 2605),
    (LocationName.Castle_Quest_MainEE_Victory, 2606),
]]

# Shadows of Evil zm_zod
Shadows_Round_Locations = gen_map_round_locations(Maps.Shadows_Map_String, 100)

Shadows_Quest_MainQuest_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Shadows_Quest_MainQuest_MagicianRitual, 3100),
    (LocationName.Shadows_Quest_MainQuest_BoxerRitual, 3101),
    (LocationName.Shadows_Quest_MainQuest_DetectivesRitual, 3102),
    (LocationName.Shadows_Quest_MainQuest_FemmeFataleRitual, 3103),
    (LocationName.Shadows_Quest_MainQuest_OpenPortal, 3104),
]]

Shadows_Quest_ApothiconSword_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Shadows_Quest_ApothiconSword_EnterCode, 3110),
    (LocationName.Shadows_Quest_ApothiconSword_CollectSword, 3111),
    (LocationName.Shadows_Quest_ApothiconSword_CollectUpgradedSword, 3112),
]]

Shadows_Quest_MainEE_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Shadows_Quest_MainEE_FindNerosBook, 3200),
    (LocationName.Shadows_Quest_MainEE_DefeatShadowman, 3201),
    (LocationName.Shadows_Quest_MainEE_DefeatGiantSpaceSquid, 3202),
    (LocationName.Shadows_Quest_MainEE_Victory, 3203),
]]

Shadows_Quest_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Shadows_Quest_AllSpareChangeCollected, 3500),
    (LocationName.Shadows_Quest_LaundryTicket, 3501),
]]

Shadows_Craftable_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.MISC, row[1]) for row in [
    (LocationName.Shadows_Craftable_ApothiconServant_MargwaHeart, 3300),
    (LocationName.Shadows_Craftable_ApothiconServant_MargwaTentacle, 3301),
    (LocationName.Shadows_Craftable_ApothiconServant_Xenomatter, 3302),
    (LocationName.Shadows_Craftable_CivilProtector_Fuse1, 3310),
    (LocationName.Shadows_Craftable_CivilProtector_Fuse2, 3311),
    (LocationName.Shadows_Craftable_CivilProtector_Fuse3, 3312),
    (LocationName.Shadows_Craftable_ShieldPartDolly, 3320),
    (LocationName.Shadows_Craftable_ShieldPartDoor, 3321),
    (LocationName.Shadows_Craftable_ShieldPartClamp, 3322),
]]

# Zetsubou No Shima

Zetsubou_Round_Locations = gen_map_round_locations(Maps.Zetsubou_Map_String, 100)

Zetsubou_Quest_MainQuest_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Zetsubou_Quest_MainQuest_Bucket, 5100),
    (LocationName.Zetsubou_Quest_MainQuest_Bunker, 5101),
    (LocationName.Zetsubou_Quest_MainQuest_Power, 5102),
    (LocationName.Zetsubou_Quest_MainQuest_Pap, 5103),
]]

Zetsubou_Quest_MainEE_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Zetsubou_Quest_MainEE_AirplaneAmmo, 5110),
    (LocationName.Zetsubou_Quest_MainEE_AirplaneDown, 5111),
    (LocationName.Zetsubou_Quest_MainEE_Gear2, 5112),
    (LocationName.Zetsubou_Quest_MainEE_Gear3, 5113),
    (LocationName.Zetsubou_Quest_MainEE_FreeTakeo, 5114),
    (LocationName.Zetsubou_Quest_MainEE_Victory, 5115),
]]

Zetsubou_Quest_KT4_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Zetsubou_Quest_KT4_Vial, 5120),
    (LocationName.Zetsubou_Quest_KT4_Flower, 5121),
    (LocationName.Zetsubou_Quest_KT4_Spider, 5122),
    (LocationName.Zetsubou_Quest_Masamune_Vial, 5123),
    (LocationName.Zetsubou_Quest_Masamune_Flower, 5124),
    (LocationName.Zetsubou_Quest_Masamune_Spider, 5125),
]]

Zetsubou_Quest_Skull_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Zetsubou_Quest_Skull_Cleanse, 5130),
    (LocationName.Zetsubou_Quest_Skull_CleanseAll, 5131),
    (LocationName.Zetsubou_Quest_Skull_Survive, 5132),
]]

Zetsubou_Quest_Challenges_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Zetsubou_Quest_Challenge_1, 5140),
    (LocationName.Zetsubou_Quest_Challenge_2, 5141),
    (LocationName.Zetsubou_Quest_Challenge_3, 5142),
    (LocationName.Zetsubou_Quest_Challenge_All, 5143),
]]

Zetsubou_Craftable_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.Zetsubou_Craftable_Gasmask_Visor, 5200),
    (LocationName.Zetsubou_Craftable_Gasmask_Filter, 5201),
    (LocationName.Zetsubou_Craftable_Gasmask_Strap, 5202),
    (LocationName.Zetsubou_Craftable_ShieldPartDolly, 5203),
    (LocationName.Zetsubou_Craftable_ShieldPartDoor, 5204),
    (LocationName.Zetsubou_Craftable_ShieldPartClamp, 5205),
]]

# Gorod Krovi

GorodKrovi_Round_Locations = gen_map_round_locations(Maps.GorodKrovi_Map_String, 100)

GorodKrovi_Quest_MainQuest_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Transmitter, 4100),
    (LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Codes, 4101),
    (LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Map, 4102),
    (LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Repaired, 4103),
]]

GorodKrovi_Quest_MaineEE_Locations =  [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_MainEE_CollectTrophies, 4110),
    (LocationName.GorodKrovi_Quest_MainEE_ChargeGenerator, 4111),
    (LocationName.GorodKrovi_Quest_MainEE_PnuematicTubes, 4112),
    (LocationName.GorodKrovi_Quest_MainEE_EnterSophiasPassword, 4113),
    (LocationName.GorodKrovi_Quest_MainEE_CompleteScenarios, 4114),
    (LocationName.GorodKrovi_Quest_MainEE_DeliverPowerCore, 4115),
    (LocationName.GorodKrovi_Quest_MainEE_SlayDragon, 4116),
    (LocationName.GorodKrovi_Quest_MainEE_DefeatNikolai, 4117),
    (LocationName.GorodKrovi_Quest_MainEE_Victory, 4118),
]]

GorodKrovi_Quest_DragonStrikes = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_Dragonstrikes_Acquire, 4120),
    (LocationName.GorodKrovi_Quest_Dragonstrikes_Upgrade, 4121),
]]

GorodKrovi_Quest_DragonGauntlets = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_DragonGauntlets_AcquireEgg, 4130),
    (LocationName.GorodKrovi_Quest_DragonGauntlets_WarmEgg, 4131),
    (LocationName.GorodKrovi_Quest_DragonGauntlets_C1Napalm, 4132),
    (LocationName.GorodKrovi_Quest_DragonGauntlets_C2Collatoral, 4133),
    (LocationName.GorodKrovi_Quest_DragonGauntlets_C3Knife, 4134),
    (LocationName.GorodKrovi_Quest_DragonGauntlets_IncubateEgg, 4135),
    (LocationName.GorodKrovi_Quest_DragonGauntlets_HatchEgg, 4136),
]]

GorodKrovi_Quest_TiamatsMaw = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_TiamatsMaw_Kills, 4140),
    (LocationName.GorodKrovi_Quest_TiamatsMaw_Bathe, 4141),
    (LocationName.GorodKrovi_Quest_TiamatsMaw_Runes, 4142),
    (LocationName.GorodKrovi_Quest_TiamatsMaw_Upgrade, 4143),
]]

GorodKrovi_Quest_SideEE = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_SideEE_DragonWings, 4150),
    (LocationName.GorodKrovi_Quest_SideEE_ManglerHelm, 4151),
    (LocationName.GorodKrovi_Quest_SideEE_ValkyrieHelm, 4152),
]]

GorodKrovi_Quest_Challenges = [LocationData(row[0], BO3ZombiesLocationCategory.QUEST, row[1]) for row in [
    (LocationName.GorodKrovi_Quest_Challenges_1, 4160),
    (LocationName.GorodKrovi_Quest_Challenges_2, 4161),
    (LocationName.GorodKrovi_Quest_Challenges_3, 4162),
    (LocationName.GorodKrovi_Quest_UpgradeMonkeyBombs, 4163),
]]

GorodKrovi_Craftable_Locations = [LocationData(row[0], BO3ZombiesLocationCategory.MISC, row[1]) for row in [
    (LocationName.GorodKrovi_Craftable_ShieldPartDoor, 4200),
    (LocationName.GorodKrovi_Craftable_ShieldPartDolly, 4201),
    (LocationName.GorodKrovi_Craftable_ShieldPartClamp, 4202),
]]

early_locations =  [LocationData(row[0], row[1], row[2]) for row in [
    (LocationName.RepairWindows_5, BO3ZombiesLocationCategory.MISC, 9001),
]]

all_locations = (
    TheGiant_Round_Locations 
    + Castle_Round_Locations + Castle_Quest_Locations + Castle_Quest_Music_Locations + Castle_Craftable_Locations 
    + Castle_Quest_ElementalBow_Fire_Locations + Castle_Quest_ElementalBow_Void_Locations + Castle_Quest_ElementalBow_Storm_Locations + Castle_Quest_ElementalBow_Wolf_Locations
    + Castle_Quest_MainEE_Locations
    + Shadows_Round_Locations + Shadows_Quest_Locations + Shadows_Craftable_Locations
    + Shadows_Quest_MainQuest_Locations + Shadows_Quest_ApothiconSword_Locations 
    + Shadows_Quest_MainEE_Locations
    + Zetsubou_Round_Locations + Zetsubou_Craftable_Locations
    + Zetsubou_Quest_MainQuest_Locations + Zetsubou_Quest_MainEE_Locations + Zetsubou_Quest_Challenges_Locations
    + Zetsubou_Quest_KT4_Locations + Zetsubou_Quest_Skull_Locations
    + GorodKrovi_Round_Locations + GorodKrovi_Craftable_Locations + GorodKrovi_Quest_MaineEE_Locations + GorodKrovi_Quest_SideEE
    + GorodKrovi_Quest_DragonStrikes + GorodKrovi_Quest_DragonGauntlets + GorodKrovi_Quest_Challenges + GorodKrovi_Quest_TiamatsMaw
    + GorodKrovi_Quest_MainQuest_Locations
    + early_locations)
