# Options.py
from dataclasses import dataclass
import typing
from Options import OptionGroup, Toggle, PerGameCommonOptions, Range, Choice

class MapShadowsEnabled(Toggle):
    """Enables Map: \"Shadows of Evil\""""
    display_name =  "\"Shadows of Evil\" map enabled"
    default = True

class MapTheGiantEnabled(Toggle):
    """Enables Map: \"The Giant\"."""
    display_name = "\"The Giant\" map enabled"
    default = True

class MapCastleEnabled(Toggle):
    """Enables Map: \"Castle\"."""
    display_name = "\"Castle\" map enabled"
    default = True

class MapZetsubouEnabled(Toggle):
    """Enables Map: \"Zetsubou No Shima\"."""
    display_name = "\"Zetsubou No Shima\" map enabled"
    default = True

class MapGorodKroviEnabled(Toggle):
    """Enabled Map: \"Gorod Krovi\""""
    display_name = "\"Gorod Krovi\" map enabled"
    default = True
    
class MapRevelationsEnabled(Toggle):
    """Enabled Map: \"Revelations\""""
    display_name = "\"Revelations\" map enabled"
    default = True

class MapKinoEnabled(Toggle):
    """Enabled Map: \"Kino der Toten\""""
    display_name = "(Chronicles) \"Kino der Toten\" map enabled"
    default = False

class MapWorkshopWantedEnabled(Toggle):
    """Enabled Map: \"Wanted\""""
    display_name = "(BROKEN) \"Wanted\" map enabled"
    default = False

class StartMapHints(Toggle):
    """Start hints the maps you have in the pool."""
    display_name = "Start Hint Maps"
    default = True

class SpecialRoundsEnabled(Toggle):
    """Enables Special Rounds (Dogs, Monkeys, ect.)."""
    display_name = "Special Rounds Enabled"
    default = True

class RandomizeShieldParts(Toggle):
    """Shuffles your shield parts into the item pool"""
    display_name = "Randomize Shield Parts"
    default = True

class RandomizeGorodDragonrideParts(Toggle):
    """Shuffles the parts to unlock the pack-a-punch into the item pool"""
    display_name = "(UNUSED) Randomized Gorod Dragonride Parts"
    default = False

class RevelationsMaskCount(Range):
    """Number of random Revelations Mask quests to include in checks"""
    display_name = "(Revelations) Number of Masks with Checks"
    default = 3
    range_start = 0
    range_end = 7

class RevelationsMaskEnabledDireWolf(Toggle):
    """Enable Dire Wolf mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Dire Wolf"
    default = True

class RevelationsMaskEnabledSiegfried(Toggle):
    """Enable Helmet of Siegfried mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Helmet of Siegfried"
    default = True

class RevelationsMaskEnabledKing(Toggle):
    """Enable Helmet of the King mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Helmet of the King"
    default = True

class RevelationsMaskEnabledFury(Toggle):
    """Enable Fury's Head mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Fury Head"
    default = True

class RevelationsMaskEnabledMargwa(Toggle):
    """Enable Margwa's mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Margwa Head"
    default = True

class RevelationsMaskEnabledKeeperSkull(Toggle):
    """Enable Keeper Skull mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Keeper Skull"
    default = True

class RevelationsMaskEnabledApothicon(Toggle):
    """Enable Apothicon God Mask check for Revelations Mask checks"""
    display_name = "(Revelations) Mask - Apothicon God"
    default = True

class MysteryBoxSpecialItems(Toggle):
    """Shuffles special Mystery Box item unlocks (Wonder weapons, special equipment, specialist weapons) into the item pool"""
    display_name = "Mystery Box - Special Items"
    default = True

class MysteryBoxRegularItems(Toggle):
    """Shuffles regular Mystery Box item unlocks into the item pool"""
    display_name = "Mystery Box - Regular Items"
    default = True

class CastleBowCount(Range):
    """Number of random Elemental Bow quests to include in checks or Weapon Quest goal conditions"""
    display_name = "(Der Eisendrache) Number of Elemental Bow Quests with Checks"
    default = 2
    range_start = 0
    range_end = 4

