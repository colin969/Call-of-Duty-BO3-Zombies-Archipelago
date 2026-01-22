# Options.py
from dataclasses import dataclass
import typing
from Options import Option, OptionGroup, Toggle, PerGameCommonOptions, Range


class TheGiantEnabled(Toggle):
    """Enables Map: \"The Giant\"."""
    display_name = "\"The Giant\" map enabled"
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

class VictoryRound(Range):
    """Round to award Map Victory."""
    display_name = "Victory Round"
    range_start = 1
    range_end = 99
    default = 20


@dataclass
class BO3ZombiesOptions(PerGameCommonOptions):
    the_giant_enabled: TheGiantEnabled
    special_rounds_enabled: SpecialRoundsEnabled
    victory_round: VictoryRound
    blocker_doors_enabled: BlockerDoorsEnabled
    map_specific_wallbuys: MapSpecificWallbuysEnabled

bo3_option_groups = [
    OptionGroup("General Options", [
        TheGiantEnabled,
        SpecialRoundsEnabled,
        VictoryRound,
        BlockerDoorsEnabled,
        MapSpecificWallbuysEnabled
    ])
]
