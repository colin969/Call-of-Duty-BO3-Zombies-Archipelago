import string
import math
import random

from BaseClasses import MultiWorld, Region, Item, ItemClassification, Tutorial

from worlds.AutoWorld import World, WebWorld

from . import Regions, Locations, Items, Options
from .Options import BO3ZombiesOptions, bo3_option_groups
from .Names import ItemName, LocationName, RegionName, Maps

from .Logic import CODBO3Logic

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

    enabled_location_names = []
    victory_items = []
    # Options

    def generate_early(self) -> None:
        for location in Locations.early_locations:
            self.enabled_location_names.append(location.name)

        if self.options.map_the_giant_enabled:
            for i in range(0, self.options.victory_round):
                self.enabled_location_names.append(Locations.TheGiant_Round_Locations[i].name)
        if self.options.map_castle_enabled:
            self.enabled_location_names.extend([row.name for row in Locations.Castle_Craftable_Locations])
            self.enabled_location_names.extend([row.name for row in Locations.Castle_Quest_Locations])
            for i in range(0, self.options.victory_round):
                self.enabled_location_names.append(Locations.Castle_Round_Locations[i].name)

    def create_regions(self):
        universal_locations = [
            LocationName.RepairWindows_5
        ]
        print(self.enabled_location_names)
        menu_region = self.create_region(self.multiworld, self.player, self.enabled_location_names, 'Menu', universal_locations)
        
        self.multiworld.regions.append(menu_region)
        
        # Default Balancing, Make sure you get to every region
        # TODO: Randomize this a bit/weight it

        map_rounds = self.options.victory_round

        print("Assigning regions")

        if self.options.map_the_giant_enabled:
            rounds_assigned = 0
            # Courtyard

            region_distributions = [
                (RegionName.TheGiant_Courtyard, 3),
                (RegionName.TheGiant_AnimalTesting, 3),
                (RegionName.TheGiant_Garage, 4),
                (RegionName.TheGiant_PowerRoom, 4),
                (RegionName.TheGiant_Teleporter1, 0),
                (RegionName.TheGiant_Teleporter2, 7),
                (RegionName.TheGiant_Teleporter3, 999)
            ]
            
            # Add round locations until each region is full, or we run out of locations to allocate
            for region_name, desired_count in region_distributions:
                assigned_rounds = max(desired_count, (map_rounds - rounds_assigned))
                print("Assigned " + str(assigned_rounds) + " to Region " + region_name)
                
                if assigned_rounds > 0:
                    self.multiworld.regions.append(
                        self.create_region(self.multiworld, self.player, self.enabled_location_names,
                            region_name,
                            [loc[0] for loc in Locations.TheGiant_Round_Locations[rounds_assigned:rounds_assigned + assigned_rounds]]
                        )
                    )
                    rounds_assigned += assigned_rounds
                else:
                    self.multiworld.regions.append(
                        self.create_region(self.multiworld, self.player, self.enabled_location_names,
                            region_name,
                            []
                        )
                    )
        
        if self.options.map_castle_enabled:
            # TODO: Add blockers
            all_locations = []
            all_locations.extend([loc.name for loc in Locations.Castle_Round_Locations[0:map_rounds]])
            all_locations.extend([loc.name for loc in Locations.Castle_Craftable_Locations])
            all_locations.extend([loc.name for loc in Locations.Castle_Quest_Locations])
            self.multiworld.regions.append(
                self.create_region(self.multiworld, self.player, self.enabled_location_names,
                    RegionName.Castle_Gondola,
                    all_locations
                )
            )
        
        Regions.connect_regions(self.multiworld, self.player)

    def create_region(self, world: MultiWorld, player: int, active_location_names: list, name: str, locations=None):
        ret = Region(name, player, world)
        if locations:
            for location in locations:
                if location in active_location_names:
                    location = Locations.BO3ZombiesLocation(player, location, self.location_name_to_id[location], ret)
                    ret.locations.append(location)

        return ret

    def create_item(self, name: str) -> Item:
        useful_categories = {
            Items.BO3ZombiesItemCategory.WALLBUY,
            Items.BO3ZombiesItemCategory.MACHINE,
        }

        # TODO: do a getProgressiveItems list instead
        progression_categories = {
            Items.BO3ZombiesItemCategory.BLOCKER,
            Items.BO3ZombiesItemCategory.POWER,
            Items.BO3ZombiesItemCategory.EASTER_EGG,
            Items.BO3ZombiesItemCategory.VICTORY
        }
        data = self.item_name_to_id[name]

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

        # Add machines to pool
        if self.options.map_specific_machines:
            # Add map specific machines for each
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_Machines_Specific
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_Machines_Specific
        else:
            # Only add one instance per machine
            seen = set()
            if self.options.map_the_giant_enabled:
                for machine in Items.The_Giant_Machines:
                    if machine[0] not in seen:
                        enabled_items.append(machine)
                        seen.add(machine[0])
            if self.options.map_castle_enabled:
                for machine in Items.Castle_Machines:
                    if machine[0] not in seen:
                        enabled_items.append(machine)
                        seen.add(machine[0])

        # Add wallbuys to pool
        if self.options.map_specific_wallbuys:
            # Add map specific wallbuys for each
            if self.options.map_the_giant_enabled:
                enabled_items += Items.The_Giant_Wallbuys_Specific
            if self.options.map_castle_enabled:
                enabled_items += Items.Castle_Wallbuys_Specific
        else:
            # Only add one instance per wallbuy
            seen = set()
            if self.options.map_the_giant_enabled:
                for wallbuy in Items.The_Giant_Wallbuys:
                    if wallbuy[0] not in seen:
                        enabled_items.append(wallbuy)
                        seen.add(wallbuy[0])
            if self.options.map_castle_enabled:
                for wallbuy in Items.Castle_Wallbuys:
                    if wallbuy[0] not in seen:
                        enabled_items.append(wallbuy)
                        seen.add(wallbuy[0])


        if self.options.map_the_giant_enabled:
            enabled_items += Items.The_Giant_Blockers_Doors

        enabled_items_dict = {item_data.name: item_data for item_data in enabled_items}

        map_list = []
        if self.options.map_the_giant_enabled:
            map_list.append(Maps.The_Giant_Map_String)
        if self.options.map_castle_enabled:
            map_list.append(Maps.Castle_Map_String)

        if self.options.victory_round_choice == 0:
            # Random victory round item
            victory_map = random.choice(map_list)
            self.victory_items.append(victory_map + " Victory")
            victory_location = Locations.get_map_victory_location(victory_map, self.options.victory_round)
            self.multiworld.get_location(victory_location, self.player).place_locked_item(
                self.create_item(victory_map + " Victory")
            )
        else:
            for m in map_list:
                # Victory round item on every map
                self.victory_items.append(m + " Victory")
                victory_location = Locations.get_map_victory_location(m, self.options.victory_round)
                self.multiworld.get_location(victory_location, self.player).place_locked_item(
                    self.create_item(m + " Victory")
                )

        filler_count = len(self.enabled_location_names)
        exclude = [item for item in self.multiworld.precollected_items[self.player]]

        filler_count -= len(exclude)
        filler_count -= len(self.victory_items)

        for item in map(self.create_item, enabled_items_dict):
            if (Items.all_items_dict[item.name] not in self.victory_items) and (item not in exclude):
                self.multiworld.itempool.append(item)
                filler_count -= 1

        gift_filler_weight = self.options.gift_weight / 100
        gift_filler_count = math.floor(filler_count * gift_filler_weight)
        filler_count -= gift_filler_count

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
        # Collect all Victory Items for Victory
        self.multiworld.completion_condition[self.player] = lambda state: state.has_all(self.victory_items, self.player)

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
            "blocker_doors_enabled": bool(options.blocker_doors_enabled),
        }

        return slot_data

    @staticmethod
    def get_round_location_string(map_name: str, victory_round: int):
        if map_name == "The Giant":
            return Locations.TheGiant_Locations[victory_round - 1].name
        return ""
