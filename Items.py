import typing
from enum import IntEnum
from BaseClasses import Item
from .Names import ItemName

def gen_map_wallbuy_set(mapString, wallbuys):
    map_specific_set = [ItemData(mapString + " " + wallbuy[0], wallbuy[1]) for wallbuy in wallbuys]
    return map_specific_set

class BO3ZombiesItemCategory(IntEnum):
    BLOCKER = 5
    WALLBUY = 6
    POWER = 7
    EASTER_EGG = 8
    MACHINE = 9
    MISC = 10
    VICTORY = 11


class ItemData(typing.NamedTuple):
    name: str
    category: BO3ZombiesItemCategory

class BO3ZombiesItem(Item):
    game: str = "Black Ops 3 - Zombies"

    @staticmethod
    def get_name_to_id(base_id) -> dict:
        return {item_data.name: id for id, item_data in enumerate(all_items, base_id)}
    
The_Giant_Map_String = "(The Giant)"

The_Giant_Blockers_Doors = [ItemData(row[0], row[1]) for row in [  
    (ItemName.TheGiant_AnimalTesting,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Garage,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_PowerRoom,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Teleporter1,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Teleporter2,BO3ZombiesItemCategory.BLOCKER),
    (ItemName.TheGiant_Teleporter3,BO3ZombiesItemCategory.BLOCKER),
]]

# The Giant Items
The_Giant_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.TheGiant_Juggernog, BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_QuickRevive, BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_DoubleTap, BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_SpeedCola,BO3ZombiesItemCategory.MACHINE),
    (ItemName.TheGiant_MuleKick, BO3ZombiesItemCategory.MACHINE),
]]

The_Giant_Wallbuys = [ItemData(row[0], row[1]) for row in[
    # Teleporter A
    (ItemName.Weapon_M8A7,BO3ZombiesItemCategory.WALLBUY),
    # Teleporter B
    (ItemName.Weapon_HVK,BO3ZombiesItemCategory.WALLBUY),
    # Teleporter C
    (ItemName.Weapon_KN44,BO3ZombiesItemCategory.WALLBUY),
    (ItemName.Weapon_BowieKnife,BO3ZombiesItemCategory.WALLBUY),
    # Starting Area
    (ItemName.Weapon_Sheiva,BO3ZombiesItemCategory.WALLBUY),
    (ItemName.Weapon_RK5,BO3ZombiesItemCategory.WALLBUY),
    # Courtyard
    (ItemName.Weapon_VMP,BO3ZombiesItemCategory.WALLBUY),
    # Garage
    (ItemName.Weapon_VMP,BO3ZombiesItemCategory.WALLBUY),
    (ItemName.Weapon_KRM,BO3ZombiesItemCategory.WALLBUY),
    # Animal Testing
    (ItemName.Weapon_Kuda,BO3ZombiesItemCategory.WALLBUY),
    (ItemName.Weapon_LCAR,BO3ZombiesItemCategory.WALLBUY)
]]

The_Giant_Wallbuys_Specific = gen_map_wallbuy_set(The_Giant_Map_String, The_Giant_Wallbuys)

# Point Drop Items
Points_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points500, BO3ZombiesItemCategory.MISC)
]]

# Victory
Victory_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.TheGiant_Victory, BO3ZombiesItemCategory.VICTORY)
]]

# Misc/Filler Items
Misc_Items = [ItemData(row[0], row[1]) for row in [
    (ItemName.Points50, BO3ZombiesItemCategory.MISC)
]]

base_items = Points_Items

all_items = Points_Items + Victory_Items + Misc_Items + The_Giant_Blockers_Doors + The_Giant_Items + The_Giant_Wallbuys + The_Giant_Wallbuys_Specific

all_items_dict = {item_data.name: item_data for item_data in all_items}
