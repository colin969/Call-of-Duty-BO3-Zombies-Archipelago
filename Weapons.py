from typing import NamedTuple
from .Names import ItemName, Maps

class WeaponData(NamedTuple):
    category: str
    strength: int
    item_name: str

weapon_data_set: dict[str, dict[str, WeaponData]] = {
    "vanilla": {
        # Assault Rifles
        "ar_accurate": WeaponData("ar", 4, ItemName.Weapon_ICR),
        "ar_cqb": WeaponData("ar", 4, ItemName.Weapon_HVK),
        "ar_damage": WeaponData("ar", 4, ItemName.Weapon_ManoWar),
        "ar_longburst": WeaponData("ar", 2, ItemName.Weapon_M8A7),
        "ar_marksman": WeaponData("ar", 1, ItemName.Weapon_Sheiva),
        "ar_standard": WeaponData("ar", 3, ItemName.Weapon_KN44),
        "ar_famas": WeaponData("ar", 3, ItemName.Weapon_FFAR),
        "ar_garand": WeaponData("ar", 1, ItemName.Weapon_Garand),
        "ar_peacekeeper": WeaponData("ar", 3, ItemName.Weapon_Peacekeeper),
        "ar_an94": WeaponData("ar", 2, ItemName.Weapon_AN94),
        "ar_galil": WeaponData("ar", 2, ItemName.Weapon_Galil),
        "ar_m14": WeaponData("ar", 1, ItemName.Weapon_M14),
        "ar_m16": WeaponData("ar", 4, ItemName.Weapon_M16),
        "ar_pulse": WeaponData("ar", 0, ItemName.Weapon_Basilisk),
        "ar_fastburst": WeaponData("ar", 0, ItemName.Weapon_XR2),
        "ar_stg44": WeaponData("ar", 2, ItemName.Weapon_STG44),
        
        # Light Machine Guns
        "lmg_cqb": WeaponData("lmg", 4, ItemName.Weapon_Dingo),
        "lmg_heavy": WeaponData("lmg", 3, ItemName.Weapon_Dredge),
        "lmg_light": WeaponData("lmg", 2, ItemName.Weapon_BRM),
        "lmg_slowfire": WeaponData("lmg", 1, ItemName.Weapon_Gorgon),
        "lmg_infinite": WeaponData("lmg", 3, ItemName.Weapon_R70Ajax),
        "lmg_rpk": WeaponData("lmg", 4, ItemName.Weapon_RPK),
        "lmg_mg08": WeaponData("lmg", 3, ItemName.Weapon_MG08),
        
        # Sub Machine Guns
        "smg_burst": WeaponData("smg", 1, ItemName.Weapon_Pharo),
        "smg_capacity": WeaponData("smg", 1, ItemName.Weapon_Weevil),
        "smg_fastfire": WeaponData("smg", 2, ItemName.Weapon_Vesper),
        "smg_standard": WeaponData("smg", 2, ItemName.Weapon_Kuda),
        "smg_versatile": WeaponData("smg", 3, ItemName.Weapon_VMP),
        "smg_sten": WeaponData("smg", 3, ItemName.Weapon_Bootlegger),
        "smg_mp40": WeaponData("smg", 3, ItemName.Weapon_HG40),
        "smg_ppsh": WeaponData("smg", 3, ItemName.Weapon_PPSH),
        "smg_thompson": WeaponData("smg", 0, ItemName.Weapon_M1927),
        "smg_longrange": WeaponData("smg", 4, ItemName.Weapon_Razorback),
        "smg_ak74u": WeaponData("smg", 4, ItemName.Weapon_AK47u),
        "smg_msmc": WeaponData("smg", 3, ItemName.Weapon_MSMC),
        "smg_nailgun": WeaponData("smg", 3, ItemName.Weapon_Nailgun),
        "smg_rechamber": WeaponData("smg", 3, ItemName.Weapon_HLX4),
        "smg_sten2": WeaponData("smg", 2, ItemName.Weapon_Sten),
        "smg_mp40_1940": WeaponData("smg", 2, ItemName.Weapon_MP40),
        
        # Snipers
        "sniper_fastsemi": WeaponData("sniper", 4, ItemName.Weapon_Drakon),
        "sniper_fastbolt": WeaponData("sniper", 3, ItemName.Weapon_Locus),
        "sniper_powerbolt": WeaponData("sniper", 1, ItemName.Weapon_SVG),
        
        # Shotguns
        "shotgun_fullauto": WeaponData("shotgun", 4, ItemName.Weapon_Haymaker),
        "shotgun_precision": WeaponData("shotgun", 2, ItemName.Weapon_Argus),
        "shotgun_pump": WeaponData("shotgun", 1, ItemName.Weapon_KRM),
        "shotgun_semiauto": WeaponData("shotgun", 4, ItemName.Weapon_Brecci),
        "shotgun_energy": WeaponData("shotgun", 1, ItemName.Weapon_Banshii),
        "shotgun_olympia": WeaponData("shotgun", 1, ItemName.Weapon_Olympia),
        
        # Pistols
        "pistol_revolver38": WeaponData("pistol", 1, ItemName.Weapon_Bloodhound),
        "pistol_standard": WeaponData("pistol", 1, ItemName.Weapon_MR6),
        "pistol_burst": WeaponData("pistol", 2, ItemName.Weapon_RK5),
        "pistol_fullauto": WeaponData("pistol", 1, ItemName.Weapon_LCAR),
        "pistol_energy": WeaponData("pistol", 1, ItemName.Weapon_RiftE9),
        "pistol_m1911": WeaponData("pistol", 1, ItemName.Weapon_M1911),
        "pistol_shotgun_dw": WeaponData("pistol", 3, ItemName.Weapon_Marshal16),
        "pistol_c96": WeaponData("pistol", 1, ItemName.Weapon_MauserC96),

        # Launchers
        "launcher_standard": WeaponData("launcher", 1, ItemName.Weapon_XM53),
        "launcher_multi": WeaponData("launcher", 1, ItemName.Weapon_Siege),
        "launcher_ex41": WeaponData("launcher", 1, ItemName.Weapon_ChinaLake),

        # Other?
        "special_crossbow_dw": WeaponData("other", 1, ItemName.Weapon_Shadowclaw),

        # Regular Equipment
        "bouncingbetty": WeaponData("equipment", 1, ItemName.Weapon_TripMines),
        "hero_annihilator": WeaponData("equipment", 3, ItemName.Weapon_Annihilator),

        # Melee
        "bowie_knife": WeaponData("melee", 2, ItemName.Weapon_BowieKnife),
        "melee_dagger": WeaponData("melee", 2, ItemName.Weapon_Dagger),
        "melee_fireaxe": WeaponData("melee", 2, ItemName.Weapon_Fireaxe),
        "melee_sword": WeaponData("melee", 2, ItemName.Weapon_Sword),
        "melee_wrench": WeaponData("melee", 2, ItemName.Weapon_Wrench),
        "melee_boneglass": WeaponData("melee", 2, ItemName.Weapon_Claws),
        "melee_improvise": WeaponData("melee", 2, ItemName.Weapon_BuzzCutter),
        "melee_nunchuks": WeaponData("melee", 2, ItemName.Weapon_Nunchuks),
        "melee_mace": WeaponData("melee", 2, ItemName.Weapon_Mace),
        "melee_katana": WeaponData("melee", 2, ItemName.Weapon_Katana),
        
        # Wonder Weapons
        "ray_gun": WeaponData("wonder", 2, ItemName.Weapon_Raygun),
        "raygun_mark2": WeaponData("wonder", 4, ItemName.Weapon_RaygunMk2),
        "raygun_mark3": WeaponData("wonder", 5, ItemName.Weapon_RaygunMk3),
        "tesla_gun": WeaponData("wonder", 4, ItemName.Weapon_Wunderwaffe),
        "idgun_genesis_0": WeaponData("wonder", 5, ItemName.Weapon_ApothiconServant),
        "idgun_0": WeaponData("wonder", 5, ItemName.Weapon_ApothiconServant),
        "hero_mirg2000": WeaponData("wonder", 4, ItemName.Weapon_KT4),
        "thundergun": WeaponData("wonder", 4, ItemName.Weapon_Thundergun),
        "hero_gravityspikes_melee": WeaponData("wonder", 5, ItemName.Weapon_Ragnaroks),
        "cymbal_monkey": WeaponData("wonder", 4, ItemName.Weapon_MonkeyBombs),
        "octobomb": WeaponData("wonder", 5, ItemName.Weapon_LilArnies),
    },
    "zm_westernz":
    {
        "grenade_homunculus": WeaponData("wonder", 4, ItemName.Weapon_Modded_HomunculusBomb),
        "t8_shotgun_blundergat": WeaponData("wonder", 5, ItemName.Weapon_Modded_Blundergat),
        "t8_raygun": WeaponData("wonder", 2, ItemName.Weapon_Raygun),
        "ww2_lewis": WeaponData("lmg", 3, ItemName.Weapon_Modded_Ww2Lewis),
        "m1831": WeaponData("shotgun", 4, ItemName.Weapon_Modded_M1831Blundergat),
        "bo3_boneglass": WeaponData("shotgun", 3, ItemName.Weapon_Modded_Nightbreaker),
        "t8_m1897": WeaponData("shotgun", 2, ItemName.Weapon_Modded_Model1897),
        "ww2_ribeyrolles": WeaponData("smg", 4, ItemName.Weapon_Modded_Ribeyrolles),
        "m1889": WeaponData("shotgun", 2, ItemName.Weapon_Modded_RemingtonM1889),
        "m1903_epic": WeaponData("sniper", 1, ItemName.Weapon_Modded_M1903),
        "bo4_escargot": WeaponData("pistol", 3, ItemName.Weapon_Modded_Escargot),
        "mwr_ranger": WeaponData("shotgun", 1, ItemName.Weapon_Modded_Ranger),
        "ww2_winchester94": WeaponData("ar", 2, ItemName.Weapon_Modded_WinchesterModel94),
        "ww2_crossbow": WeaponData("sniper", 1, ItemName.Weapon_Modded_Crossbow),
        "aw_winchester": WeaponData("ar", 3, ItemName.Weapon_Modded_WinchesterModel94_Auto),
        "doc_w1866": WeaponData("sniper", 1, ItemName.Weapon_Modded_GreatScott),
        "m1896_essex": WeaponData("sniper", 1, ItemName.Weapon_Modded_M1896Essex),
        "ww2_mosin": WeaponData("ar", 2, ItemName.Weapon_Modded_Mosin),
        "ww2_m712": WeaponData("pistol", 1, ItemName.Weapon_Modded_MachinePistol),
        "ww2_enfield2": WeaponData("pistol", 1, ItemName.Weapon_Modded_EnfieldNo2),
        "ww2_enfield2_gold": WeaponData("pistol", 2, ItemName.Weapon_Modded_EnfieldNo2Gold),
        "ww2_colt45saa": WeaponData("pistol", 1, ItemName.Weapon_Modded_Colt45),
        "ww2_reichsrevolver": WeaponData("pistol", 1, ItemName.Weapon_Modded_M1883),
        "t8_welling": WeaponData("pistol", 1, ItemName.Weapon_Modded_WebleyMark4),
        "ww2_iceaxe": WeaponData("melee", 2, ItemName.Weapon_Modded_Icepick),
        "ww2_raven": WeaponData("melee", 2, ItemName.Weapon_Modded_RedTalon),
        "frag_ww2_dynamite": WeaponData("wonder", 4, ItemName.Weapon_Modded_Dynamite),
        "m1827_exp": WeaponData("ar", 4, ItemName.Weapon_Modded_M1892),
        "wes_jag42": WeaponData("launcher", 1, ItemName.Weapon_Modded_Jag42),
        "ww2_fliegerfaust": WeaponData("launcher", 1, ItemName.Weapon_Modded_Fliegerfaust),
        "lebel_m1811": WeaponData("ar", 2, ItemName.Weapon_Modded_M1811),
        "fc4_m1887_long": WeaponData("ar", 1, ItemName.Weapon_Modded_M1887),
        "w1892": WeaponData("ar", 2, ItemName.Weapon_Modded_M1892),
        "ww2_model21": WeaponData("shotgun", 1, ItemName.Weapon_Modded_SawedOff),
        "w1887": WeaponData("ar", 1, ItemName.Weapon_Modded_M1887_2),
        "henry_m1840": WeaponData("shotgun", 2, ItemName.Weapon_Modded_M1840),
        "bo3_olympia": WeaponData("shotgun", 1, ItemName.Weapon_Modded_Olympia),
        "t8_allistair_annihalator": WeaponData("wonder", 5, ItemName.Weapon_Modded_Bo4Annihilator),
        "t8_crossbow": WeaponData("ar", 4, ItemName.Weapon_Modded_Impaler),

    }
}

