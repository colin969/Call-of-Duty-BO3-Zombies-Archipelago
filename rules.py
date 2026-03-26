from BaseClasses import CollectionState
from . import Locations, Items, Options
from .Options import BO3ZombiesOptions, bo3_option_groups
from .Names import ItemName, LocationName, RegionName, Maps

def can_open_map(state: CollectionState, player: int, options, map_name, third, two_third) -> bool:
    # This is a rule meant to basically say "yeah we can open the map now" based on round logic and current starting points
    starting_points = 500
    starting_points += (500 * state.count(Items.Progressive_StartingPoints500.name, player))
    # Various ways we can pass this check
    # points only - we have enough starting points we don't care about what round we can reach
    points_only = (starting_points >= 5000)
    # mixed - enough starting points and can reach round 7
    mixed = (starting_points >= 2500) and check_round_logic(state, player, options, 7, map_name, third, two_third)
    # round only - we have enough round access logically to reliably open the map
    round_only = check_round_logic(state, player, options, 10, map_name, third, two_third)

    return any([points_only, mixed, round_only])

def check_round_logic(state: CollectionState, player: int, options, round_num, map_name, third, two_third) -> bool:
    # Let's just say we can reach round 5 without any progression items
    round_can_reach = 5
    # Value where we stop caring about round logic because we have enough items based on our settings
    round_max_threshold = 40
    # Number of rounds we add with each perk
    rounds_from_perks = 4
    # Number of rounds from important aspects, like box weapons and pap
    rounds_from_important = 4
    # Number of rounds to from having a shield
    rounds_from_shield = 4

    map_perks = {
        Maps.Shadows_Map_String: Items.Shadows_Machines,
        Maps.The_Giant_Map_String: Items.The_Giant_Machines,
        Maps.Castle_Map_String: Items.Castle_Machines,
        Maps.Zetsubou_Map_String: Items.Zetsubou_Machines,
        Maps.GorodKrovi_Map_String: Items.GorodKrovi_Machines,
        Maps.Revelations_Map_String: Items.Revelations_Machines,
        Maps.Wanted_Map_String: Items.Wanted_Machines,
    }
    map_perks_specific = {
        Maps.Shadows_Map_String: Items.Shadows_Machines_Specific,
        Maps.The_Giant_Map_String: Items.The_Giant_Machines_Specific,
        Maps.Castle_Map_String: Items.Castle_Machines_Specific,
        Maps.Zetsubou_Map_String: Items.Zetsubou_Machines_Specific,
        Maps.GorodKrovi_Map_String: Items.GorodKrovi_Machines_Specific,
        Maps.Revelations_Map_String: Items.Revelations_Machines_Specific,
        Maps.Wanted_Map_String: Items.Wanted_Machines_Specific,
    }
    map_shield = {
        Maps.Shadows_Map_String: Items.Shadows_Shield,
        Maps.Castle_Map_String: Items.Castle_Shield,
        Maps.Zetsubou_Map_String: Items.Zetsubou_Shield,
        Maps.GorodKrovi_Map_String: Items.GorodKrovi_Shield,
        Maps.Revelations_Map_String: Items.Revelations_Shield,
        Maps.Wanted_Map_String: Items.Wanted_Shield
    }

    # The giant doesn't have enough logical perks to hit the round max threshold, so we'll softcap at 35
    if map_name == Maps.The_Giant_Map_String and options.round_location_max.value > 35:
        round_max_threshold = 35

    # We'll start with adjusting our round logic for our perks, +4 logical rounds per perk
    # However, we'll only consider perks we have up to 2 over our current limit (4 perks logical at a 2 perk limit)
    starting_perk_count = 4 + options.perk_limit_default_modifier.value
    current_perk_limit = starting_perk_count + state.count(Items.Progressive_PerkLimitIncrease.name, player)

    # We scale up the rounds from important items the lower our max perk limit is from 5
    # This was no matter our perk limit we can hit the round_max_threshold
    max_perk_limit = starting_perk_count + options.progressive_perk_limit_increase.value
    scaling_threshold = 5
    # If the map has a shield, start scaling other factors up with one less perk limit
    if map_name in list(map_shield.keys()):
        scaling_threshold -= 1
    if max_perk_limit < scaling_threshold:
        # rounds_from_improvement becomes 6 at 4 (3 on maps with shield) max limit, and so on
        round_adjustment = (scaling_threshold - max_perk_limit) * 2
        rounds_from_important += round_adjustment

    # Check if we have our shield
    if map_name in list(map_shield.keys()):
        has_shield = True
        for part in map_shield[map_name]:
            # We don't have our shield, break and give up
            if not state.has(part.name, player):
                has_shield = False
                break
        if has_shield:
            round_can_reach += rounds_from_shield

    # Get our perks based on the map and our perk item setting
    perks = 0
    # Let's only do these calculations if we can even have perks
    if current_perk_limit > 0:
        perks_owned = []
        if options.map_specific_machines:
            perk_list = map_perks_specific[map_name]
        else:
            perk_list = map_perks[map_name]
        perks = 0
        for perk in perk_list:
            if state.has(perk.name, player):
                perks_owned.append(perk.name)
                # Let's not consider deadshot or quick revive for perk logic
                if ("Dead Shot" not in perk.name) and ("Quick Revive" not in perk.name):
                    perks += 1
        # If we have too many perks for our current limit (1 over whatever), limit logical perk count
        if len(perks_owned) > (current_perk_limit + 1):
            # Don't set the perk count based on limit unless our logical perks are actually higher in count
            perks = min(perks, current_perk_limit + 1)
        # If we don't have jugg, lets limit our logical perk count to 2
        has_important_perk = False
        for perk in perks_owned:
            if "Juggernog" in perk:
                has_important_perk = True
                break
        if not has_important_perk and perks > 2:
            perks = 2

    round_can_reach += (perks * rounds_from_perks)

    if options.mystery_box_regular_items:
        # We have a lot of weapons, add 5 rounds
        if state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, player, third):
            round_can_reach += rounds_from_important
        # Now we really have a lot of weapons, add 5 more
        if state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, player, two_third):
            round_can_reach += rounds_from_important
    else:
        round_can_reach += (rounds_from_important * 2)

    # Give 5 rounds logically for each pap upgrade
    current_pap_upgrades = state.count(Items.Progressive_PackAPunch.name, player)
    round_can_reach += (current_pap_upgrades * rounds_from_important)

    return (round_can_reach >= round_num) or (round_can_reach >= round_max_threshold)