class CastleBowEnabledStorm(Toggle):
    """Allow the Storm bow to be one of your random Elemental Bow quest checks"""
    display_name = "(Der Eisendrache) Elemental Bow - Storm"
    default = True

class CastleBowEnabledWolf(Toggle):
    """Allow the Wolf bow to be one of your random Elemental Bow quest checks"""
    display_name = "(Der Eisendrache) Elemental Bow - Wolf"
    default = True

class CastleBowEnabledFire(Toggle):
    """Allow the Fire bow to be one of your random Elemental Bow quest checks"""
    display_name = "(Der Eisendrache) Elemental Bow - Fire"
    default = False

class CastleBowEnabledVoid(Toggle):
    """Allow the Void bow to be one of your random Elemental Bow quest checks"""
    display_name = "(Der Eisendrache) Elemental Bow - Void"
    default = False

class StartingQuickRevive(Toggle):
    """Start with Quick Revive on all maps."""
    display_name = "Quick Revive on Start"
    default = False

class PerkLimitDefaultModifier(Range):
    """Modifier for initial perk limit, e.g If a map has a perk limit of 4, then -1 modifier will make it 3"""
    display_name = "Perk Limit Default Modifier"
    default = -2
    range_start = -3
    range_end = 4

class ProgressivePerkLimitIncrease(Range):
    """How many increases to the perk limit to add to the item pool"""
    display_name = "Progressive Perk Limit Increase"
    default = 4
    range_start = 0
    range_end = 6

class ProgressiveStartingPoints(Range):
    """How many extra starting points to add into the pool. This will be rounded to 500"""
    default = 3000
    range_start = 0
    range_end = 10000

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
    default = 40
    range_start = 0
    range_end = 100

class TrapWeight(Range):
    """Weighting of traps to replace filler with"""
    display_name = "Trap Weight"
    default = 0
    range_start = 0
    range_end = 100

class RoundMaxLocation(Range):
    """Maximum of rounds per map to be included as an AP location / check."""
    display_name = "Max Round Location"
    range_start = 0
    range_end = 50
    default = 16

class RoundLocationFrequency(Range):
    """Frequency of rounds to award an AP location / check for.
    e.g. Setting this to 3 and Max Round Location to 15 means you'll get a check on rounds 3, 6, 9, 12 and 15"""
    display_name = "Round Location Frequency"
    range_start = 1
    range_end = 10
    default = 2

class EasterEggsEnabled(Toggle):
    """Include Easter Egg steps as AP locations / checks when Easter Egg Hunt is not the goal condition"""
    display_name = "Easter Egg Checks"
    default = False

class MusicEasterEggsEnabled(Toggle):
    """Include music easter eggs as AP locations / checks"""
    display_name = "Music Easter Egg Checks (Streamer Warning)"
    default = True

class GoalCondition(Choice):
    """Condition to finish the see.
    Easter Egg Hunt: Complete the Main Easter Egg on enabled maps
    Weapon Quest: Complete all weapon quests on enabled maps
    Victory Round: Reach a selected round on enabled maps"""
    display_name = "Victory Condition"
    default = 0

    option_easter_egg_hunt = 0
    option_weapon_quest = 1
    option_goal_round = 2

class GoalEasterEggCount(Range):
    """Number of Main Easter Eggs needed to complete the seed when running Easter Egg Hunt. This will not exceed the number of selected maps"""
    display_name = "Easter Egg Hunt - Goal Count"
    range_start = 1
    range_end = 6

    default = 2

class GoalEasterEggHuntRandom(Toggle):
    """Randomize which Easter Eggs are required. If disabled, you may complete any number of enabled maps to meet your Easter Egg Goal Count"""
    display_name = "Easter Egg Hunt - Specific Required Maps"
    default = False

class GoalRound(Range):
    """Round to award Goal Round to award victory on when running the Victory Round goal condition"""
    display_name = "Goal Round - Round Number"
    range_start = 2
    range_end = 100
    default = 25

class GoalRoundCount(Range):
    """Number of maps to meet the goal round to satisfy the win condition. This will not exceed the number of selected maps."""
    display_name = "Goal Round - Number of maps to goal"
    range_start = 1
    range_end = 7
    default = 7