class WeaponLists(NamedTuple):
    table: str
    special: list[str]
    vanilla: list[str]
    expanded: list[str]
    wallbuys: list[str]

class WeaponDataLists(NamedTuple):
    table: str
    special: dict[str, WeaponData]
    vanilla: dict[str, WeaponData]
    expanded: dict[str, WeaponData]
    wallbuys: dict[str, WeaponData]

map_weapon_lists: dict[str, WeaponLists] = {
    Maps.Shadows_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "ar_accurate",
            "ar_cqb",
            "ar_damage",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "shotgun_fullauto",
            "shotgun_precision",
            "shotgun_semiauto",
            "launcher_standard",
            "smg_burst",
            "smg_capacity",
            "smg_sten",
            "sniper_fastbolt",
            "sniper_fastsemi",
            "sniper_powerbolt",
        ],
        expanded = [
            "pistol_revolver38",
            "bouncingbetty",
            "bowie_knife",
            "ar_longburst",
            "ar_marksman",
            "ar_standard",
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_fastfire",
            "smg_standard",
            "smg_versatile",
        ],
        wallbuys = [
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "ar_cqb",
            "ar_longburst",
            "smg_standard",
            "smg_versatile",
            "smg_fastfire",
            "ar_standard",
            "smg_sten",
            #"bouncingbetty",
            #"bowie_knife",
        ],
        special = [
            "octobomb",
            "ray_gun",
        ]
    ),
    Maps.Castle_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "bouncingbetty",
            "ar_accurate",
            "ar_cqb",
            "ar_damage",
            "ar_marksman",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "shotgun_fullauto",
            "shotgun_precision",
            "shotgun_semiauto",
            "launcher_standard",
            "smg_burst",
            "smg_capacity",
            "smg_versatile",
            "sniper_fastbolt",
            "sniper_fastsemi",
            "sniper_powerbolt",
            "lmg_rpk",
        ],
        expanded = [
            "pistol_standard",
            "bowie_knife",
            "ar_longburst",
            "ar_standard",
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_fastfire",
            "smg_standard",
        ],
        wallbuys = [
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "ar_longburst",
            "ar_cqb",
            "smg_standard",
            "smg_versatile",
            "smg_fastfire",
            "ar_standard",
            "lmg_light",
            "bowie_knife",
        ],
        special = [
            "ray_gun",
            "cymbal_monkey",
        ]
    ),
    Maps.Zetsubou_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "ar_accurate",
            "ar_cqb",
            "ar_damage",
            "ar_garand",
            "ar_longburst",
            "ar_marksman",
            "ar_standard",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "pistol_shotgun_dw",
            "shotgun_fullauto",
            "shotgun_precision",
            "shotgun_semiauto",
            "launcher_standard",
            "smg_capacity",
            "smg_fastfire",
            "smg_longrange",
            "smg_mp40",
            "smg_standard",
            "smg_versatile",
            "sniper_fastbolt",
            "sniper_fastsemi",
            "sniper_powerbolt",
        ],
        expanded = [
            "pistol_standard",
            "bouncingbetty",
            "bowie_knife",
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_burst",
        ],
        wallbuys = [
            "pistol_burst",
            "smg_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_standard",
            "smg_versatile",
            "smg_fastfire",
            "shotgun_precision",
            "ar_standard",
            "ar_accurate",
            "ar_longburst",
            "ar_cqb",
            #"bowie_knife",
        ],
        special = [
            "cymbal_monkey",
            "ray_gun",
        ]
    ),
    Maps.GorodKrovi_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "ar_damage",
            "ar_famas",
            "ar_garand",
            "ar_marksman",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "shotgun_fullauto",
            "shotgun_semiauto",
            "launcher_multi",
            "launcher_standard",
            "smg_capacity",
            "smg_mp40",
            "smg_ppsh",
            "sniper_fastbolt",
            "sniper_fastsemi",
            "sniper_powerbolt",
            "special_crossbow_dw",
            "lmg_rpk",
        ],
        expanded = [
            "bouncingbetty",
            "bowie_knife",
            "ar_accurate",
            "ar_cqb",
            "ar_longburst",
            "ar_standard",
            "pistol_standard",
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_precision",
            "shotgun_pump",
            "smg_burst",
            "smg_fastfire",
            "smg_standard",
            "smg_versatile",
            "melee_dagger",
            "melee_fireaxe",
            "melee_sword",
            "melee_wrench",
        ],
        wallbuys = [
            "pistol_burst",
            "smg_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_standard",
            "smg_versatile",
            "smg_fastfire",
            "shotgun_precision",
            "ar_standard",
            "ar_accurate",
            "ar_longburst",
            "ar_cqb",
            #"bowie_knife",
        ],
        special = [
            "cymbal_monkey",
            "ray_gun",
            "raygun_mark3",
        ]
    ),
    Maps.Revelations_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "bouncingbetty",
            "ar_accurate",
            "ar_cqb",
            "ar_damage",
            "ar_longburst",
            "ar_marksman",
            "ar_standard",
            "ar_peacekeeper",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "pistol_energy",
            "shotgun_energy",
            "shotgun_fullauto",
            "shotgun_precision",
            "shotgun_semiauto",
            "launcher_standard",
            "smg_capacity",
            "smg_fastfire",
            "smg_standard",
            "smg_thompson",
            "smg_versatile",
            "sniper_fastbolt",
            "sniper_fastsemi",
            "sniper_powerbolt",
        ],
        expanded = [
            "pistol_standard",
            "bowie_knife",
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_burst",
            "melee_boneglass",
            "melee_improvise",
            "melee_nunchuks",
            "melee_mace",
            "melee_katana",
        ],
        wallbuys = [
            "pistol_burst",
            "smg_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_standard",
            "smg_versatile",
            "smg_fastfire",
            "shotgun_precision",
            "ar_standard",
            "ar_accurate",
            "ar_longburst",
            "ar_cqb",
            #"bowie_knife",
        ],
        special = [
            "ray_gun",
            "thundergun",
            "hero_gravityspikes_melee",
            "octobomb",
            "idgun_genesis_0",
        ]
    ),
    Maps.The_Giant_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "ar_accurate",
            "ar_cqb",
            "ar_damage",
            "ar_marksman",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "shotgun_fullauto",
            "shotgun_precision",
            "shotgun_semiauto",
            "launcher_standard",
            "smg_burst",
            "smg_capacity",
            "smg_versatile",
            "sniper_fastbolt",
            "sniper_fastsemi",
            "sniper_powerbolt",
            "lmg_rpk",
        ],
        expanded = [
            "pistol_standard",
            "bouncingbetty",
            "bowie_knife",
            "ar_longburst",
            "ar_standard",
            "pistol_burst",
            "pistol_fullauto",
            "shotgun_pump",
            "smg_fastfire",
            "smg_standard",
        ],
        wallbuys = [
            "ar_longburst",
            "ar_cqb",
            "ar_standard",
            "bowie_knife",
            "pistol_burst",
            "smg_versatile",
            "shotgun_pump",
            "smg_standard",
            "pistol_fullauto",
        ],
        special = [
            "cymbal_monkey",
            "ray_gun",
            "tesla_gun",
        ]
    ),
    Maps.Kino_Map_String: WeaponLists(
        table = "vanilla",
        vanilla = [
            "ar_accurate",
            "ar_cqb",
            "ar_damage",
            "ar_famas",
            "ar_galil",
            "ar_longburst",
            "ar_m16",
            "ar_marksman",
            "ar_standard",
            "lmg_cqb",
            "lmg_heavy",
            "lmg_light",
            "lmg_slowfire",
            "pistol_fullauto",
            "shotgun_fullauto",
            "shotgun_precision",
            "shotgun_pump",
            "shotgun_semiauto",
            "launcher_standard",
            "smg_burst",
            "smg_capacity",
            "smg_fastfire",
            "smg_standard",
            "smg_versatile",
            "smg_mp40_1940",
            "smg_ak74u",
            "sniper_fastsemi",
            "sniper_powerbolt",
            "lmg_rpk",
            "ar_m14",
        ],
        expanded = [
            "pistol_standard",
            "pistol_m1911",
            "bouncingbetty",
            "bowie_knife",
            "pistol_burst",
        ],
        wallbuys = [
            "pistol_burst",
            "smg_burst",
            "ar_standard",
            "smg_mp40_1940",
            "pistol_fullauto",
            "smg_fastfire",
            "ar_accurate",
            "smg_versatile",
            "shotgun_precision",
            "ar_longburst",
            "bowie_knife",
        ],
        special = [
            "cymbal_monkey",
            "thundergun",
            "ray_gun",
            "raygun_mark2",
            "tesla_gun",
            "hero_annihilator",
        ]
    ),
    Maps.Wanted_Map_String: WeaponLists(
        table = "zm_westernz",
        vanilla = [
            "t8_crossbow",
            "bo3_boneglass",
            "t8_allistair_annihalator",
            "m1831",
            "bo3_olympia",
            "henry_m1840",
            "w1887",
            "t8_m1897",
            "ww2_model21",
            "ww2_winchester94",
            "w1892",
            "fc4_m1887_long",
            "lebel_m1811",
            "ww2_lewis",
            "ww2_fliegerfaust",
            "wes_jag42",
            "m1827_exp",
        ],
        expanded = [
            # "frag_ww2_molotov",
            "ww2_raven",
            "ww2_iceaxe",
            "bowie_knife",
            "t8_welling",
            "ww2_reichsrevolver",
            "ww2_colt45saa",
            "ww2_enfield2",
            "ww2_enfield2_gold",
            "ww2_m712",
            "m1889",
            "mwr_ranger",
            "m1903_epic",
            "ww2_mosin",
            "m1896_essex",
            "doc_w1866",
            "aw_winchester",
            "ww2_crossbow",
            "ww2_ribeyrolles",
            "bo4_escargot",
        ],
        wallbuys = [
            "ww2_winchester94",
            "bo4_escargot",
            "ww2_ribeyrolles",
            "m1903_epic",
            "m1889",
            "mwr_ranger",
        ],
        special = [
            "frag_ww2_dynamite",
            "grenade_homunculus",
            "thundergun",
            "t8_shotgun_blundergat",
            "t8_raygun",
            "tesla_gun",
        ]
    ),
}

