import typing
from enum import IntEnum
from BaseClasses import Location
from .Names import LocationName, Maps

BaseMapIds = {
    Maps.The_Giant_Map_String: 1000,
    Maps.Castle_Map_String: 2000,
    Maps.Shadows_Map_String: 3000
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

class BO3ZombiesLocation(Location):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {loc_data.name: loc_data.code + base_id for loc_data in all_locations}

def gen_map_round_locations(map_string, count):
    if map_string not in BaseMapIds:
        raise Exception("round location gen - Map string not in base map ids?")
    base_map_id = BaseMapIds[map_string]
    locations = []
    for i in range(1, count + 1):
        location_name = f"{map_string} Round {i:02d}"
        locations.append(LocationData(location_name, BO3ZombiesLocationCategory.ROUND, base_map_id + i))
    return locations

def get_map_victory_location(map_string, victory_round):
    converted = int(victory_round)
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

early_locations =  [LocationData(row[0], row[1], row[2]) for row in [
    (LocationName.RepairWindows_5, BO3ZombiesLocationCategory.MISC, 9001),
]]

all_locations = (
    TheGiant_Round_Locations 
    + Castle_Round_Locations + Castle_Quest_Locations + Castle_Quest_Music_Locations + Castle_Craftable_Locations 
    + Castle_Quest_ElementalBow_Fire_Locations + Castle_Quest_ElementalBow_Void_Locations + Castle_Quest_ElementalBow_Storm_Locations + Castle_Quest_ElementalBow_Wolf_Locations
    + Castle_Quest_MainEE_Locations
    + Shadows_Round_Locations + Shadows_Quest_Locations + Shadows_Craftable_Locations
    + Shadows_Quest_MainQuest_Locations + Shadows_Quest_ApothiconSword_Locations + Shadows_Quest_MainEE_Locations
    + early_locations)