class DifficultyGorodEggCooldown(Toggle):
    """Instantly cool down the egg instead of waiting 2 rounds to retrieve it each time"""
    display_name = "Gorod Krovi - Instant Egg Cooldown"
    default = True

class DifficultyGorodDragonWings(Toggle):
    """Start the game with the Dragon Wings unlocked in the Department Store"""
    display_name = "Gorod Krovi - Starting Dragon Wings"
    default = False

class DifficultyEasterEggCheckpoints(Range):
    """Number of checkpoints along the easter egg quest, for completing various steps."""
    display_name = "Easter Egg Checkpoints"
    default = 0
    range_start = 0
    range_end = 3

class DifficultyRoundCheckpoints(Range):
    """Makes a checkpoint every X round, if above 0"""
    display_name = "Round Checkpoints"
    default = 0
    range_start = 0
    range_end = 15

class AttachmentsEnabled(Toggle):
    """Whether to randomize attachments per weapon per seed"""
    display_name = "Attachments - Randomized"
    default = True

class AttachmentsSightWeight(Range):
    """Probability of a large sight (Recon, Infra-Red etc) being chosen instead of a small sight (Iron sights, reflex etc)"""
    display_name = "Attachments - Large Sight Weighting"
    default = 30
    range_start = 0
    range_end = 100

class CamoEnabled(Toggle):
    display_name = "Camo - Base Weapon Randomized"
    default = True

class CamoMixed(Toggle):
    display_name = "Camo - Base Weapon Can Have Upgraded Camo"
    default = False

class CamoPapEnabled(Toggle):
    display_name = "Camo - Upgraded Weapon Randomized"
    default = True

class CamoPapMixed(Toggle):
    display_name = "Camo - Upgraded Weapon Can Have Base Camo"
    default = False

class CamoJoined(Toggle):
    display_name = "Camo - Base Weapon will match Upgraded Weapon"
    default = False

class ReticleEnabled(Toggle):
    display_name = "Scope Reticle - Base Weapon Randomized"
    default = False

class ReticlePapEnabled(Toggle):
    display_name = "Scope Reticle - Upgraded Weapon Randomized"
    default = True

class ReticleJoined(Toggle):
    display_name = "Scope Reticle - Base Weapon will match Upgraded Weapon"
    default = False

class DeathlinkEnabled(Toggle):
    """Deathlink Enabled. This can be disabled during the AP, but not during it."""
    display_name = "Deathlink Enabled"
    default = False

class DeathlinkSendMode(Choice):
    """Action which will send a deathlink"""
    display_name = "Deathlink Sender Mode"
    default = 0

    option_any_player_down = 0
    option_any_player_death = 1
    option_end_game = 2

class DeathlinkRecvMode(Choice):
    """Consequence of being sent a deathlink"""
    display_name = "Deathlink Receiver Mode"
    default = 0

    option_single_player_down = 0
    option_single_player_death = 1
    option_all_players_down = 2
    option_end_game = 3

class DeathlinkSoloUnlimitedQuickRevive(Toggle):
    """In a solo game, allow more than 3 uses of quick revive when deathlink is enabled"""
    display_name = "Deathlink - More than 3 Solo Quick Revive uses"
    default = True

class DeathlinkSoloFreeQuickRevive(Toggle):
    """In a solo game, unlock quick revive immediately"""
    display_name = "Deathlink - Start with Quick Revive machine turned on"
    default = True

class StartingMapsUnlocked(Range):
    """Number of maps to start unlocked, the rest will require AP items to access"""
    display_name = "Number of Starting Maps"
    default = 1
    
    range_start = 0
    range_end = 15

class ShopPerkTokens(Range):
    """One time use per map (unless save data is cleared), these can be spent to get any perk including those not unlocked yet"""
    display_name = "Shop - Perk Tokens (UNUSED)"
    default = 0

    range_start = 0
    range_end = 10

class ShopMegaGumTokens(Range):
    """One time use per map (unless save data is cleared), these can be spent to get a random mega gobblegum"""
    display_name = "Shop - Mega Gobblegum Tokens"
    default = 3

    range_start = 0
    range_end = 10

