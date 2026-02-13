import string
import math
import random
import os

from BaseClasses import Location, MultiWorld, Region, Item, ItemClassification, Tutorial

from worlds.AutoWorld import World, WebWorld

from worlds.generic.Rules import set_rule

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

        self.rolled_bows = []
        self.weapon_quest_items = []
        pass

    def create_regions(self):
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
            add_round_locations(all_locations, Locations.Shadows_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.Shadows_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Shadows_Quest_ApothiconSword_Locations])

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Shadows_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Shadows_MainEE, ee_locs)
            main_ee_region_requirements = []
            if self.options.randomized_shield_parts:
                main_ee_region_requirements = [item.name for item in Items.Shadows_Shield]
            if self.options.mystery_box_special_items:
                main_ee_region_requirements += [item.name for item in Items.Shadows_MysteryBox]
            menu_region.connect(main_ee_region, rule = lambda state: state.has_all(main_ee_region_requirements, self.player))
    
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
            bow_count = min(self.options.castle_bow_count.value, 4)
            bow_pairs = self.random.sample(bow_pairs, bow_count)
            for bow in bow_pairs:
                all_locations.extend([loc.name for loc in bow[0]])
                self.weapon_quest_items.append(bow[1].name)
                if bow[1].name == ItemName.Castle_Victory_ElementalBow_Storm:
                    self.rolled_bows.append("storm")
                if bow[1].name == ItemName.Castle_Victory_ElementalBow_Wolf:
                    self.rolled_bows.append("wolf")
                if bow[1].name == ItemName.Castle_Victory_ElementalBow_Fire:
                    self.rolled_bows.append("fire")
                if bow[1].name == ItemName.Castle_Victory_ElementalBow_Void:
                    self.rolled_bows.append("void")


            add_round_locations(all_locations, Locations.Castle_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.Castle_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Castle_Quest_Locations])
            if self.options.music_ee_enabled:
                all_locations.extend([loc.name for loc in Locations.Castle_Quest_Music_Locations])

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Castle_Quest_MainEE_Locations[:4]]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Castle_MainEE, ee_locs)
            main_ee_region_requirements = []
            if self.options.randomized_shield_parts:
                main_ee_region_requirements = [item.name for item in Items.Castle_Shield]
            if self.options.mystery_box_special_items:
                main_ee_region_requirements += [item.name for item in Items.Castle_MysteryBox]
            menu_region.connect(main_ee_region, rule = lambda state: state.has_all(main_ee_region_requirements, self.player))

            main_region = self.create_region(self.multiworld, self.player, RegionName.Castle_Gondola, all_locations)
            self.multiworld.regions.append(main_region)
            menu_region.connect(main_region)

            # Weapon Quest - Add available bows
            if self.options.goal_condition == 1:
                for bow in bow_pairs:
                    self.multiworld.get_location(bow[0][-1].name, self.player).place_locked_item(bow[1])
            
            boss_fight_locations = []
            if add_ee_checks:
                boss_fight_locations = [loc.name for loc in Locations.Castle_Quest_MainEE_Locations[4:]]
            boss_region = self.create_region(self.multiworld, self.player, RegionName.Castle_BossFight, boss_fight_locations)
            self.multiworld.regions.append(boss_region)
            main_ee_region.connect(boss_region, rule = lambda state: state.has_all([item.name for item in Items.Castle_Craftables], self.player))

        if self.options.map_zetsubou_enabled:
            all_locations = []
            add_round_locations(all_locations, Locations.Zetsubou_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_Challenges_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_KT4_Locations])
            all_locations.extend([loc.name for loc in Locations.Zetsubou_Quest_Skull_Locations])

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Zetsubou_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Zetsubou_MainEE, ee_locs)
            main_ee_region_requirements = []
            if self.options.randomized_shield_parts:
                main_ee_region_requirements = [item.name for item in Items.Zetsubou_Shield]
            if self.options.mystery_box_special_items:
                main_ee_region_requirements += [item.name for item in Items.Zetsubou_MysteryBox]
                main_ee_region_requirements += [item.name for item in Items.Zetsubou_Craftables_Gasmask]
            menu_region.connect(main_ee_region, rule = lambda state: state.has_all(main_ee_region_requirements, self.player))

            main_region = self.create_region(self.multiworld, self.player, RegionName.Zetsubou_Beach, all_locations)
            self.multiworld.regions.append(main_region)
            menu_region.connect(main_region)


        if self.options.map_gorod_enabled:
            all_locations = []
            add_round_locations(all_locations, Locations.GorodKrovi_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.GorodKrovi_Craftable_Locations])
            # Remove dragon wings location if we start with them
            if self.options.difficulty_gorod_dragon_wings:
                all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_SideEE[1:]])
            else:
                all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_SideEE])
            # Challenges 2 and 4 are locked behind other regions
            all_locations.append(Locations.GorodKrovi_Quest_Challenges[0].name)
            all_locations.append(Locations.GorodKrovi_Quest_Challenges[2].name)
            all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_DragonGauntlets])
            all_locations.extend([loc.name for loc in Locations.GorodKrovi_Quest_DragonStrikes])

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.GorodKrovi_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_MainEE, ee_locs)
            main_ee_region_requirements = []
            if self.options.randomized_shield_parts:
                main_ee_region_requirements = [item.name for item in Items.GorodKrovi_Shield]
            if self.options.mystery_box_special_items:
                main_ee_region_requirements += [item.name for item in Items.GorodKrovi_MysteryBox]
            menu_region.connect(main_ee_region, rule = lambda state: state.has_all(main_ee_region_requirements, self.player))

            # Checks which require the shield items
            shield_locations = (
                [Locations.GorodKrovi_Quest_Challenges[1].name] +
                [loc.name for loc in Locations.GorodKrovi_Quest_TiamatsMaw]
            )
            shield_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_Shield, shield_locations)
            self.multiworld.regions.append(shield_region)

            # Monkey Bomb upgrade location - Requires shield as well as monkey bombs in box
            monkeybomb_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_MonkeyBombs, [Locations.GorodKrovi_Quest_Challenges[3].name])
            self.multiworld.regions.append(monkeybomb_region)
            if self.options.mystery_box_special_items:
                shield_region.connect(monkeybomb_region, rule = lambda state: state.has(Items.GorodKrovi_MysteryBox[1].name, self.player))
            else:
                shield_region.connect(monkeybomb_region)

            main_region = self.create_region(self.multiworld, self.player, RegionName.Gorod_Trenches, all_locations)
            self.multiworld.regions.append(main_region)
            if self.options.randomized_shield_parts:
                main_region.connect(shield_region, rule = lambda state: state.has_all([item.name for item in Items.GorodKrovi_Shield], self.player))
            else:
                main_region.connect(shield_region)

            menu_region.connect(main_region)

        if self.options.map_revelations_enabled:
            all_locations = []
            add_round_locations(all_locations, Locations.Revelations_Round_Locations, round_max, round_freq, is_round_goal_cond, goal_round)
            all_locations.extend([loc.name for loc in Locations.Revelations_Quest_MainQuest_Locations])
            all_locations.extend([loc.name for loc in Locations.Revelations_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Revelations_Quest_SideEE_Locations])
            all_locations.extend([loc.name for loc in Locations.Revelations_Quest_Challenges])

            weapon_quest_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_WeaponQuest, [loc.name for loc in Locations.Revelations_Quest_Weapons])
            weapon_quest_region_requirements = []
            if self.options.mystery_box_special_items:
                weapon_quest_region_requirements += [Items.Revelations_MysteryBox[1].name, Items.Revelations_Machines[2].name]
            menu_region.connect(weapon_quest_region, rule = lambda state: state.has_all(weapon_quest_region_requirements, self.player))

            ee_locs = []
            if add_ee_checks:
                ee_locs = [loc.name for loc in Locations.Revelations_Quest_MainEE_Locations]

            main_ee_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_MainEE, ee_locs)
            main_ee_region_requirements = [item.name for item in Items.Revelations_Shield]
            if self.options.mystery_box_special_items:
                main_ee_region_requirements += [item.name for item in Items.Revelations_MysteryBox]
            menu_region.connect(main_ee_region, rule = lambda state: state.has_all(main_ee_region_requirements, self.player))
            
            main_region = self.create_region(self.multiworld, self.player, RegionName.Revelations_House, all_locations)

            self.multiworld.regions.append(main_region)
            menu_region.connect(main_region)

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
            Items.BO3ZombiesItemCategory.REGULAR_WEAPON,
            Items.BO3ZombiesItemCategory.CRAFTABLE,
        }

        # TODO: do a getProgressiveItems list instead
        progression_categories = {
            Items.BO3ZombiesItemCategory.MACHINE,
            Items.BO3ZombiesItemCategory.PROGRESSIVE,
            Items.BO3ZombiesItemCategory.SPECIAL_WEAPON,
            Items.BO3ZombiesItemCategory.CRAFTABLE,
            Items.BO3ZombiesItemCategory.BLOCKER,
            Items.BO3ZombiesItemCategory.POWER,
            Items.BO3ZombiesItemCategory.EASTER_EGG,
            Items.BO3ZombiesItemCategory.VICTORY
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
            random.shuffle(self._gift_bag)

        gift = self._gift_bag.pop()
        return self.create_item(gift[0])
    
    def create_filler_trap(self) -> Item:
        if not hasattr(self, '_trap_bag') or not self._trap_bag:
            self._trap_bag = list(Items.Trap_Items)
            random.shuffle(self._trap_bag)

        gift = self._trap_bag.pop()
        return self.create_item(gift[0])

    def create_filler(self) -> Item:
        # TODO make a proper filler item
        return self.create_item(ItemName.Points50)

    def create_items(self) -> None:
        enabled_items = [item for item in Items.base_items]
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
            if self.options.map_zetsubou_enabled:
                enabled_items += Items.Zetsubou_Machines_Specific
            if self.options.map_gorod_enabled:
                enabled_items += Items.GorodKrovi_Machines_Specific
            if self.options.map_revelations_enabled:
                enabled_items += Items.Revelations_Machines_Specific
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
        if self.options.map_zetsubou_enabled:
            map_list.append(Maps.Zetsubou_Map_String)
            if self.options.randomized_shield_parts:
                enabled_items += Items.Zetsubou_Shield
            enabled_items += Items.Zetsubou_Craftables_Gasmask
        if self.options.map_gorod_enabled:
            map_list.append(Maps.GorodKrovi_Map_String)
            if self.options.randomized_shield_parts:
                enabled_items += Items.GorodKrovi_Shield
            # enabled_items += Items.GorodKrovi_Craftables_Dragonride
        if self.options.map_revelations_enabled:
            map_list.append(Maps.Revelations_Map_String)
            if self.options.randomized_shield_parts:
                enabled_items += Items.Revelations_Shield

        if self.options.mystery_box_special_items:
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_MysteryBox
            if self.options.map_shadows_enabled:
                enabled_items += Items.Shadows_MysteryBox
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_MysteryBox
            if self.options.map_zetsubou_enabled:
                enabled_items += Items.Zetsubou_MysteryBox
            if self.options.map_gorod_enabled:
                enabled_items += Items.GorodKrovi_MysteryBox
            if self.options.map_revelations_enabled:
                enabled_items += Items.Revelations_MysteryBox

        if self.options.mystery_box_regular_items:
            seen = set()
            if self.options.map_the_giant_enabled:
                add_universal_items(enabled_items, seen, Items.The_Giant_MysteryBox_Regular)
            if self.options.map_shadows_enabled:
                add_universal_items(enabled_items, seen, Items.Shadows_MysteryBox_Regular)
            if self.options.map_castle_enabled:
                add_universal_items(enabled_items, seen, Items.Castle_MysteryBox_Regular)
            if self.options.map_zetsubou_enabled:
                add_universal_items(enabled_items, seen, Items.Zetsubou_MysteryBox_Regular)
            if self.options.map_gorod_enabled:
                add_universal_items(enabled_items, seen, Items.GorodKrovi_MysteryBox_Regular)
            if self.options.map_revelations_enabled:
                add_universal_items(enabled_items, seen, Items.Revelations_MysteryBox_Regular)

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
                goal_item = self.create_item(ItemName.Shadows_Victory_ApothiconSwordLvl2)
                self.weapon_quest_items.append(ItemName.Shadows_Victory_ApothiconSwordLvl2)
                self.multiworld.get_location(Locations.Shadows_Quest_ApothiconSword_Locations[-1].name, self.player).place_locked_item(goal_item) 
            
            if self.options.map_castle_enabled:
                # Handled in create_regions
                pass
            
            if self.options.map_zetsubou_enabled:
                goal_items = list(map(self.create_item, [
                    ItemName.Zetsubou_Victory_Masamune,
                    ItemName.Zetsubou_Victory_Skull,
                ]))
                self.weapon_quest_items.extend([item.name for item in goal_items])
                self.multiworld.get_location(Locations.Zetsubou_Quest_KT4_Locations[-1].name, self.player).place_locked_item(goal_items[0])
                self.multiworld.get_location(Locations.Zetsubou_Quest_Skull_Locations[-1].name, self.player).place_locked_item(goal_items[1])
            
            if self.options.map_gorod_enabled:
                goal_items = list(map(self.create_item, [
                    ItemName.GorodKrovi_Victory_DragonGauntlets,
                    ItemName.GorodKrovi_Victory_Upgraded_Dragonstrikes,
                    ItemName.GorodKrovi_Victory_Upgraded_MonkeyBombs,
                    ItemName.GorodKrovi_Victory_TiamatsMaw
                ]))
                self.weapon_quest_items.extend([item.name for item in goal_items])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_DragonGauntlets[-1].name, self.player).place_locked_item(goal_items[0])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_DragonStrikes[-1].name, self.player).place_locked_item(goal_items[1])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_Challenges[3].name, self.player).place_locked_item(goal_items[2])
                self.multiworld.get_location(Locations.GorodKrovi_Quest_TiamatsMaw[-1].name, self.player).place_locked_item(goal_items[3])

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
            self.slot_goal_items_required = len(self.slot_goal_items)
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
            "mystery_box_special_items": bool(options.mystery_box_special_items),
            "mystery_box_regular_items": bool(options.mystery_box_regular_items),
            "difficulty_gorod_egg_cooldown": bool(options.difficulty_gorod_egg_cooldown),
            "difficulty_gorod_dragon_wings": bool(options.difficulty_gorod_dragon_wings),
            "difficulty_ee_checkpoints": options.difficulty_ee_checkpoints.value,
            "difficulty_round_checkpoints": options.difficulty_round_checkpoints.value,
            "rolled_bows": self.rolled_bows,
            "goal_items_required": int(self.slot_goal_items_required),
            "goal_items": self.slot_goal_items,
        }

        return slot_data

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
