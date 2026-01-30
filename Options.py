# Options.py
from dataclasses import dataclass
import typing
from Options import Option, OptionGroup, Toggle, PerGameCommonOptions, Range, NamedRange

class MapShadowsEnabled(Toggle):
    """Enables Map: \"Shadows of Evil\""""
    display_name =  "\"Shadows of Evil\" map enabled"
    default = True

class MapTheGiantEnabled(Toggle):
    """Enables Map: \"The Giant\"."""
    display_name = "\"The Giant\" map enabled"
    default = False

class MapCastleEnabled(Toggle):
    """Enables Map: \"Castle\"."""
    display_name = "\"Castle\" map enabled"
    default = True

class SpecialRoundsEnabled(Toggle):
    """Enables Special Rounds (Dogs, Monkeys, ect.)."""
    display_name = "Special Rounds Enabled"
    default = True

class RandomizeShieldParts(Toggle):
    """Shuffles your shield parts into the item pool"""
    display_name = "Randomize Shield Parts"
    default = True

class CastleBowCount(Range):
    """Number of Elemental Bow quests to include in checks or Weapon Quest goal conditions"""
    display_name = "(Castle) Weapon Quest - Bow Count"
    default = 4
    range_start = 0
    range_end = 4

class CastleWolfBow(Toggle):
    """Include Wolf Bow / Wolf Howl in Castle location list"""
    display_name = "(Castle) Wolf Bow / Wolf Howl Locations"
    default = True

class CastleFireBow(Toggle):
    """Include Fire Bow / Rune Prison in Castle location list"""
    display_name = "(Castle) Fire Bow / Rune Prison Locations"
    default = True

class CastleVoidBow(Toggle):
    """Include Void Bow / Demon Gate in Castle location list"""
    display_name = "(Castle) Void Bow / Demon Gate Locations"
    default = True

class PerkLimitDefaultModifier(Range):
    """Modifier for initial perk limit, e.g If a map has a perk limit of 4, then -1 modifier will make it 3"""
    display_name = "Perk Limit Default Modifier"
    default = -2
    range_start = -4
    range_end = 4

class ProgressivePerkLimitIncrease(Range):
    """How many increases to the perk limit to add to the item pool"""
    display_name = "Progressive Perk Limit Increase"
    default = 4
    range_start = 0
    range_end = 6

class MapSpecificWallbuysEnabled(Toggle):
    """Enables map specific wallbuy items"""
    display_name = "Map specific wallbuys"
    default = False

class MapSpecificMachinesEnabled(Toggle):
    """Enables map specific perk machine items"""
    display_name = "Map specific perk machines"
    default = False

class GiftWeight(Range):
    """Weighting of gifts to replace filler with"""
    display_name = "Gift Weight"
    default = 20
    range_start = 0
    range_end = 100

class RoundMaxLocation(Range):
    """Maximum of rounds per map to be included as an AP location / check. This will not exceed Goal Round if your goal condiiton is Victory Round"""
    display_name = "Max Round Location"
    range_start = 0
    range_end = 50
    default = 15

class RoundLocationFrequency(Range):
    """Frequency of rounds to award an AP location / check for.
    e.g. Setting this to 3 and Max Round Location to 15 means you'll get a check on rounds 3, 6, 9, 12 and 15"""
    display_name = "Round Location Frequency"
    range_start = 1
    range_end = 10
    default = 2

class EasterEggsEnabled(Toggle):
    """Include Easter Egg steps as AP locations / checks"""
    display_name = "Easter Egg Locations"
    default = True

class MusicEasterEggsEnabled(Toggle):
    """Include music easter eggs as AP locations / checks"""
    display_name = "Music Easter Egg Locations (Streamer Warning)"
    default = True

class GoalCondition(NamedRange):
    """Condition to finish the see.
    Easter Egg Hunt: Complete the Main Easter Egg on enabled maps
    Weapon Quest: Complete all weapon quests on enabled maps
    Victory Round: Reach a selected round on enabled maps"""
    display_name = "Victory Condition"
    range_start = 0
    range_end = 4
    default = 0

    option_easter_egg_hunt = 0
    option_weapon_quest = 1
    option_goal_round = 2

    special_range_names = {
        "easter_egg_hunt": 0,
        "weapon_quest": 1,
        "goal_round": 2,
    }

    default = 0

class GoalEasterEggCount(Range):
    """Number of Main Easter Eggs needed to complete the seed when running Easter Egg Hunt. This will not exceed the number of selected maps"""
    display_name = "Easter Egg Goal Count"
    range_start = 1
    range_end = 4

    default = 1

class GoalEasterEggHuntRandom(Toggle):
    """Randomize which Easter Eggs are required. If disabled, you may complete any number of enabled maps to meet your Easter Egg Goal Count"""
    display_name = "Easter Egg Randomize Requirement"
    default = False

class GoalRound(Range):
    """Round to award Goal Round to award victory on when running the Victory Round goal condition"""
    display_name = "Goal Round"
    range_start = 1
    range_end = 99
    default = 25

@dataclass
class BO3ZombiesOptions(PerGameCommonOptions):
    map_shadows_enabled: MapShadowsEnabled
    map_the_giant_enabled: MapTheGiantEnabled
    map_castle_enabled: MapCastleEnabled
    special_rounds_enabled: SpecialRoundsEnabled
    round_location_max: RoundMaxLocation
    round_location_freq: RoundLocationFrequency
    goal_condition: GoalCondition
    goal_round: GoalRound
    goal_ee_count: GoalEasterEggCount
    goal_ee_random: GoalEasterEggHuntRandom
    perk_limit_default_modifier: PerkLimitDefaultModifier
    progressive_perk_limit_increase: ProgressivePerkLimitIncrease
    randomized_shield_parts: RandomizeShieldParts
    map_specific_wallbuys: MapSpecificWallbuysEnabled
    map_specific_machines: MapSpecificMachinesEnabled
    castle_bow_count: CastleBowCount
    gift_weight: GiftWeight

bo3_option_groups = [
    OptionGroup("General Options", [
        RandomizeShieldParts,
        MapSpecificWallbuysEnabled,
        MapSpecificMachinesEnabled,
        RoundMaxLocation,
        RoundLocationFrequency,
        EasterEggsEnabled,
        MusicEasterEggsEnabled,
    ]),
    OptionGroup("Goal Conditions", [
        GoalCondition,
        GoalEasterEggHuntRandom,
        GoalEasterEggCount,
        GoalRound,
    ]),
    OptionGroup("Progressive Settings", [
        PerkLimitDefaultModifier,
        ProgressivePerkLimitIncrease,
    ]),
    OptionGroup("Map Settings", [
        MapShadowsEnabled,
        MapTheGiantEnabled,
        MapCastleEnabled,
        CastleBowCount,
    ]),
    OptionGroup("Filler", [
        GiftWeight,
    ]),
    OptionGroup("WIP", [
        SpecialRoundsEnabled,
    ])
]
