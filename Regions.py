import typing

from BaseClasses import MultiWorld, Region, Entrance

from .Locations import BO3ZombiesLocation
from .Names import RegionName


def connect_regions(world: MultiWorld, player: int):
    names: typing.Dict[str, int] = {}

    # connecting Menu to enabled starting locations
    connect(world, player, names, "Menu", RegionName.TheGiant_Courtyard)
    connect(world, player, names, "Menu", RegionName.Castle_Gondola)
    connect(world, player, names, RegionName.Castle_Gondola, RegionName.Castle_BossFight)
    connect(world, player, names, "Menu", RegionName.Shadows_Alleyway)

# shamelessly stolen from the sa2b (and hk2)
def connect(world: MultiWorld, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def create_region(world: MultiWorld, player: int, active_locations, name: str, locations=None):
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            loc_id = active_locations.get(location, 0)
            if loc_id:
                location = BO3ZombiesLocation(player, location, loc_id.code, ret)
                ret.locations.append(location)

    return ret