class ShopRareGumTokens(Range):
    """One time use per map (unless save data is cleared), these can be spent to get a random rare mega gobblegum"""
    display_name = "Shop - Rare Mega Gobblegum Tokens"
    default = 2

    range_start = 0
    range_end = 10

class ShopLegendaryGumTokens(Range):
    """One time use per map (unless save data is cleared), these can be spent to get a random legandary mega gobblegum"""
    display_name = "Shop - Legendary Mega Gobblegum Tokens"
    default = 1

    range_start = 0
    range_end = 10

class ShopStartingCheckpointTokens(Range):
    """Added to starting inventory. One time use per map (unless save data is cleared), these can be spent to immediately make a checkpoint."""
    display_name = "Shop - Starting Checkpoint Tokens"
    default = 1

    range_start = 0
    range_end = 3

class ShopAdditionalCheckpointTokens(Range):
    """Shuffled into the item pool. One time use per map (unless save data is cleared), these can be spent to immediately make a checkpoint."""
    display_name = "Shop - Additional Checkpoint Tokens"
    default = 1

    range_start = 0
    range_end = 3

@dataclass
class BO3ZombiesOptions(PerGameCommonOptions):
    starting_maps_unlocked: StartingMapsUnlocked
    map_shadows_enabled: MapShadowsEnabled
    map_the_giant_enabled: MapTheGiantEnabled
    map_zetsubou_enabled: MapZetsubouEnabled
    map_castle_enabled: MapCastleEnabled
    map_gorod_enabled: MapGorodKroviEnabled
    map_revelations_enabled: MapRevelationsEnabled
    map_kino_enabled: MapKinoEnabled
    map_workshop_wanted_enabled: MapWorkshopWantedEnabled
    start_map_hints: StartMapHints
    special_rounds_enabled: SpecialRoundsEnabled
    round_location_max: RoundMaxLocation
    round_location_freq: RoundLocationFrequency
    goal_condition: GoalCondition
    goal_round: GoalRound
    goal_round_count: GoalRoundCount
    goal_ee_count: GoalEasterEggCount
    goal_ee_random: GoalEasterEggHuntRandom
    start_quick_revive: StartingQuickRevive
    perk_limit_default_modifier: PerkLimitDefaultModifier
    progressive_perk_limit_increase: ProgressivePerkLimitIncrease
    progressive_starting_points: ProgressiveStartingPoints
    randomized_shield_parts: RandomizeShieldParts
    randomized_gorod_dragonride_parts: RandomizeGorodDragonrideParts
    mystery_box_special_items: MysteryBoxSpecialItems
    mystery_box_regular_items: MysteryBoxRegularItems
    map_specific_wallbuys: MapSpecificWallbuysEnabled
    map_specific_machines: MapSpecificMachinesEnabled
    castle_bow_count: CastleBowCount
    castle_bow_storm: CastleBowEnabledStorm
    castle_bow_wolf: CastleBowEnabledWolf
    castle_bow_fire: CastleBowEnabledFire
    castle_bow_void: CastleBowEnabledVoid
    revelations_mask_count: RevelationsMaskCount
    revelations_mask_enabled_dire_wolf: RevelationsMaskEnabledDireWolf
    revelations_mask_enabled_siegfried: RevelationsMaskEnabledSiegfried
    revelations_mask_enabled_king: RevelationsMaskEnabledKing
    revelations_mask_enabled_fury: RevelationsMaskEnabledFury
    revelations_mask_enabled_margwa: RevelationsMaskEnabledMargwa
    revelations_mask_enabled_keeper_skull: RevelationsMaskEnabledKeeperSkull
    revelations_mask_enabled_apothicon: RevelationsMaskEnabledApothicon
    gift_weight: GiftWeight
    trap_weight: TrapWeight
    difficulty_gorod_egg_cooldown: DifficultyGorodEggCooldown
    difficulty_gorod_dragon_wings: DifficultyGorodDragonWings
    difficulty_ee_checkpoints: DifficultyEasterEggCheckpoints
    difficulty_round_checkpoints: DifficultyRoundCheckpoints
    easter_egg_checks_enabled: EasterEggsEnabled
    music_ee_enabled: MusicEasterEggsEnabled
    attachments_randomized: AttachmentsEnabled
    attachments_sight_weight: AttachmentsSightWeight
    camo_randomized: CamoEnabled
    camo_mixed: CamoMixed
    camo_pap_randomized: CamoPapEnabled
    camo_pap_mixed: CamoPapMixed
    camo_joined: CamoJoined
    reticle_randomized: ReticleEnabled
    reticle_pap_randomized: ReticlePapEnabled
    reticle_joined: ReticleJoined
    deathlink_enabled: DeathlinkEnabled
    deathlink_send_mode: DeathlinkSendMode
    deathlink_recv_mode: DeathlinkRecvMode
    shop_perk_tokens: ShopPerkTokens
    shop_mega_gums: ShopMegaGumTokens
    shop_rare_gums: ShopRareGumTokens
    shop_legendary_gums: ShopLegendaryGumTokens
    shop_starting_checkpoint_tokens: ShopStartingCheckpointTokens
    shop_additional_checkpoint_tokens: ShopAdditionalCheckpointTokens

