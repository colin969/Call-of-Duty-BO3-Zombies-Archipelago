import string
import math
import random

from BaseClasses import MultiWorld, Region, Item, ItemClassification, Tutorial

from worlds.AutoWorld import World, WebWorld

from worlds.generic.Rules import set_rule

from . import Regions, Locations, Items, Options
from .Options import BO3ZombiesOptions, bo3_option_groups
from .Names import ItemName, LocationName, RegionName, Maps

class BO3ZombiesWeb(WebWorld):
    theme = "ocean"
    option_groups = bo3_option_groups

class BO3ZombiesWorld(World):
    """
    TODO: Game Description
    """
    game: str = "Black Ops 3 - Zombies"
    web = BO3ZombiesWeb()

    options_dataclass = BO3ZombiesOptions
    options = BO3ZombiesOptions

    required_client_version = (0, 6, 5)

    topology_present = True
    # Game's SteamID
    base_id = 311210
    item_name_to_id = Items.BO3ZombiesItem.get_name_to_id(base_id)
    location_name_to_id = Locations.BO3ZombiesLocation.get_name_to_id(base_id)

    # Full Remote Items
    items_handling = 0b111

    def generate_early(self) -> None:
        self.weapon_quest_items = []
        pass

    def create_regions(self):
        universal_locations = [
            LocationName.RepairWindows_5
        ]
        menu_region = self.create_region(self.multiworld, self.player, 'Menu', universal_locations)
        
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
            add_round_locations(all_locations, Locations.Shadows_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.Shadows_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_ApothiconSword_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_MainEE_Locations])
            main_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_Alleyway, all_locations)
            self.multiworld.regions.append(main_region)
            menu_region.connect(main_region)

        if self.options.map_the_giant_enabled:
            all_locations = []
            add_round_locations(all_locations, Locations.TheGiant_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            main_region = self.create_region(self.multiworld, self.player, RegionName.TheGiant_Courtyard, all_locations)
            self.multiworld.regions.append(main_region)
            menu_region.connect(main_region)

        if self.options.map_castle_enabled:
            all_locations = []

            bow_pairs = [
                (Locations.Castle_Quest_ElementalBow_Storm_Locations, self.create_item(ItemName.Castle_Victory_ElementalBow_Storm)),
                (Locations.Castle_Quest_ElementalBow_Wolf_Locations, self.create_item(ItemName.Castle_Victory_ElementalBow_Wolf)),
                (Locations.Castle_Quest_ElementalBow_Fire_Locations, self.create_item(ItemName.Castle_Victory_ElementalBow_Fire)),
                (Locations.Castle_Quest_ElementalBow_Void_Locations, self.create_item(ItemName.Castle_Victory_ElementalBow_Void)),
            ]
            bow_count = min(self.options.castle_bow_count, 4)
            bow_pairs = self.random.sample(bow_pairs, bow_count)
            for bow in bow_pairs:
                all_locations.extend([loc.name for loc in bow[0]])
                self.weapon_quest_items.append(bow[1].name)

            add_round_locations(all_locations, Locations.Castle_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.Castle_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Castle_Quest_Locations])
            all_locations.extend([loc.name for loc in Locations.Castle_Quest_MainEE_Locations[:4]]) # Up to Boss Fight start
            all_locations.extend([loc.name for loc in Locations.Castle_Quest_Music_Locations])

            main_region = self.create_region(self.multiworld, self.player, RegionName.Castle_Gondola, all_locations)
            self.multiworld.regions.append(main_region)

            # Weapon Quest - Add available bows
            if self.options.goal_condition == 1:
                for bow in bow_pairs:
                    self.multiworld.get_location(bow[0][-1].name, self.player).place_locked_item(bow[1])



            boss_fight_locations = [loc.name for loc in Locations.Castle_Quest_MainEE_Locations[4:]]
            boss_region = self.create_region(self.multiworld, self.player, RegionName.Castle_BossFight, boss_fight_locations)
            self.multiworld.regions.append(boss_region)

            menu_region.connect(main_region)            
            main_region.connect(boss_region, lambda state: state.has(ItemName.Castle_Craftable_GravitySpikes_Body, self.player) and
                state.has(ItemName.Castle_Craftable_GravitySpikes_Guards, self.player) and
                state.has(ItemName.Castle_Craftable_GravitySpikes_Handle, self.player))

            print(self.multiworld.regions)

    def create_region(self, world: MultiWorld, player: int, name: str, locations=None):
        ret = Region(name, player, world)
        if locations:
            for location in locations:
                location = Locations.BO3ZombiesLocation(player, location, self.location_name_to_id[location], ret)
                ret.locations.append(location)

        return ret

    def create_item(self, name: str) -> Item:
        data = self.item_name_to_id[name]

        useful_categories = {
            Items.BO3ZombiesItemCategory.WALLBUY,
            Items.BO3ZombiesItemCategory.MACHINE,
            Items.BO3ZombiesItemCategory.PROGRESSIVE,
        }

        # TODO: do a getProgressiveItems list instead
        progression_categories = {
            Items.BO3ZombiesItemCategory.BLOCKER,
            Items.BO3ZombiesItemCategory.POWER,
            Items.BO3ZombiesItemCategory.EASTER_EGG,
            Items.BO3ZombiesItemCategory.VICTORY
        }

        if Items.all_items_dict[name].category in progression_categories:
            item_classification = ItemClassification.progression
        elif Items.all_items_dict[name].category in useful_categories:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler

        return Items.BO3ZombiesItem(name, item_classification, data, self.player)

    def create_filler_gift(self) -> Item:
        gift = random.choice(Items.Gift_Items)
        return self.create_item(gift[0])

    def create_filler(self) -> Item:
        # TODO make a proper filler item
        return self.create_item(ItemName.Points50)

    def create_items(self) -> None:
        enabled_items = Items.base_items
        enabled_items.append(Items.PapItem)

        # Add progressives to pool
        if self.options.progressive_perk_limit_increase > 0:
            for i in range(self.options.progressive_perk_limit_increase):
                enabled_items += [Items.Progressive_PerkLimitIncrease]

        # Add machines to pool
        if self.options.map_specific_machines:
            # Add map specific machines for each
            if self.options.map_shadows_enabled:
                enabled_items += Items.Shadows_Machines_Specific
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_Machines_Specific
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_Machines_Specific
        else:
            # Only add one instance per machine
            seen = set()
            if self.options.map_shadows_enabled:
                add_universal_items(enabled_items, seen, Items.Shadows_Machines)
            if self.options.map_the_giant_enabled:
                add_universal_items(enabled_items, seen, Items.The_Giant_Machines)
            if self.options.map_castle_enabled:
                add_universal_items(enabled_items, seen, Items.Castle_Machines)

        # Add wallbuys to pool
        if self.options.map_specific_wallbuys:
            # Add map specific wallbuys for each
            if self.options.map_shadows_enabled:
                enabled_items += Items.Shadows_Wallbuys_Specific
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_Wallbuys_Specific
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_Wallbuys_Specific
        else:
            # Only add one instance per wallbuy
            seen = set()
            if self.options.map_shadows_enabled:
                add_universal_items(enabled_items, seen, Items.Shadows_Wallbuys)
            if self.options.map_the_giant_enabled:
                add_universal_items(enabled_items, seen, Items.The_Giant_Wallbuys)
            if self.options.map_castle_enabled:
                add_universal_items(enabled_items, seen, Items.Castle_Wallbuys)

        map_list = []
        if self.options.map_shadows_enabled:
            map_list.append(Maps.Shadows_Map_String)
            if self.options.randomized_shield_parts:
                enabled_items += Items.Shadows_Shield
            enabled_items += Items.Shadows_Craftables
        if self.options.map_the_giant_enabled:
            map_list.append(Maps.The_Giant_Map_String)
        if self.options.map_castle_enabled:
            map_list.append(Maps.Castle_Map_String)
            if self.options.randomized_shield_parts:
                enabled_items += Items.Castle_Shield
            enabled_items += Items.Castle_Craftables

        # Easter Egg Hunt
        if self.options.goal_condition == 0:
            # Get list of compatible enabled maps
            ee_pairs = []
            if self.options.map_shadows_enabled:
                ee_pairs.append((LocationName.Shadows_Quest_MainEE_Victory, Maps.Shadows_Map_String + ItemName.EE_Victory))
            if self.options.map_castle_enabled:
                ee_pairs.append((LocationName.Castle_Quest_MainEE_Victory, Maps.Castle_Map_String + ItemName.EE_Victory))

            # Get bounds for number of victory items to add
            ee_allow_any = not self.options.goal_ee_random
            ee_count = min(self.options.goal_ee_count, len(ee_pairs))
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
                goal_item = self.create_item(ItemName.Shadows_Victory_ApothiconSwordLvl2)
                self.weapon_quest_items.append(ItemName.Shadows_Victory_ApothiconSwordLvl2)
                self.multiworld.get_location(Locations.Shadows_Quest_ApothiconSword_Locations[-1].name, self.player).place_locked_item(goal_item)
            if self.options.map_castle_enabled:
                # Handled in create_regions
                pass

        # Goal Round Condition
        if self.options.goal_condition == 2:
            self.goal_round_items = []
            for m in map_list:
                # Victory round item on every map
                goal_location = Locations.get_map_victory_location(m, self.options.goal_round)
                goal_item = self.create_item(m + " Victory")
                self.goal_round_items.append(m + " Victory")
                self.multiworld.get_location(goal_location, self.player).place_locked_item(goal_item)

        locations_left = len(self.multiworld.get_unfilled_locations(self.player))

        for item_data in enabled_items:
            self.multiworld.itempool.append(self.create_item(item_data.name))
            locations_left -= 1

        print("Unfilled after item allocation: " + str(locations_left))

        gift_filler_weight = self.options.gift_weight / 100
        gift_filler_count = math.floor(locations_left * gift_filler_weight)
        filler_count = locations_left - gift_filler_count

        # Creates filler in remaining slots
        self.multiworld.itempool.extend([self.create_filler_gift() for _ in range(gift_filler_count)])
        self.multiworld.itempool.extend([self.create_filler() for _ in range(filler_count)])

    def generate_basic(self) -> None:
        # for debugging purposes, you may want to visualize the layout of your world. Uncomment the following code to
        # write a PlantUML diagram to the file "my_world.puml" that can help you see whether your regions and locations
        # are connected and placed as desired
        #from Utils import visualize_regions
        #visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
        pass

    def set_rules(self) -> None:
        # Goal Conditions

        # Easter Egg Hunt
        if self.options.goal_condition == 0:
            # Whether or not we require *all* selected goal items (Randomised goal selection)
            ee_goal_count = min(self.options.goal_ee_count, len(self.ee_goal_items))
            ee_allow_any = not self.options.goal_ee_random
            print("Allowed goal items:")
            print(self.ee_goal_items)
            print("Required number to goal:")
            print(ee_goal_count)
            if not ee_allow_any:
                self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.ee_goal_items, self.player)
            else:
                self.multiworld.completion_condition[self.player] = lambda state: state.has_from_list(self.ee_goal_items, self.player, min(self.options.goal_ee_count, len(self.ee_goal_items)))
            
        # Weapon Quest
        if self.options.goal_condition == 1:
            self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.weapon_quest_items, self.player)

        # Goal Round
        if self.options.goal_condition == 2:
            self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.goal_round_items, self.player)

    def fill_slot_data(self) -> dict:
        options = self.options
        
        slot_data = {
            'seed': "".join(
                self.random.choice(string.ascii_letters) for _ in range(16)),
            'base_id': str(self.base_id),
            "slot": self.multiworld.player_name[self.player],
            "map_the_giant_enabled": bool(options.map_the_giant_enabled),
            "map_castle_enabled": bool(options.map_castle_enabled),
            "map_specific_machines": bool(options.map_specific_machines),
            "map_specific_wallbuys": bool(options.map_specific_wallbuys),
            "special_rounds_enabled": bool(options.special_rounds_enabled),
            "perk_limit_default_modifier": int(options.perk_limit_default_modifier),
            "randomized_shield_parts": bool(options.randomized_shield_parts),
        }

        return slot_data

    @staticmethod
    def get_round_location_string(map_name: str, goal_round: int):
        if map_name == "The Giant":
            return Locations.TheGiant_Locations[goal_round - 1].name
        return ""

def add_universal_items(enabled_items, seen, items):
    for item in items:
        if item[0] not in seen:
            enabled_items.append(item)
            seen.add(item[0])

def add_round_locations(enabled_location_names, round_locations, round_max, round_freq, is_goal_cond, goal_round):
    if round_freq > 0:
        i = round_freq
        # Add rounds into pool
        while i <= round_max:
            enabled_location_names.append(round_locations[i - 1].name)
            i += round_freq
        # Make sure the Goal Round is always included
        if is_goal_cond:
            if goal_round > round_max or goal_round % round_freq != 0:
                enabled_location_names.append(round_locations[goal_round - 1].name)
