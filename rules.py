from BaseClasses import CollectionState
from . import Locations, Items, Options
from .Options import BO3ZombiesOptions, bo3_option_groups
from .Names import ItemName, LocationName, RegionName, Maps


def check_round_logic(state: CollectionState, player: int, options, round_num, map_name, third, two_third) -> bool:
    # Let's just say we can reach round 5 without any progression items
    round_can_reach = 5
    # Value where we stop caring about round logic because we have enough items based on our settings
    round_max_threshold = 40
    # Number of rounds we add with each perk
    rounds_from_perks = 4
    # Number of rounds from important aspects, like box weapons and pap
    rounds_from_important = 4

    # We'll start with adjusting our round logic for our perks, +4 logical rounds per perk
    # However, we'll only consider perks we have up to 2 over our current limit (4 perks logical at a 2 perk limit)
    starting_perk_count = 4 + options.perk_limit_default_modifier.value
    current_perk_limit = starting_perk_count + state.count(Items.Progressive_PerkLimitIncrease.name, player)

    # We scale up the rounds from important items the lower our max perk limit is from 5
    # This was no matter our perk limit we can hit the round_max_threshold
    max_perk_limit = starting_perk_count + options.progressive_perk_limit_increase.value
    if max_perk_limit < 5:
        # rounds_from_improvement becomes 6 at 4 max limit, and so on
        round_adjustment = (5 - max_perk_limit) * 2
        rounds_from_important += round_adjustment

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
                # Let's... not consider deadshot for perk logic LOL
                if "Dead Shot" not in perk.name:
                    perks += 1
        # If we have too many perks for our current limit (1 over whatever), limit logical perk count
        if perks > (current_perk_limit + 1):
            perks = current_perk_limit + 1
        # If we don't have quick revive or jugg, lets limit our logical perk count to 2
        has_important_perk = False
        for perk in perks_owned:
            if ("Juggernog" in perk) or ("QuickRevive" in perk):
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