bo3_option_groups = [
    OptionGroup("General Options", [
        StartingMapsUnlocked,
        RandomizeShieldParts,
        MysteryBoxSpecialItems,
        MysteryBoxRegularItems,
        MapSpecificWallbuysEnabled,
        MapSpecificMachinesEnabled,
        RoundMaxLocation,
        RoundLocationFrequency,
        EasterEggsEnabled,
        MusicEasterEggsEnabled,
        StartingQuickRevive
    ]),
    OptionGroup("Weapons", [
        AttachmentsEnabled,
        AttachmentsSightWeight,
        CamoEnabled,
        CamoMixed,
        CamoPapEnabled,
        CamoPapMixed,
        CamoJoined,
        ReticleEnabled,
        ReticlePapEnabled,
        ReticleJoined
    ]),
    OptionGroup("Goal Conditions", [
        GoalCondition,
        GoalEasterEggHuntRandom,
        GoalEasterEggCount,
        GoalRound,
        GoalRoundCount,
    ]),
    OptionGroup("Progressive Settings", [
        PerkLimitDefaultModifier,
        ProgressivePerkLimitIncrease,
        ProgressiveStartingPoints,
    ]),
    OptionGroup("Map Settings", [
        MapShadowsEnabled,
        MapTheGiantEnabled,
        MapCastleEnabled,
        MapZetsubouEnabled,
        MapGorodKroviEnabled,
        MapRevelationsEnabled,
        MapKinoEnabled,
        StartMapHints,
        CastleBowCount,
        CastleBowEnabledStorm,
        CastleBowEnabledWolf,
        CastleBowEnabledFire,
        CastleBowEnabledVoid,
        RandomizeGorodDragonrideParts,
        RevelationsMaskCount,
        RevelationsMaskEnabledDireWolf,
        RevelationsMaskEnabledSiegfried,
        RevelationsMaskEnabledKing,
        RevelationsMaskEnabledMargwa,
        RevelationsMaskEnabledFury,
        RevelationsMaskEnabledKeeperSkull,
        RevelationsMaskEnabledApothicon,
    ]),
    OptionGroup("Workshop Map Settings", [
        MapWorkshopWantedEnabled,
    ]),
    OptionGroup("Shop Settings", [
        ShopPerkTokens,
        ShopMegaGumTokens,
        ShopRareGumTokens,
        ShopLegendaryGumTokens,
        ShopStartingCheckpointTokens,
        ShopAdditionalCheckpointTokens,
    ]),
    OptionGroup("Difficulty Adjustments", [
        DifficultyGorodEggCooldown,
        DifficultyGorodDragonWings,
        DifficultyEasterEggCheckpoints,
        DifficultyRoundCheckpoints,
    ]),
    OptionGroup("Deathlink", [
        DeathlinkEnabled,
        DeathlinkSendMode,
        DeathlinkRecvMode,
    ]),
    OptionGroup("Filler", [
        GiftWeight,
        TrapWeight,
    ]),
    OptionGroup("WIP", [
        SpecialRoundsEnabled,
    ])
]