def special_weapon_name(map: str, itemname: str):
    if itemname.startswith("("):
        return itemname
    return map + " " + itemname

def get_weapon_with_vanilla_fallback(weapon_name: str, table: str, map_name = "", special = 0) -> WeaponData | None:
    # Try the specified table first
    weapon = weapon_data_set[table].get(weapon_name)
    if weapon:
        if special:
            return weapon._replace(item_name = special_weapon_name(map_name, weapon.item_name))
        return weapon
    
    # Try vanilla table as fallback
    weapon = weapon_data_set['vanilla'].get(weapon_name)
    if weapon:
        if special:
            return weapon._replace(item_name = special_weapon_name(map_name, weapon.item_name))
        return weapon
    
    # Not found anywhere
    print(f"Warning: Weapon '{weapon_name}' not found in table '{table}' or 'vanilla'")
    return None

map_weapon_data_sets: dict[str, WeaponDataLists] = {
    map_name: WeaponDataLists(
        table = weapon_list.table,
        vanilla = {
            weapon_name: weapon_data
            for weapon_name in weapon_list.vanilla
            if (weapon_data := get_weapon_with_vanilla_fallback(weapon_name, weapon_list.table)) is not None
        },
        expanded = {
            weapon_name: weapon_data
            for weapon_name in weapon_list.expanded
            if (weapon_data := get_weapon_with_vanilla_fallback(weapon_name, weapon_list.table)) is not None
        },
        wallbuys = {
            weapon_name: weapon_data
            for weapon_name in weapon_list.wallbuys
            if (weapon_data := get_weapon_with_vanilla_fallback(weapon_name, weapon_list.table)) is not None
        },
        special = {
            weapon_name: weapon_data
            for weapon_name in weapon_list.special
            if (weapon_data := get_weapon_with_vanilla_fallback(weapon_name, weapon_list.table, map_name, 1)) is not None
        },
    )
    for map_name, weapon_list in map_weapon_lists.items()
}

