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

class VictoryRound(Range):
    """Round to award Map Victory."""
    display_name = "Victory Round"
    range_start = 1
    range_end = 99
    default = 20

class VictoryRoundChoice(NamedRange):
    """Round to award Map Victory.
    Random: Must reach victory round on a random enabled map
    All Maps: Must reach victory round on every enabled map
    """
    display_name = "Victory Round"
    default = 0

    range_start = 0
    range_end = 1

    option_random_map = 0b0000 # 0
    option_all_maps = 0b0001 # 1

    special_range_names = {
        "random": 0b0000,   # 0
        "all_maps": 0b0001, # 1
    }

@dataclass
class BO3ZombiesOptions(PerGameCommonOptions):
    map_shadows_enabled: MapShadowsEnabled
    map_the_giant_enabled: MapTheGiantEnabled
    map_castle_enabled: MapCastleEnabled
    special_rounds_enabled: SpecialRoundsEnabled
    victory_round: VictoryRound
    victory_round_choice: VictoryRoundChoice
    perk_limit_default_modifier: PerkLimitDefaultModifier
    progressive_perk_limit_increase: ProgressivePerkLimitIncrease
    randomized_shield_parts: RandomizeShieldParts
    map_specific_wallbuys: MapSpecificWallbuysEnabled
    map_specific_machines: MapSpecificMachinesEnabled
    gift_weight: GiftWeight

bo3_option_groups = [
    OptionGroup("General Options", [
        VictoryRound,
        VictoryRoundChoice,
        RandomizeShieldParts,
        MapSpecificWallbuysEnabled,
        MapSpecificMachinesEnabled,
    ]),
    OptionGroup("Progressive Settings", [
        PerkLimitDefaultModifier,
        ProgressivePerkLimitIncrease,
    ]),
    OptionGroup("Map Settings", [
        MapShadowsEnabled,
        MapTheGiantEnabled,
        MapCastleEnabled,
    ]),
    OptionGroup("Filler", [
        GiftWeight,
    ]),
    OptionGroup("WIP", [
        SpecialRoundsEnabled,
    ])
]
