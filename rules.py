from BaseClasses import CollectionState
from . import Locations, Items, Options
from .Options import BO3ZombiesOptions, bo3_option_groups
from .Names import ItemName, LocationName, RegionName, Maps
from .Weapons import WeaponData, map_weapon_data_sets, special_weapon_name

import math

map_perks = {
    Maps.Shadows_Map_String: Items.Shadows_Machines,
    Maps.The_Giant_Map_String: Items.The_Giant_Machines,
    Maps.Castle_Map_String: Items.Castle_Machines,
    Maps.Zetsubou_Map_String: Items.Zetsubou_Machines,
    Maps.GorodKrovi_Map_String: Items.GorodKrovi_Machines,
    Maps.Revelations_Map_String: Items.Revelations_Machines,
    Maps.Nacht_Map_String: Items.Nacht_Machines,
    Maps.Kino_Map_String: Items.Kino_Machines,
    Maps.Moon_Map_String: Items.Moon_Machines,
    Maps.Origins_Map_String: Items.Origins_Machines,
    Maps.Wanted_Map_String: Items.Wanted_Machines,
}
map_perks_specific = {
    Maps.Shadows_Map_String: Items.Shadows_Machines_Specific,
    Maps.The_Giant_Map_String: Items.The_Giant_Machines_Specific,
    Maps.Castle_Map_String: Items.Castle_Machines_Specific,
    Maps.Zetsubou_Map_String: Items.Zetsubou_Machines_Specific,
    Maps.GorodKrovi_Map_String: Items.GorodKrovi_Machines_Specific,
    Maps.Revelations_Map_String: Items.Revelations_Machines_Specific,
    Maps.Nacht_Map_String: Items.Nacht_Machines_Specific,
    Maps.Kino_Map_String: Items.Kino_Machines_Specific,
    Maps.Moon_Map_String: Items.Moon_Machines_Specific,
    Maps.Origins_Map_String: Items.Origins_Machines_Specific,
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

def can_open_map(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name) -> bool:
    # This is a rule meant to basically say "yeah we can open the map now" based on round logic and current starting points
    starting_points = 500
    starting_points += (500 * state.count(Items.Progressive_StartingPoints500.name, player))
    # Various ways we can pass this check
    # points only - we have enough starting points we don't care about what round we can reach
    points_only = (starting_points >= 5000)
    # round only - we have enough round access logically to reliably open the map
    round_only = check_round_logic(state, player, options, 10, map_name)

    return points_only or round_only

def get_map_weapon_data(map_name: str, options: BO3ZombiesOptions) -> tuple[dict[str, WeaponData], dict[str, WeaponData]]:
    weapon_list: dict[str, WeaponData] = {}
    full_weapon_list: dict[str, WeaponData] = {}
    if map_name in map_weapon_data_sets:
        weapon_data_set = map_weapon_data_sets[map_name]

        full_weapon_list = {**weapon_data_set.vanilla, **weapon_data_set.special, **weapon_data_set.wallbuys}
        if options.mystery_box_regular_items and options.mystery_box_expanded:
            full_weapon_list.update(weapon_data_set.expanded)

        weapon_list = weapon_data_set.wallbuys.copy()
        if options.mystery_box_special_items:
            weapon_list.update(weapon_data_set.special)
        if options.mystery_box_regular_items:
            weapon_list.update(weapon_data_set.vanilla)
            if options.mystery_box_expanded:
                weapon_list.update(weapon_data_set.expanded)

    return (weapon_list, full_weapon_list)

# Check whether player has more than (decimal) percentage of their weapon unlocks for a map
def has_weapon_percentage(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name: str, percent: float) -> bool:
    weapon_data, full_weapon_data = get_map_weapon_data(map_name, options)
    # Names of all pooled weapons
    weapon_keys = [item.item_name for item in weapon_data.values()]
    full_count = len(full_weapon_data.keys())
    # How many weapons that aren't shuffled
    initial_num = full_count - len(weapon_keys)

    return state.count_from_list_unique(weapon_keys, player) + initial_num >= math.floor(full_count * percent)

def has_shield(state: CollectionState, player: int, map_name: str) -> bool:
    if map_name in map_shield:
        return state.has_all([item.name for item in map_shield[map_name]], player)
    else:
        return True

def has_sniper(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name: str) -> bool:
    weapon_data, full_weapon_data = get_map_weapon_data(map_name, options)
    for weapon_key, weapon in full_weapon_data.items():
        if weapon.category == "sniper":
            # Unrando'd sniper
            if weapon_key not in weapon_data:
                return True
            # Found sniper
            if state.has(weapon.item_name, player):
                return True
    return False

def has_weapon_of_strength(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name: str, strength: int, count = 1) -> bool:
    counted, total = count_weapons_of_strength(state, player, options, map_name, strength)
    if total < count:
        return True
    if counted >= count:
        return True
    return False

def has_special_weapon(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name: str, weapon_name: str) -> bool:
    if options.mystery_box_special_items.value == 0:
        return True
    return state.has(special_weapon_name(map_name, weapon_name), player)

def has_perk(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name: str, perk_name: str) -> bool:
    perks = map_perks[map_name]
    if perk_name not in perks:
        return True

    if options.map_specific_machines:
        return state.has(map_name + " " + perk_name, player)
    return state.has(perk_name, player)

def count_weapons_of_strength(state: CollectionState, player: int, options: BO3ZombiesOptions, map_name: str, strength: int) -> tuple[int, int]:
    has_phd = has_perk(state, player, options, map_name, ItemName.Machine_PhdFlopper)
    weapon_data, full_weapon_data = get_map_weapon_data(map_name, options)
    total = 0
    counted = 0
    for weapon_key, weapon in full_weapon_data.items():
        if has_phd and weapon.phd_modifier > 0:
            if (weapon.strength + weapon.phd_modifier) >= strength:
                total += 1
                if weapon_key not in weapon_data:
                    counted += 1
                elif state.has(weapon.item_name, player):
                    counted += 1
        elif weapon.strength >= strength:
            total += 1
            if weapon_key not in weapon_data:
                counted += 1
            elif state.has(weapon.item_name, player):
                counted += 1
    return counted, total


def check_round_logic(state: CollectionState, player: int, options: BO3ZombiesOptions, round_num, map_name: str) -> bool:
    # Let's just say we can reach round 6 without any progression items
    round_can_reach = 6
    # Value where we stop caring about round logic because we have enough items based on our settings
    round_max_threshold = 36
    # Number of rounds we add with each perk
    rounds_from_perks = 4
    # Number of rounds from important aspects, like box weapons and pap
    rounds_from_important = 4
    # Number of rounds to from having a shield
    rounds_from_shield = 4

    has_jugg = False

    weapon_data, full_weapon_data = get_map_weapon_data(map_name, options)
    # Names of all pooled weapons
    weapon_keys = [item.item_name for item in weapon_data.values()]
    full_count = len(full_weapon_data.keys())
    # How many weapons that aren't shuffled
    initial_num = full_count - len(weapon_keys)

    # Lets look at the length of our map's perks, and adjust the round threshold accordingly
    perks_copy = map_perks[map_name]
    # Looping through the full list of perks for the map, and removing from the copy as needed to get logical perk count
    for perk in map_perks[map_name]:
        # Remove deadshot and only remove quick revive if we start with it
        if ("Dead Shot" in perk.name) or ("Quick Revive" in perk.name and options.start_quick_revive):
            perks_copy.remove(perk)

    # Our number of logical perks for the map
    num_logical_perks = len(perks_copy)

    # Or we're the giant and quick revive is started with, we'll cheat here and say there's 4 because perk rng
    # when we consider staminup vs deadshot spawning
    if map_name == Maps.The_Giant_Map_String and options.start_quick_revive:
        num_logical_perks = 4

    # If we're at less than 5, we can't hit round 40 threshold, adjust accordingly
    if num_logical_perks < 5:
        times_to_adjust = (5 - num_logical_perks)
        round_max_threshold -= (times_to_adjust * 5)

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
    if options.map_specific_machines:
        perk_list = map_perks_specific[map_name]
    else:
        perk_list = map_perks[map_name]
    perks_owned = []
    for perk in perk_list:
        if state.has(perk.name, player):
            perks_owned.append(perk.name)
            # Let's not consider deadshot or quick revive for perk logic
            if ("Dead Shot" in perk.name) or (options.start_quick_revive and ("Quick Revive" in perk.name)):
                continue
            perks += 1
    rule_perks = perks
    # Let's only do these calculations if we can even have perks
    if current_perk_limit > 0:
        # If we have too many perks for our current limit (1 over whatever), limit logical perk count
        if len(perks_owned) > (current_perk_limit):
            # Don't set the perk count based on limit unless our logical perks are actually higher in count
            perks = min(perks, current_perk_limit)
        # If we don't have jugg, reduce value of perks past our first
        for perk in perks_owned:
            if "Juggernog" in perk:
                has_jugg = True
                break

    round_can_reach += (perks * rounds_from_perks)

    weap_item_count = state.count_from_list_unique(weapon_keys, player) + initial_num
    total_weap_rounds = rounds_from_important * 2
    earned_weap_rounds = math.floor(total_weap_rounds * (weap_item_count / full_count))
    round_can_reach += earned_weap_rounds

    # Give 4 rounds logically for each pap upgrade
    current_pap_upgrades = state.count(Items.Progressive_PackAPunch.name, player)
    round_can_reach += (current_pap_upgrades * rounds_from_important)
    
    # Certain hard requirements for better balancing
    if len(perk_list) >= 4 and rule_perks < 2:
        round_can_reach = min(10, round_can_reach)
    if len(perk_list) >= 6 and rule_perks < 3:
        round_can_reach = min(18, round_can_reach)
    if weap_item_count < math.floor(full_count * 0.3):
        round_can_reach = min(12, round_can_reach)
    if not has_jugg:
        round_can_reach = min(12, round_can_reach)
    if current_pap_upgrades == 0:
        round_can_reach = min(16, round_can_reach)

    return (round_can_reach >= round_num) or (round_can_reach >= round_max_threshold)