def get_map_special_weapons_itemnames(map):
    if map in map_weapon_data_sets:
        return [map_weapon_data_sets[map].special[weapon_key].item_name for weapon_key in map_weapon_data_sets[map].special]
    return []

def add_wallbuy_weapon_items(enabled_items: list[str], seen: set, map: str):
    if map in map_weapon_data_sets:
        weapon_data_set = map_weapon_data_sets[map]
        weapon_list = weapon_data_set.wallbuys

        for weapon_key, weapon_data in weapon_list.items():
            if weapon_data.item_name not in seen:
                enabled_items.append(weapon_data.item_name)
                seen.add(weapon_data.item_name)

def add_mystery_box_weapon_items(enabled_items: list[str], seen: set, map: str, expanded_mystery_box):
    if map in map_weapon_data_sets:
        weapon_data_set = map_weapon_data_sets[map]
        weapon_list = {}
        if expanded_mystery_box:
            weapon_list = {**weapon_data_set.vanilla, **weapon_data_set.expanded}
        else:
            weapon_list = weapon_data_set.vanilla

        for weapon_key, weapon_data in weapon_list.items():
            if weapon_data.item_name not in seen:
                enabled_items.append(weapon_data.item_name)
                seen.add(weapon_data.item_name)

class WeaponDistribution:
    # Number of weapons we want available on each map at the start, per strength
    num_of_group: list[int] = [0,0,0,0,0]
