import string
import math
import os
import json

from BaseClasses import Location, MultiWorld, Region, Item, ItemClassification, CollectionState
from worlds.generic.Rules import CollectionRule
from . import rules

from worlds.AutoWorld import World, WebWorld

# from rule_builder.rules import Has, HasAll, HasGroupUnique

from . import Locations, Items, Options
from .Options import BO3ZombiesOptions, bo3_option_groups
from .Names import ItemName, LocationName, RegionName, Maps

class BO3ZombiesWeb(WebWorld):
    theme = "ocean"
    option_groups = bo3_option_groups

class BO3ZombiesLocation(Location):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {loc_data.name: loc_data.code + base_id for loc_data in Locations.all_locations}

class BO3ZombiesWorld(World):
    """
    TODO: Game Description
    """
    game: str = "Black Ops 3 - Zombies"
    web = BO3ZombiesWeb()

    options_dataclass = BO3ZombiesOptions
    options: BO3ZombiesOptions

    required_client_version = (0, 6, 0)

    topology_present = True
    # Game's SteamID
    base_id = 311210
    item_name_to_id = Items.BO3ZombiesItem.get_name_to_id(base_id)
    location_name_to_id = BO3ZombiesLocation.get_name_to_id(base_id)

    item_name_groups = Items.item_groups

    # Full Remote Items
    items_handling = 0b111

    # Enable to log the location lua data
    write_lua_locations = False

    def generate_early(self) -> None:
        if self.write_lua_locations:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(script_dir, 'Locations.lua'), 'w', encoding='utf-8') as f:
                f.write("local LocationToID = {}\n")
                f.write("local IDToLocation = {}\n")
                for location in Locations.all_locations:
                    f.write("LocationToID[\"{}\"] = {}\n".format(location.name, location.code))
                    f.write("IDToLocation[{}] = \"{}\"\n".format(location.code, location.name))
                f.write("local locations = { LocationToID = LocationToID, IDToLocation = IDToLocation }\n")
                f.write("return locations\n")

        # At least one map has to be enabled
        if (not self.options.map_shadows_enabled and not self.options.map_castle_enabled
            and not self.options.map_zetsubou_enabled and not self.options.map_gorod_enabled
            and not self.options.map_revelations_enabled and not self.options.map_the_giant_enabled):
            self.options.map_shadows_enabled.value = True

        self.mystery_box_regular_items = []
        if self.options.mystery_box_regular_items:
            seen = set()
            if self.options.map_the_giant_enabled:
                add_universal_items(self.mystery_box_regular_items, seen, Items.The_Giant_MysteryBox_Regular)
            if self.options.map_shadows_enabled:
                add_universal_items(self.mystery_box_regular_items, seen, Items.Shadows_MysteryBox_Regular)
            if self.options.map_castle_enabled:
                add_universal_items(self.mystery_box_regular_items, seen, Items.Castle_MysteryBox_Regular)
            if self.options.map_zetsubou_enabled:
                add_universal_items(self.mystery_box_regular_items, seen, Items.Zetsubou_MysteryBox_Regular)
            if self.options.map_gorod_enabled:
                add_universal_items(self.mystery_box_regular_items, seen, Items.GorodKrovi_MysteryBox_Regular)
            if self.options.map_revelations_enabled:
                add_universal_items(self.mystery_box_regular_items, seen, Items.Revelations_MysteryBox_Regular)
            if self.options.map_workshop_wanted_enabled:
                self.mystery_box_regular_items += Items.Wanted_MysteryBox_Regular
        self.mystery_box_regular_items_two_third = math.ceil(len(self.mystery_box_regular_items) * 0.67)
        self.mystery_box_regular_items_third = math.ceil(len(self.mystery_box_regular_items) * 0.33)

        self.mystery_box_special_items = []
        if self.options.mystery_box_special_items:
            if self.options.map_the_giant_enabled:
                self.mystery_box_special_items += Items.The_Giant_MysteryBox
            if self.options.map_shadows_enabled:
                self.mystery_box_special_items += Items.Shadows_MysteryBox
            if self.options.map_castle_enabled:
                self.mystery_box_special_items += Items.Castle_MysteryBox
            if self.options.map_zetsubou_enabled:
                self.mystery_box_special_items += Items.Zetsubou_MysteryBox
            if self.options.map_gorod_enabled:
                self.mystery_box_special_items += Items.GorodKrovi_MysteryBox
            if self.options.map_revelations_enabled:
                self.mystery_box_special_items += Items.Revelations_MysteryBox
            if self.options.map_workshop_wanted_enabled:
                self.mystery_box_special_items += Items.Wanted_MysteryBox

        self.rolled_bows = []
        self.weapon_quest_items = []
        pass

    def create_regions(self):
        is_ut = getattr(self.multiworld, "generation_is_fake", False)

        # Create list of already unlocked maps
        locked_maps = []
        if self.options.map_shadows_enabled:
            locked_maps.append(ItemName.Map_Shadows)
        if self.options.map_castle_enabled:
            locked_maps.append(ItemName.Map_Castle)
        if self.options.map_zetsubou_enabled:
            locked_maps.append(ItemName.Map_Zetsubou)
        if self.options.map_gorod_enabled:
            locked_maps.append(ItemName.Map_GorodKrovi)
        if self.options.map_revelations_enabled:
            locked_maps.append(ItemName.Map_Revelations)
        if self.options.map_the_giant_enabled:
            locked_maps.append(ItemName.Map_The_Giant)
        if self.options.map_workshop_wanted_enabled:
            locked_maps.append(ItemName.Map_Wanted)

        self.num_maps = len(locked_maps)

        # Randomly picked selected starting maps
        starting_maps_unlocked = min(self.options.starting_maps_unlocked.value, len(locked_maps))
        if starting_maps_unlocked > 0:
            starting_maps = []
            left_to_pick = starting_maps_unlocked
            # Collect from starting inventory first
            for item in self.options.start_inventory:
                if item in locked_maps:
                    left_to_pick -= 1
                    starting_maps.append(item)
                    locked_maps.remove(item)
            # Fill rest of starting maps randomly
            if left_to_pick > 0:
                self.random.shuffle(locked_maps)
                starting_maps.extend(locked_maps[:left_to_pick])
                locked_maps = locked_maps[left_to_pick:]
            # Precollect starting maps
            for item in map(self.create_item, starting_maps):
                self.push_precollected(item)
        else:
            for item in map(self.create_item, locked_maps):
                self.push_precollected(item)
            locked_maps = []

        # Auto-hint map unlocks, let players spend hints on things they really want, not what they desperately need
        for item in locked_maps:
            self.options.start_hints.value.add(item)
        self.cod_locked_maps = locked_maps

        universal_locations = [
            LocationName.RepairWindows_5
        ]
        menu_region = self.create_region(self.multiworld, self.player, 'Menu', universal_locations)
        add_ee_checks = self.options.goal_condition == 0 or self.options.easter_egg_checks_enabled

        self.multiworld.regions.append(menu_region)
        
        # Default Balancing, Make sure you get to every region
        # TODO: Randomize this a bit/weight it
        
        is_round_goal_cond = self.options.goal_condition == 2
        goal_round = self.options.goal_round
        round_max = self.options.round_location_max
        if is_round_goal_cond:
            round_max = min(round_max, goal_round)
        round_freq = self.options.round_location_freq

        if self.options.map_shadows_enabled:
            all_locations = []
            #free_locs, quarter_locs, half_locs = add_round_locations(Locations.Shadows_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            #all_locations.extend(free_locs)
            all_locations.extend([loc.name for loc in Locations.Shadows_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_ApothiconSword_Locations])
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.Shadows_Quest_Music_Locations])

            main_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_Alleyway, all_locations)
            self.multiworld.regions.append(main_region)
            # create_entrance(menu_region, main_region, Has(ItemName.Map_Shadows))
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_Shadows, self.player))

            servant_locations = []
            servant_locations.extend([loc.name for loc in Locations.Shadows_ApothiconServant_Locations])
            servant_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_Servant, servant_locations)
            self.multiworld.regions.append(servant_region)
            rule: CollectionRule = lambda state: rules.check_round_logic(state, self.player, self.options, 12, "(Shadows of Evil)", self.mystery_box_regular_items_third, self.mystery_box_regular_items_two_third)
            create_entrance(main_region, servant_region, rule)

            #self.add_quarter_round_region(main_region, RegionName.Shadows_Quarter_Weapons, quarter_locs)
            #self.add_half_round_region(main_region, RegionName.Shadows_Half_Weapons, half_locs)

            # widows_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_Widows, [loc.name for loc in Locations.Shadows_Widows_Locations])
            # self.multiworld.regions.append(widows_region)
            # create_entrance(main_region, widows_region, lambda state: state.has(ItemName.Machine_WidowsWine) or state.has(Maps.Shadows_Map_String + " - " + ItemName.Machine_WidowsWine))

            # raygun_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_RayGun, [loc.name for loc in Locations.Shadows_RayGun_Locations])
            # self.multiworld.regions.append(raygun_region)
            # create_entrance(main_region, raygun_region, lambda state: (not self.options.mystery_box_special_items) or state.has(Items.Shadows_MysteryBox[0].name, self.player))

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Shadows_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_MainEE, ee_locs)
            # rule = Has(ItemName.Progressive_PackAPunch) & HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third)
            # if self.options.randomized_shield_parts:
            #     rule = rule & HasAll(*[item.name for item in Items.Shadows_Shield])
            # if self.options.mystery_box_special_items:
            #     rule = rule & HasAll(*[item.name for item in Items.Shadows_MysteryBox])
            # create_entrance(main_region, main_ee_region, rule)
            create_entrance(
                main_region, 
                main_ee_region, 
                lambda state: (
                        state.has(ItemName.Progressive_PackAPunch, self.player) and
                        (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True) and
                        state.has_all({item.name for item in Items.Shadows_Shield}, self.player) and
                        (state.has_all({item.name for item in Items.Shadows_MysteryBox}, self.player) if self.options.mystery_box_special_items else True)
                )
            )

            upgraded_locs = [loc.name for loc in Locations.Shadows_Quest_ApothiconSword_Upgrade_Locations]
            upgraded_weapon_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_Upgraded, upgraded_locs)
            # create_entrance(main_region, upgraded_weapon_region, HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third))
            create_entrance(main_region, upgraded_weapon_region, lambda state: (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True))

            upgraded_arnies_locs = [loc.name for loc in Locations.Shadows_LilArnies_Locations]
            upgraded_arnies_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_Arnies, upgraded_arnies_locs)
            self.multiworld.regions.append(upgraded_arnies_region)
            create_entrance(main_region, upgraded_arnies_region, lambda state:
                ((not self.options.mystery_box_special_items) or state.has(Items.Shadows_MysteryBox[1].name, self.player))
                and (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True)
            )

        if self.options.map_the_giant_enabled:
            all_locations = [loc.name for loc in Locations.TheGiant_Quest_Locations]
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.TheGiant_Quest_Music_Locations])
                
            #free_locs, quarter_locs, half_locs = add_round_locations(Locations.TheGiant_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            #all_locations.extend(free_locs)

            main_region = self.create_region(self.multiworld, self.player, RegionName.TheGiant_Courtyard, all_locations)
            self.multiworld.regions.append(main_region)
            # create_entrance(menu_region, main_region, Has(ItemName.Map_The_Giant))
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_The_Giant, self.player))


            pap_region = self.create_region(self.multiworld, self.player, RegionName.TheGiant_Pap, [loc.name for loc in Locations.TheGiant_Pap])
            self.multiworld.regions.append(pap_region)
            # create_entrance(main_region, pap_region, Has(Items.Progressive_PackAPunch.name))
            create_entrance(main_region, pap_region, lambda state: state.has(ItemName.Progressive_PackAPunch, self.player))


            monkeybomb_region = self.create_region(self.multiworld, self.player, RegionName.TheGiant_MonkeyBombs, [loc.name for loc in Locations.TheGiant_MonkeyBomb])
            self.multiworld.regions.append(monkeybomb_region)
            # create_entrance(main_region, monkeybomb_region, Has(Items.The_Giant_MysteryBox[2].name))
            if self.options.mystery_box_special_items:
                create_entrance(main_region, monkeybomb_region, lambda state: state.has(Items.The_Giant_MysteryBox[2].name, self.player))
            else:
                create_entrance(main_region, monkeybomb_region)

            #self.add_quarter_round_region(main_region, RegionName.TheGiant_Quarter_Weapons, quarter_locs)
            #self.add_half_round_region(main_region, RegionName.TheGiant_Half_Weapons, half_locs)

        if self.options.map_castle_enabled:
            all_locations = []

            bow_pairs = [
                (Locations.Castle_Quest_ElementalBow_Storm_Locations, ItemName.Castle_Victory_ElementalBow_Storm),
                (Locations.Castle_Quest_ElementalBow_Wolf_Locations, ItemName.Castle_Victory_ElementalBow_Wolf),
                (Locations.Castle_Quest_ElementalBow_Fire_Locations, ItemName.Castle_Victory_ElementalBow_Fire),
                (Locations.Castle_Quest_ElementalBow_Void_Locations, ItemName.Castle_Victory_ElementalBow_Void),
            ]
            bow_count = min(self.options.castle_bow_count.value, len(bow_pairs))
            # Make sure universal tracker sees all 4 location groups
            if not is_ut:
                bow_pairs = self.random.sample(bow_pairs, bow_count)
            for bow in bow_pairs:
                all_locations.extend([loc.name for loc in bow[0]])
                self.weapon_quest_items.append(bow[1])
                if bow[1] == ItemName.Castle_Victory_ElementalBow_Storm:
                    self.rolled_bows.append("storm")
                if bow[1] == ItemName.Castle_Victory_ElementalBow_Wolf:
                    self.rolled_bows.append("wolf")
                if bow[1] == ItemName.Castle_Victory_ElementalBow_Fire:
                    self.rolled_bows.append("fire")
                if bow[1] == ItemName.Castle_Victory_ElementalBow_Void:
                    self.rolled_bows.append("void")


            #free_locs, quarter_locs, half_locs = add_round_locations(Locations.Castle_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            #all_locations.extend(free_locs)
            all_locations.extend([loc.name for loc in Locations.Castle_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Castle_Quest_Locations])
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.Castle_Quest_Music_Locations])
                
            main_region = self.create_region(self.multiworld, self.player, RegionName.Castle_Gondola, all_locations)
            self.multiworld.regions.append(main_region)
            # create_entrance(menu_region, main_region, Has(ItemName.Map_Castle))
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_Castle, self.player))

            dg4_locations = []
            dg4_locations.extend([loc.name for loc in Locations.Castle_DG4_Locations])
            dg4_region = self.create_region(self.multiworld, self.player, RegionName.Castle_DG4, dg4_locations)
            self.multiworld.regions.append(dg4_region)
            rule: CollectionRule = lambda state: rules.check_round_logic(state, self.player, self.options, 12, "(Castle)", self.mystery_box_regular_items_third, self.mystery_box_regular_items_two_third)
            create_entrance(main_region, dg4_region, rule)

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Castle_Quest_MainEE_Locations[:4]]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Castle_MainEE, ee_locs)
            create_entrance(
                main_region, 
                main_ee_region, 
                lambda state: (
                    state.has(ItemName.Progressive_PackAPunch, self.player) and
                    (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True) and
                    state.has_all({item.name for item in Items.Castle_Shield}, self.player) and
                    (state.has_all({item.name for item in Items.Castle_MysteryBox}, self.player) if self.options.mystery_box_special_items else True)
                )
            )

            # Weapon Quest - Add available bows
            if self.options.goal_condition == 1:
                for bow in bow_pairs:
                    self.multiworld.get_location(bow[0][-1].name, self.player).place_locked_item(self.create_item(bow[1]))
            
            boss_fight_locations = []
            if add_ee_checks:
                boss_fight_locations = [loc.name for loc in Locations.Castle_Quest_MainEE_Locations[4:]]
            boss_region = self.create_region(self.multiworld, self.player, RegionName.Castle_BossFight, boss_fight_locations)
            self.multiworld.regions.append(boss_region)
            main_ee_region.connect(boss_region, rule = lambda state: state.has_all([item.name for item in Items.Castle_Craftables], self.player))

        if self.options.map_zetsubou_enabled:
            all_locations = []
            #free_locs, quarter_locs, half_locs = add_round_locations(Locations.Zetsubou_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            #all_locations.extend(free_locs)
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_Challenges_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_KT4_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_Skull_Locations])
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_Music_Locations])

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Zetsubou_Quest_MainEE_Locations]

            main_region = self.create_region(self.multiworld, self.player, RegionName.Zetsubou_Beach, all_locations)
            self.multiworld.regions.append(main_region)
            # create_entrance(menu_region, main_region, Has(ItemName.Map_Zetsubou))
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_Zetsubou, self.player))

            #self.add_quarter_round_region(main_region, RegionName.Zetsubou_Quarter_Weapons, quarter_locs)
            #self.add_half_round_region(main_region, RegionName.Zetsubou_Half_Weapons, half_locs)

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Zetsubou_MainEE, ee_locs)
            # rule = Has(ItemName.Progressive_PackAPunch) & HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third)
            # if self.options.randomized_shield_parts:
            #     rule = rule & HasAll(*[item.name for item in Items.Zetsubou_Shield])
            # if self.options.mystery_box_special_items:
            #     rule = rule & HasAll(*[item.name for item in Items.Zetsubou_MysteryBox])
            # rule = rule & HasAll(*[item.name for item in Items.Zetsubou_Craftables_Gasmask])
            # create_entrance(main_region, main_ee_region, rule)
            create_entrance(
                main_region, 
                main_ee_region, 
                lambda state: (
                    state.has(ItemName.Progressive_PackAPunch, self.player) and
                    (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True) and
                    state.has_all({item.name for item in Items.Zetsubou_Shield}, self.player) and
                    (state.has_all({item.name for item in Items.Zetsubou_MysteryBox}, self.player) if self.options.mystery_box_special_items else True)
                )
            )

            upgraded_locs = [loc.name for loc in Locations.Zetsubou_Quest_Masamune_Locations]
            upgraded_weapon_region = self.create_region(self.multiworld, self.player, RegionName.Zetsubou_Upgraded, upgraded_locs)
            # create_entrance(main_region, upgraded_weapon_region, HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third))
            create_entrance(main_region, upgraded_weapon_region, lambda state: (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True))

        if self.options.map_gorod_enabled:
            all_locations = []
            #free_locs, quarter_locs, half_locs = add_round_locations(Locations.GorodKrovi_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            #all_locations.extend(free_locs)
            all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.GorodKrovi_Craftable_Locations])
            # Remove dragon wings location if we start with them
            if self.options.difficulty_gorod_dragon_wings:
                all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_SideEE[1:]])
            else:
                all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_SideEE])
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_Music_Locations])

            main_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_Trenches, all_locations)
            self.multiworld.regions.append(main_region)
            # create_entrance(menu_region, main_region, Has(ItemName.Map_GorodKrovi))
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_GorodKrovi, self.player))


            bunker_locs = [loc.name for loc in Locations.GorodKrovi_Quest_DragonStrikes]
            bunker_locs.extend([loc.name for loc in Locations.GorodKrovi_Quest_DragonGauntlets_Early])
            bunker_locs.append(Locations.GorodKrovi_Quest_Challenges[0].name)
            bunker_locs.append(Locations.GorodKrovi_Quest_Challenges[2].name)
            bunker_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_Bunker, bunker_locs)
            create_entrance(
                main_region,
                bunker_region,
            )

            #self.add_quarter_round_region(main_region, RegionName.Gorod_Quarter_Weapons, quarter_locs)
            #self.add_half_round_region(main_region, RegionName.Gorod_Half_Weapons, half_locs)

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.GorodKrovi_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_MainEE, ee_locs)
            # rule = Has(ItemName.Progressive_PackAPunch) & HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third)
            # if self.options.randomized_shield_parts:
            #     rule = rule & HasAll(*[item.name for item in Items.GorodKrovi_Shield])
            # if self.options.mystery_box_special_items:
            #     rule = rule & HasAll(*[item.name for item in Items.GorodKrovi_MysteryBox])
            # create_entrance(main_region, main_ee_region, rule)
            create_entrance(
                bunker_region, 
                main_ee_region, 
                lambda state: (
                    state.has(ItemName.Progressive_PackAPunch, self.player) and
                    (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True) and
                    state.has_all({item.name for item in Items.GorodKrovi_Shield}, self.player) and
                    (state.has_all({item.name for item in Items.GorodKrovi_MysteryBox}, self.player) if self.options.mystery_box_special_items else True)
                )
            )

            # Checks which require the shield items
            shield_locations = (
                [Locations.GorodKrovi_Quest_Challenges[1].name] +
                [loc.name for loc in Locations.GorodKrovi_Quest_TiamatsMaw]
            )
            shield_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_Shield, shield_locations)
            self.multiworld.regions.append(shield_region)
            # create_entrance(main_region, shield_region, HasAll(*[item.name for item in Items.GorodKrovi_Shield]))
            create_entrance(main_region, shield_region, lambda state: state.has_all([item.name for item in Items.GorodKrovi_Shield], self.player))

            # Monkey Bomb upgrade location - Requires shield as well as monkey bombs in box
            monkeybomb_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_MonkeyBombs, [Locations.GorodKrovi_Quest_Challenges[3].name])
            self.multiworld.regions.append(monkeybomb_region)
            if self.options.mystery_box_special_items:
                # create_entrance(shield_region, monkeybomb_region, Has(Items.GorodKrovi_MysteryBox[1].name))
                create_entrance(shield_region, monkeybomb_region, lambda state: state.has(Items.GorodKrovi_MysteryBox[1].name, self.player))
            else:
                create_entrance(shield_region, monkeybomb_region)


            upgraded_locs = [loc.name for loc in Locations.GorodKrovi_Quest_DragonStrikes_Upgraded]
            upgraded_locs += [loc.name for loc in Locations.GorodKrovi_Quest_DragonGauntlets_Late]
            upgraded_weapon_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_Upgraded, upgraded_locs)
            # create_entrance(main_region, upgraded_weapon_region, HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third))
            create_entrance(bunker_region, upgraded_weapon_region, lambda state: (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True))

        if self.options.map_revelations_enabled:
            all_locations = []
            # free_locs, quarter_locs, half_locs = add_round_locations(Locations.Revelations_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            # all_locations.extend(free_locs)
            all_locations.extend([loc.name for loc in Locations.Revelations_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Revelations_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Revelations_Quest_SideEE_Locations])
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.Revelations_Quest_Music_Locations])

            main_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_House, all_locations)
            self.multiworld.regions.append(main_region)
            # create_entrance(menu_region, main_region, Has(ItemName.Map_Revelations))
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_Revelations, self.player))

            # Round 18 logic for the panzer/margwa challenges and shield for the possible shield challenge
            challenge_locations = []
            challenge_locations.extend([loc.name for loc in Locations.Revelations_Quest_Challenges])
            challenge_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_Challenges, challenge_locations)
            self.multiworld.regions.append(challenge_region)
            rule: CollectionRule = lambda state: (
                rules.check_round_logic(state, self.player, self.options, 18, "(Revelations)", self.mystery_box_regular_items_third, self.mystery_box_regular_items_two_third) and
                state.has_all({item.name for item in Items.Revelations_Shield}, self.player)
            )
            create_entrance(main_region, challenge_region, rule)

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Revelations_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_MainEE, ee_locs)
            self.multiworld.regions.append(main_ee_region)
            # rule = Has(ItemName.Progressive_PackAPunch) & HasGroupUnique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.mystery_box_regular_items_two_third)
            # if self.options.randomized_shield_parts:
            #     rule = rule & HasAll(*[item.name for item in Items.Revelations_Shield])
            # if self.options.mystery_box_special_items:
            #     rule = rule & HasAll(*[item.name for item in Items.Revelations_MysteryBox])
            # create_entrance(main_region, main_ee_region, rule)
            create_entrance(
                main_region, 
                main_ee_region, 
                lambda state: (
                    state.has(ItemName.Progressive_PackAPunch, self.player) and
                    (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True) and
                    state.has_all({item.name for item in Items.Revelations_Shield}, self.player) and
                    (state.has_all({item.name for item in Items.Revelations_MysteryBox}, self.player) if self.options.mystery_box_special_items else True)
                )
            )

            apothicon_ugprade_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_Apothicon_Upgrade, [Locations.Revelations_Quest_Weapons[0].name])
            if self.options.mystery_box_special_items:
                # create_entrance(main_region, apothicon_ugprade_region, Has(Items.Revelations_MysteryBox[2].name))
                create_entrance(main_region, apothicon_ugprade_region, lambda state: state.has(Items.Revelations_MysteryBox[2].name, self.player))
            else:
                create_entrance(main_region, apothicon_ugprade_region)


            arnies_ugprade_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_Arnies_Upgrade, [Locations.Revelations_Quest_Weapons[1].name])
            if self.options.mystery_box_special_items:
                # create_entrance(main_region, arnies_ugprade_region, Has(Items.Revelations_MysteryBox[1].name))
                create_entrance(main_region, arnies_ugprade_region, lambda state: state.has(Items.Revelations_MysteryBox[1].name, self.player))
            else:
                create_entrance(main_region, arnies_ugprade_region)

        # == Modded Maps ==

        if self.options.map_workshop_wanted_enabled:
            all_locations = []
            # free_locs, quarter_locs, half_locs = add_round_locations(Locations.Revelations_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            # all_locations.extend(free_locs)
            all_locations.extend([loc.name for loc in Locations.Wanted_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Wanted_Quest_Weapons])
            all_locations.extend([loc.name for loc in Locations.Wanted_Craftable_Locations])
            main_region = self.create_region(self.multiworld, self.player, RegionName.Wanted_Town, all_locations)
            self.multiworld.regions.append(main_region)
            create_entrance(menu_region, main_region, lambda state: state.has(ItemName.Map_Wanted, self.player))

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Wanted_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Wanted_MainEE, ee_locs)
            self.multiworld.regions.append(main_ee_region)
            create_entrance(
                main_region, 
                main_ee_region, 
                lambda state: (
                    state.has(ItemName.Progressive_PackAPunch, self.player) and
                    (state.has_group_unique(Items.BO3ZombiesItemCategory.REGULAR_WEAPON, self.player, self.mystery_box_regular_items_two_third) if self.options.mystery_box_regular_items else True) and
                    state.has_all({item.name for item in Items.Wanted_Shield}, self.player)
                    # (state.has_all({item.name for item in Items.Revelations_MysteryBox}, self.player) if self.options.mystery_box_special_items else True)
                )
            )


    def create_region(self, world: MultiWorld, player: int, name: str, locations=None):
        ret = Region(name, player, world)
        if locations:
            for location in locations:
                location = BO3ZombiesLocation(player, location, self.location_name_to_id[location], ret)
                ret.locations.append(location)

        return ret

    def create_item(self, name: str) -> Item:
        data = self.item_name_to_id[name]

        useful_categories = {
            Items.BO3ZombiesItemCategory.WALLBUY,
            Items.BO3ZombiesItemCategory.MACHINE,
            Items.BO3ZombiesItemCategory.SPECIAL_WEAPON,
            Items.BO3ZombiesItemCategory.CRAFTABLE,
            Items.BO3ZombiesItemCategory.MAP_UNLOCK,
            Items.BO3ZombiesItemCategory.SHOP_ITEMS,
        }

        # TODO: do a getProgressiveItems list instead
        progression_categories = {
            Items.BO3ZombiesItemCategory.MACHINE,
            Items.BO3ZombiesItemCategory.PROGRESSIVE,
            Items.BO3ZombiesItemCategory.REGULAR_WEAPON,
            Items.BO3ZombiesItemCategory.SPECIAL_WEAPON,
            Items.BO3ZombiesItemCategory.CRAFTABLE,
            Items.BO3ZombiesItemCategory.BLOCKER,
            Items.BO3ZombiesItemCategory.POWER,
            Items.BO3ZombiesItemCategory.EASTER_EGG,
            Items.BO3ZombiesItemCategory.VICTORY,
            Items.BO3ZombiesItemCategory.MAP_UNLOCK,
        }

        if Items.all_items_dict[name].category in progression_categories:
            item_classification = ItemClassification.progression
        elif Items.all_items_dict[name].category in useful_categories:
            item_classification = ItemClassification.useful
        elif Items.all_items_dict[name].category == Items.BO3ZombiesItemCategory.TRAP:
            item_classification = ItemClassification.trap
        else:
            item_classification = ItemClassification.filler

        return Items.BO3ZombiesItem(name, item_classification, data, self.player)

    def create_filler_gift(self) -> Item:
        if not hasattr(self, '_gift_bag') or not self._gift_bag:
            self._gift_bag = list(Items.Gift_Items)
            self.random.shuffle(self._gift_bag)

        gift = self._gift_bag.pop()
        return self.create_item(gift[0])
    
    def create_filler_trap(self) -> Item:
        if not hasattr(self, '_trap_bag') or not self._trap_bag:
            self._trap_bag = list(Items.Trap_Items)
            self.random.shuffle(self._trap_bag)

        gift = self._trap_bag.pop()
        return self.create_item(gift[0])

    def create_filler(self) -> Item:
        # TODO make a proper filler item
        return self.create_item(ItemName.Points200)

    def create_items(self) -> None:
        print("items")
        enabled_items = [
            Items.Points_1500,
            Items.Points_1500,
        ]

        # Add locked map items
        enabled_items += list(map(self.create_item, self.cod_locked_maps))

        # Add progressive starting items
        if self.options.progressive_starting_points > 0:
            num_items = math.floor(self.options.progressive_starting_points / 500)
            for i in range(num_items):
                enabled_items.append(Items.Progressive_StartingPoints500)

        # 2 Progressive Pap items (turn on + alternate ammo types)
        enabled_items.extend([Items.Progressive_PackAPunch, Items.Progressive_PackAPunch])

        # Add progressive perk limits to pool
        if self.options.progressive_perk_limit_increase > 0:
            for i in range(self.options.progressive_perk_limit_increase):
                enabled_items += [Items.Progressive_PerkLimitIncrease]

        # Add shop items
        if self.options.shop_perk_tokens > 0:
            for i in range(self.options.shop_perk_tokens):
                enabled_items.append(Items.Shop_Items[0])
        if self.options.shop_mega_gums > 0:
            for i in range(self.options.shop_mega_gums):
                enabled_items.append(Items.Shop_Items[1])
        if self.options.shop_rare_gums > 0:
            for i in range(self.options.shop_rare_gums):
                enabled_items.append(Items.Shop_Items[2])
        if self.options.shop_legendary_gums > 0:
            for i in range(self.options.shop_legendary_gums):
                enabled_items.append(Items.Shop_Items[3])

        # Add machines to pool
        if self.options.map_specific_machines:
            # Add map specific machines for each
            if self.options.map_shadows_enabled:
                enabled_items += Items.Shadows_Machines_Specific
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_Machines_Specific
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_Machines_Specific
            if self.options.map_zetsubou_enabled:
                enabled_items += Items.Zetsubou_Machines_Specific
            if self.options.map_gorod_enabled:
                enabled_items += Items.GorodKrovi_Machines_Specific
            if self.options.map_revelations_enabled:
                enabled_items += Items.Revelations_Machines_Specific
            if self.options.map_workshop_wanted_enabled:
                enabled_items += Items.Wanted_Machines_Specific
        else:
            # Only add one instance per machine
            seen = set()
            if self.options.map_shadows_enabled:
                add_universal_items(enabled_items, seen, Items.Shadows_Machines)
            if self.options.map_the_giant_enabled:
                add_universal_items(enabled_items, seen, Items.The_Giant_Machines)
            if self.options.map_castle_enabled:
                add_universal_items(enabled_items, seen, Items.Castle_Machines)
            if self.options.map_zetsubou_enabled:
                add_universal_items(enabled_items, seen, Items.Zetsubou_Machines)
            if self.options.map_gorod_enabled:
                add_universal_items(enabled_items, seen, Items.GorodKrovi_Machines)
            if self.options.map_revelations_enabled:
                add_universal_items(enabled_items, seen, Items.Revelations_Machines)
            if self.options.map_workshop_wanted_enabled:
                add_universal_items(enabled_items, seen, Items.Wanted_Machines)

        # Add wallbuys to pool
        if self.options.map_specific_wallbuys:
            # Add map specific wallbuys for each
            if self.options.map_shadows_enabled:
                enabled_items += Items.Shadows_Wallbuys_Specific
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_Wallbuys_Specific
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_Wallbuys_Specific
            if self.options.map_zetsubou_enabled:
                enabled_items += Items.Zetsubou_Wallbuys_Specific
            if self.options.map_gorod_enabled:
                enabled_items += Items.GorodKrovi_Wallbuys_Specific
            if self.options.map_revelations_enabled:
                enabled_items += Items.Revelations_Wallbuys_Specific
        else:
            # Only add one instance per wallbuy
            seen = set()
            if self.options.map_shadows_enabled:
                add_universal_items(enabled_items, seen, Items.Shadows_Wallbuys)
            if self.options.map_the_giant_enabled:
                add_universal_items(enabled_items, seen, Items.The_Giant_Wallbuys)
            if self.options.map_castle_enabled:
                add_universal_items(enabled_items, seen, Items.Castle_Wallbuys)
            if self.options.map_zetsubou_enabled:
                add_universal_items(enabled_items, seen, Items.Zetsubou_Wallbuys)
            if self.options.map_gorod_enabled:
                add_universal_items(enabled_items, seen, Items.GorodKrovi_Wallbuys)
            if self.options.map_revelations_enabled:
                add_universal_items(enabled_items, seen, Items.Revelations_Wallbuys)

        # Modded maps without universal wallbuys
        if self.options.map_workshop_wanted_enabled:
            enabled_items += Items.Wanted_Wallbuys

        map_list = []
        if self.options.map_shadows_enabled:
            map_list.append((Maps.Shadows_Map_String, RegionName.Shadows_Alleyway, RegionName.Shadows_Round_Regions, Locations.Shadows_Round_Locations))
            if self.options.randomized_shield_parts:
                enabled_items += Items.Shadows_Shield
            else:
                self.multiworld.get_location(LocationName.Shadows_Craftable_ShieldPartDoor, self.player).place_locked_item(self.create_item(Items.Shadows_Shield[0].name))
                self.multiworld.get_location(LocationName.Shadows_Craftable_ShieldPartDolly, self.player).place_locked_item(self.create_item(Items.Shadows_Shield[1].name))
                self.multiworld.get_location(LocationName.Shadows_Craftable_ShieldPartClamp, self.player).place_locked_item(self.create_item(Items.Shadows_Shield[2].name))
            enabled_items += Items.Shadows_Craftables
        if self.options.map_the_giant_enabled:
            map_list.append((Maps.The_Giant_Map_String, RegionName.TheGiant_Courtyard, RegionName.TheGiant_Round_Regions, Locations.TheGiant_Round_Locations))
        if self.options.map_castle_enabled:
            map_list.append((Maps.Castle_Map_String, RegionName.Castle_Gondola, RegionName.Castle_Round_Regions, Locations.Castle_Round_Locations))
            if self.options.randomized_shield_parts:
                enabled_items += Items.Castle_Shield
            else:
                self.multiworld.get_location(LocationName.Castle_Craftable_ShieldPartDoor, self.player).place_locked_item(self.create_item(Items.Castle_Shield[0].name))
                self.multiworld.get_location(LocationName.Castle_Craftable_ShieldPartDolly, self.player).place_locked_item(self.create_item(Items.Castle_Shield[1].name))
                self.multiworld.get_location(LocationName.Castle_Craftable_ShieldPartClamp, self.player).place_locked_item(self.create_item(Items.Castle_Shield[2].name))
            enabled_items += Items.Castle_Craftables
        if self.options.map_zetsubou_enabled:
            map_list.append((Maps.Zetsubou_Map_String, RegionName.Zetsubou_Beach, RegionName.Zetsubou_Round_Regions, Locations.Zetsubou_Round_Locations))
            if self.options.randomized_shield_parts:
                enabled_items += Items.Zetsubou_Shield
            else:
                self.multiworld.get_location(LocationName.Zetsubou_Craftable_ShieldPartDoor, self.player).place_locked_item(self.create_item(Items.Zetsubou_Shield[0].name))
                self.multiworld.get_location(LocationName.Zetsubou_Craftable_ShieldPartDolly, self.player).place_locked_item(self.create_item(Items.Zetsubou_Shield[1].name))
                self.multiworld.get_location(LocationName.Zetsubou_Craftable_ShieldPartClamp, self.player).place_locked_item(self.create_item(Items.Zetsubou_Shield[2].name))
            enabled_items += Items.Zetsubou_Craftables_Gasmask
        if self.options.map_gorod_enabled:
            map_list.append((Maps.GorodKrovi_Map_String, RegionName.Gorod_Trenches, RegionName.Gorod_Round_Regions, Locations.GorodKrovi_Round_Locations))
            if self.options.randomized_shield_parts:
                enabled_items += Items.GorodKrovi_Shield
            else:
                self.multiworld.get_location(LocationName.GorodKrovi_Craftable_ShieldPartDoor, self.player).place_locked_item(self.create_item(Items.GorodKrovi_Shield[0].name))
                self.multiworld.get_location(LocationName.GorodKrovi_Craftable_ShieldPartDolly, self.player).place_locked_item(self.create_item(Items.GorodKrovi_Shield[1].name))
                self.multiworld.get_location(LocationName.GorodKrovi_Craftable_ShieldPartClamp, self.player).place_locked_item(self.create_item(Items.GorodKrovi_Shield[2].name))
            # if self.options.randomized_gorod_dragonride_parts:
            #     enabled_items += Items.GorodKrovi_Craftables_Dragonride
            # else:
            #     self.multiworld.get_location(LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Transmitter, self.player).place_locked_item(self.create_item(ItemName.GorodKrovi_Craftable_Dragonride_Transmitter))
            #     self.multiworld.get_location(LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Codes, self.player).place_locked_item(self.create_item(ItemName.GorodKrovi_Craftable_Dragonride_Codes))
            #     self.multiworld.get_location(LocationName.GorodKrovi_Quest_MainQuest_Dragonride_Map, self.player).place_locked_item(self.create_item(ItemName.GorodKrovi_Craftable_Dragonride_Map))
        if self.options.map_revelations_enabled:
            map_list.append((Maps.Revelations_Map_String, RegionName.Revelations_House, RegionName.Revelations_Round_Regions, Locations.Revelations_Round_Locations))
            if self.options.randomized_shield_parts:
                enabled_items += Items.Revelations_Shield
            else:
                self.multiworld.get_location(LocationName.Revelations_Craftable_ShieldPartDoor, self.player).place_locked_item(self.create_item(Items.Revelations_Shield[0].name))
                self.multiworld.get_location(LocationName.Revelations_Craftable_ShieldPartDolly, self.player).place_locked_item(self.create_item(Items.Revelations_Shield[1].name))
                self.multiworld.get_location(LocationName.Revelations_Craftable_ShieldPartClamp, self.player).place_locked_item(self.create_item(Items.Revelations_Shield[2].name))
        if self.options.map_workshop_wanted_enabled:
            map_list.append((Maps.Wanted_Map_String, RegionName.Wanted_Town, RegionName.Wanted_Round_Regions, Locations.Wanted_Round_Locations))
            if self.options.randomized_shield_parts:
                enabled_items += Items.Wanted_Shield
            else:
                self.multiworld.get_location(LocationName.Wanted_Craftable_ShieldPartDoor, self.player).place_locked_item(self.create_item(Items.Wanted_Shield[0].name))
                self.multiworld.get_location(LocationName.Wanted_Craftable_ShieldPartDolly, self.player).place_locked_item(self.create_item(Items.Wanted_Shield[1].name))
                self.multiworld.get_location(LocationName.Wanted_Craftable_ShieldPartClamp, self.player).place_locked_item(self.create_item(Items.Wanted_Shield[2].name))
            enabled_items += Items.Wanted_Craftable_Acidgat

        enabled_items += self.mystery_box_special_items
        enabled_items += self.mystery_box_regular_items

        # Easter Egg Hunt
        if self.options.goal_condition == 0:
            # Get list of compatible enabled maps
            ee_pairs = []
            if self.options.map_shadows_enabled:
                ee_pairs.append((LocationName.Shadows_Quest_MainEE_Victory, Maps.Shadows_Map_String + ItemName.EE_Victory))
            if self.options.map_castle_enabled:
                ee_pairs.append((LocationName.Castle_Quest_MainEE_Victory, Maps.Castle_Map_String + ItemName.EE_Victory))
            if self.options.map_zetsubou_enabled:
                ee_pairs.append((LocationName.Zetsubou_Quest_MainEE_Victory, Maps.Zetsubou_Map_String + ItemName.EE_Victory))
            if self.options.map_gorod_enabled:
                ee_pairs.append((LocationName.GorodKrovi_Quest_MainEE_Victory, Maps.GorodKrovi_Map_String + ItemName.EE_Victory))
            if self.options.map_revelations_enabled:
                ee_pairs.append((LocationName.Revelations_Quest_MainEE_Victory, Maps.Revelations_Map_String + ItemName.EE_Victory))
            if self.options.map_workshop_wanted_enabled:
                ee_pairs.append((LocationName.Wanted_Quest_MainEE_Victory, Maps.Wanted_Map_String + ItemName.EE_Victory))

            if len(ee_pairs) == 0:
                ee_pairs.append((LocationName.TheGiant_Quest_FlyTrap, Maps.The_Giant_Map_String + ItemName.EE_Victory))

            # Get bounds for number of victory items to add
            ee_allow_any = not self.options.goal_ee_random
            ee_count = min(self.options.goal_ee_count.value, len(ee_pairs))
            self.ee_goal_items = []

            # Preselect the list of required maps, if random selection is enabled
            if not ee_allow_any:
                ee_pairs = self.random.sample(ee_pairs, ee_count)

            # Fill victory items at their victory locations
            for pair in ee_pairs:
                item = self.create_item(pair[1])
                self.multiworld.get_location(pair[0], self.player).place_locked_item(item)
                self.ee_goal_items.append(pair[1])

        # Weapon Quest
        if self.options.goal_condition == 1:
            if self.options.map_shadows_enabled:
                goal_items = list(map(self.create_item, [
                    ItemName.Shadows_Victory_ApothiconSwordLvl2,
                    ItemName.Shadows_Victory_Upgraded_LilArnies,
                    ItemName.Shadows_Victory_Upgraded_DoughnutMines,
                ]))
                self.weapon_quest_items.extend([item.name for item in goal_items])
                self.multiworld.get_location(LocationName.Shadows_Quest_ApothiconSword_CollectUpgradedSword, self.player).place_locked_item(goal_items[0]) 
                self.multiworld.get_location(LocationName.Shadows_Quest_LilArnies_Upgrade, self.player).place_locked_item(goal_items[1])
                self.multiworld.get_location(LocationName.Shadows_Quest_DoughnutMines, self.player).place_locked_item(goal_items[2])

            if self.options.map_castle_enabled:
                # Handled in create_regions
                pass
            
            if self.options.map_zetsubou_enabled:
                goal_items = list(map(self.create_item, [
                    ItemName.Zetsubou_Victory_Masamune,
                    ItemName.Zetsubou_Victory_Skull,
                ]))
                self.weapon_quest_items.extend([item.name for item in goal_items])
                self.multiworld.get_location(Locations.Zetsubou_Quest_Masamune_Locations[-1].name, self.player).place_locked_item(goal_items[0])
                self.multiworld.get_location(Locations.Zetsubou_Quest_Skull_Locations[-1].name, self.player).place_locked_item(goal_items[1])
            
            if self.options.map_gorod_enabled:
                goal_items = list(map(self.create_item, [
                    ItemName.GorodKrovi_Victory_DragonGauntlets,
                    ItemName.GorodKrovi_Victory_Upgraded_Dragonstrikes,
                    ItemName.GorodKrovi_Victory_Upgraded_MonkeyBombs,
                    ItemName.GorodKrovi_Victory_TiamatsMaw
                ]))
                self.weapon_quest_items.extend([item.name for item in goal_items])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_DragonGauntlets_Late[-1].name, self.player).place_locked_item(goal_items[0])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_DragonStrikes_Upgraded[-1].name, self.player).place_locked_item(goal_items[1])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_Challenges[3].name, self.player).place_locked_item(goal_items[2])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_TiamatsMaw[-1].name, self.player).place_locked_item(goal_items[3])

            if self.options.map_workshop_wanted_enabled:
                goal_items = list(map(self.create_item, [
                    ItemName.Wanted_Victory_Magmagat,
                    ItemName.Wanted_Victory_GreatScott,
                ]))
                self.weapon_quest_items.extend([item.name for item in goal_items])
                self.multiworld.get_location(Locations.Wanted_Quest_Weapons[0].name, self.player).place_locked_item(goal_items[0])
                self.multiworld.get_location(Locations.Wanted_Quest_Weapons[1].name, self.player).place_locked_item(goal_items[1])

        is_goal_cond = self.options.goal_condition == 2

        base_locations_left = len(self.multiworld.get_unfilled_locations(self.player))
        # Account for locked goal rounds
        if self.options.goal_condition == 2:
            base_locations_left -= len(map_list)
        locations_left = base_locations_left + self.calc_round_locations(len(map_list), is_goal_cond)

        if len(enabled_items) > locations_left:
            print(f"Black Ops 3 - Zombies: (Player {self.player}) Too few locations, increasing round frequency and maximum")

        # Adjust round freq downwards to try and generate enough locations
        while self.options.round_location_freq.value > 1 and len(enabled_items) > locations_left:
            self.options.round_location_freq.value -= 1
            locations_left = base_locations_left + self.calc_round_locations(len(map_list), is_goal_cond)

        # Still not enough locations, adjust max round
        while self.options.round_location_max.value < 99 and len(enabled_items) > locations_left :
            self.options.round_location_max.value += 1
            if self.options.goal_round.value <= self.options.round_location_max.value:
                self.options.goal_round.value = self.options.round_location_max.value + 1
            if self.options.round_location_max.value > self.options.goal_round.value:
                self.options.goal_round.value = self.options.round_location_max.value
            locations_left = base_locations_left + self.calc_round_locations(len(map_list), is_goal_cond)

        # Add round locations
        round_max = self.options.round_location_max.value
        goal_round = self.options.goal_round.value
        #if is_goal_cond:
            #round_max = min(round_max, goal_round)

        for str_map, str_main_region, list_round_regions, round_locations in map_list:
            round_locs = add_round_locations(round_locations, round_max, self.options.round_location_freq.value, is_goal_cond, goal_round)
            main_region = self.multiworld.get_region(str_main_region, self.player)
            for location_name in round_locs[0]:
                location = BO3ZombiesLocation(self.player, location_name, self.location_name_to_id[location_name], main_region)
                main_region.locations.append(location)
            for region in range(len(list_round_regions)):
                # (Starting Region, Region Being connected, Locations corresponding to region)
                self.add_round_region(main_region, list_round_regions[region], round_locs[region+1])

        # Goal Round Condition
        if self.options.goal_condition == 2:
            self.goal_round_items = []
            for m in map_list:
                # Victory round item on every map
                goal_location = Locations.get_map_victory_location(m[0], self.options.goal_round)
                goal_item = self.create_item(m[0] + " Victory")
                self.goal_round_items.append(m[0] + " Victory")
                self.multiworld.get_location(goal_location, self.player).place_locked_item(goal_item)

        locations_left = len(self.multiworld.get_unfilled_locations(self.player))

        for item_data in enabled_items:
            self.multiworld.itempool.append(self.create_item(item_data.name))
            locations_left -= 1

        if locations_left > 0:
            gift_filler_weight = self.options.gift_weight / 100
            trap_filler_weight = self.options.trap_weight / 100
            total_weight = gift_filler_weight + trap_filler_weight
            if total_weight > 1:
                gift_filler_weight *= 1 / total_weight
                trap_filler_weight *= 1 / total_weight
            trap_filler_count = math.floor(locations_left * trap_filler_weight)
            gift_filler_count = math.floor(locations_left * gift_filler_weight)
            filler_count = locations_left - (gift_filler_count + trap_filler_count)

            # Creates filler in remaining slots
            self.multiworld.itempool.extend([self.create_filler_trap() for _ in range(trap_filler_count)])
            self.multiworld.itempool.extend([self.create_filler_gift() for _ in range(gift_filler_count)])
            self.multiworld.itempool.extend([self.create_filler() for _ in range(filler_count)])

    def calc_round_locations(self, num_maps, is_goal_cond) -> int:
        round_freq = self.options.round_location_freq.value
        round_max = self.options.round_location_max.value
        if is_goal_cond:
            round_max = min(round_max, self.options.goal_round.value)
        goal_round = self.options.goal_round.value
        
        if round_freq == 0:
            return 0
        
        count = 0
        i = round_freq
        
        # Match the logic in add_round_locations
        while i <= round_max:
            # Skip round 1
            if i != 1:
                count += 1
            i += round_freq
        
        # Account for goal round being added separately if not already included
        if is_goal_cond and goal_round is not None:
            if goal_round > round_max or goal_round % round_freq != 0:
                count += 1
        
        return count * num_maps

    def generate_basic(self) -> None:
        # for debugging purposes, you may want to visualize the layout of your world. Uncomment the following code to
        # write a PlantUML diagram to the file "my_world.puml" that can help you see whether your regions and locations
        # are connected and placed as desired
        #from Utils import visualize_regions
        #visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
        pass

    def set_rules(self) -> None:
        self.slot_goal_items_required = 0
        self.slot_goal_items = []
        # Goal Conditions

        # Easter Egg Hunt
        if self.options.goal_condition == 0:
            self.slot_goal_items = self.ee_goal_items
            # Whether or not we require *all* selected goal items (Randomised goal selection)
            ee_allow_any = not self.options.goal_ee_random
            if not ee_allow_any:
                self.slot_goal_items_required = len(self.slot_goal_items)
                self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.ee_goal_items, self.player)
            else:
                self.slot_goal_items_required = self.options.goal_ee_count.value
                self.multiworld.completion_condition[self.player] = lambda state: state.has_from_list(self.ee_goal_items, self.player, min(self.options.goal_ee_count.value, len(self.ee_goal_items))) 
            
        # Weapon Quest
        if self.options.goal_condition == 1:
            self.slot_goal_items = self.weapon_quest_items
            self.slot_goal_items_required = len(self.slot_goal_items)
            self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.weapon_quest_items, self.player)

        # Goal Round
        if self.options.goal_condition == 2:
            self.slot_goal_items = self.goal_round_items
            self.slot_goal_items_required = self.options.goal_round_count.value
            self.multiworld.completion_condition[self.player] = lambda state: state.has_from_list(self.goal_round_items, self.player, min(self.options.goal_round_count.value, len(self.goal_round_items)))

    def fill_slot_data(self) -> dict:
        options = self.options
        
        slot_data = {
            'seed': "".join(
                self.random.choice(string.ascii_letters) for _ in range(16)),
            'base_id': str(self.base_id),
            "slot": self.multiworld.player_name[self.player],
            "map_specific_machines": bool(options.map_specific_machines),
            "map_specific_wallbuys": bool(options.map_specific_wallbuys),
            "special_rounds_enabled": bool(options.special_rounds_enabled),
            "perk_limit_default_modifier": int(options.perk_limit_default_modifier),
            "mystery_box_special_items": bool(options.mystery_box_special_items),
            "mystery_box_regular_items": bool(options.mystery_box_regular_items),
            "difficulty_gorod_egg_cooldown": bool(options.difficulty_gorod_egg_cooldown),
            "difficulty_gorod_dragon_wings": bool(options.difficulty_gorod_dragon_wings),
            "difficulty_ee_checkpoints": options.difficulty_ee_checkpoints.value,
            "difficulty_round_checkpoints": options.difficulty_round_checkpoints.value,
            "rolled_bows": self.rolled_bows,
            "attachments_randomized": bool(options.attachments_randomized),
            "attachments_sight_weight": int(options.attachments_sight_weight),
            "camo_randomized": bool(options.camo_randomized),
            "camo_mixed": bool(options.camo_mixed),
            "camo_pap_randomized": bool(options.camo_pap_randomized),
            "camo_pap_mixed": bool(options.camo_pap_mixed),
            "camo_joined": bool(options.camo_joined),
            "reticle_randomized": bool(options.reticle_randomized),
            "reticle_pap_randomized": bool(options.reticle_pap_randomized),
            "reticle_joined": bool(options.reticle_joined),
            "deathlink_enabled": bool(options.deathlink_enabled),
            "deathlink_send_mode": int(options.deathlink_send_mode),
            "deathlink_recv_mode": int(options.deathlink_recv_mode),
            "goal_items_required": int(self.slot_goal_items_required),
            "goal_items": self.slot_goal_items,
        }

        return slot_data

    def add_round_region(self, main_region, new_region_name, round_locs):
        round_num = new_region_name[-2:]
        # Get the round number from the location name
        if round_num == "00":  # if the last two characters in the string are 00 we know it's really round 100
            round_num = 100
        else:
            round_num = int(round_num)
        # This gets the map name from our location name
        map_name = new_region_name.split(")")[0] + ")"
        region = self.create_region(self.multiworld, self.player, new_region_name, round_locs)
        self.multiworld.regions.append(region)
        rule: CollectionRule = lambda state: rules.check_round_logic(state, self.player, self.options, round_num, map_name, self.mystery_box_regular_items_third, self.mystery_box_regular_items_two_third)
        create_entrance(main_region, region, rule)

