# Options.py
from dataclasses import dataclass
import typing
from Options import Option, OptionGroup, Toggle, PerGameCommonOptions, Range, NamedRange


class MapTheGiantEnabled(Toggle):
    """Enables Map: \"The Giant\"."""
    display_name = "\"The Giant\" map enabled"
    default = True

class MapCastleEnabled(Toggle):
    """Enables Map: \"Castle\"."""
    display_name = "\"Castle\" map enabled"
    default = True

class SpecialRoundsEnabled(Toggle):
    """Enables Special Rounds (Dogs, Monkeys, ect.)."""
    display_name = "Special Rounds Enabled"
    default = True

class BlockerDoorsEnabled(Toggle):
    """Enables doors as blockers"""
    display_name = "Enable Door Blockers"
    default = True

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
    map_the_giant_enabled: MapTheGiantEnabled
    map_castle_enabled: MapCastleEnabled
    special_rounds_enabled: SpecialRoundsEnabled
    victory_round: VictoryRound
    victory_round_choice: VictoryRoundChoice
    blocker_doors_enabled: BlockerDoorsEnabled
    map_specific_wallbuys: MapSpecificWallbuysEnabled
    map_specific_machines: MapSpecificMachinesEnabled
    gift_weight: GiftWeight

bo3_option_groups = [
    OptionGroup("General Options", [
        VictoryRound,
        VictoryRoundChoice,
        MapSpecificWallbuysEnabled,
        MapSpecificMachinesEnabled,
    ]),
    OptionGroup("Map Settings", [
        MapTheGiantEnabled,
        MapCastleEnabled,
    ]),
    OptionGroup("Filler", [
        GiftWeight,
    ]),
    OptionGroup("WIP", [
        SpecialRoundsEnabled,
        BlockerDoorsEnabled,
    ])
]