def add_universal_items(enabled_items, seen, items):
    for item in items:
        if item[0] not in seen:
            enabled_items.append(item)
            seen.add(item[0])

def add_round_locations(round_locations, round_max, round_freq, is_goal_cond, goal_round):
    round_locs_early = []
    round_locs_10 = []
    round_locs_15 = []
    round_locs_20 = []
    round_locs_25 = []
    round_locs_30 = []
    round_locs_35 = []
    round_locs_40 = []

    if round_freq > 0:
        i = round_freq
        # Add rounds into pool
        while i <= round_max:
            # Never assign to round 1
            if i == 1:
                i += round_freq
                continue
            elif i <= 5:
                round_locs_early.append(round_locations[i - 2].name)
            elif i <= 10:
                round_locs_10.append(round_locations[i - 2].name)
            elif i <= 15:
                round_locs_15.append(round_locations[i - 2].name)
            elif i <= 20:
                round_locs_20.append(round_locations[i - 2].name)
            elif i <= 25:
                round_locs_25.append(round_locations[i - 2].name)
            elif i <= 30:
                round_locs_30.append(round_locations[i - 2].name)
            elif i <= 35:
                round_locs_35.append(round_locations[i - 2].name)
            else:
                round_locs_40.append(round_locations[i - 2].name)
            i += round_freq
        # Make sure the Goal Round is always included
        if is_goal_cond:
            if goal_round > round_max or goal_round % round_freq != 0:
                if goal_round <= 5:
                    round_locs_early.append(round_locations[goal_round - 2].name)
                elif goal_round <= 10:
                    round_locs_10.append(round_locations[goal_round - 2].name)
                elif goal_round <= 15:
                    round_locs_15.append(round_locations[goal_round - 2].name)
                elif goal_round <= 20:
                    round_locs_20.append(round_locations[goal_round - 2].name)
                elif goal_round <= 25:
                    round_locs_25.append(round_locations[goal_round - 2].name)
                elif goal_round <= 30:
                    round_locs_30.append(round_locations[goal_round - 2].name)
                elif goal_round <= 35:
                    round_locs_35.append(round_locations[goal_round - 2].name)
                else:
                    round_locs_40.append(round_locations[goal_round - 2].name)
    return [round_locs_early, round_locs_10, round_locs_15, round_locs_20, round_locs_25, round_locs_30, round_locs_35, round_locs_40]

# REMOVE IN 0.6.7
def create_entrance(from_region: Region, to_region: Region, rule: CollectionRule | None = None):
    from_region.connect(to_region, None, rule)