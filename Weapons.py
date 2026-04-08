from typing import NamedTuple
from .Names import ItemName

class WeaponData(NamedTuple):
    name: str
    category: str
    strength: int

weapon_data_set: list[WeaponData] = [
    # Assault Rifles
    WeaponData(ItemName.Weapon_ICR, "ar", 4),
    WeaponData(ItemName.Weapon_HVK, "ar", 4),
    WeaponData(ItemName.Weapon_ManoWar, "ar", 4),
    WeaponData(ItemName.Weapon_M8A7, "ar", 2),
    WeaponData(ItemName.Weapon_Sheiva, "ar", 1),
    WeaponData(ItemName.Weapon_KN44, "ar", 3),
    WeaponData(ItemName.Weapon_FFAR, "ar", 3),
    WeaponData(ItemName.Weapon_Garand, "ar", 1),
    WeaponData(ItemName.Weapon_Peacekeeper, "ar", 3),
    WeaponData(ItemName.Weapon_AN94, "ar", 2),
    WeaponData(ItemName.Weapon_Galil, "ar", 2),
    WeaponData(ItemName.Weapon_M14, "ar", 1),
    WeaponData(ItemName.Weapon_M16, "ar", 4),
    WeaponData(ItemName.Weapon_Basilisk, "ar", 0),
    WeaponData(ItemName.Weapon_XR2, "ar", 0),
    WeaponData(ItemName.Weapon_STG44, "ar", 2),
    
    # Light Machine Guns
    WeaponData(ItemName.Weapon_Dingo, "lmg", 4),
    WeaponData(ItemName.Weapon_Dredge, "lmg", 3),
    WeaponData(ItemName.Weapon_BRM, "lmg", 2),
    WeaponData(ItemName.Weapon_Gorgon, "lmg", 1),
    WeaponData(ItemName.Weapon_R70Ajax, "lmg", 3),
    WeaponData(ItemName.Weapon_RPK, "lmg", 4),
    WeaponData(ItemName.Weapon_MG08, "lmg", 3),
    
    # Sub Machine Guns
    WeaponData(ItemName.Weapon_Pharo, "smg", 1),
    WeaponData(ItemName.Weapon_Weevil, "smg", 1),
    WeaponData(ItemName.Weapon_Vesper, "smg", 2),
    WeaponData(ItemName.Weapon_Kuda, "smg", 2),
    WeaponData(ItemName.Weapon_VMP, "smg", 3),
    WeaponData(ItemName.Weapon_Bootlegger, "smg", 3),
    WeaponData(ItemName.Weapon_HG40, "smg", 3),
    WeaponData(ItemName.Weapon_PPSH, "smg", 3),
    WeaponData(ItemName.Weapon_M1927, "smg", 0),
    WeaponData(ItemName.Weapon_Razorback, "smg", 4),
    WeaponData(ItemName.Weapon_AK47u, "smg", 4),
    WeaponData(ItemName.Weapon_MSMC, "smg", 3), # ?
    WeaponData(ItemName.Weapon_Nailgun, "smg", 3), # ?
    WeaponData(ItemName.Weapon_HLX4, "smg", 3), # ?
    WeaponData(ItemName.Weapon_Sten, "smg", 2),
    WeaponData(ItemName.Weapon_MP40, "smg", 2),
    
    # Snipers
    WeaponData(ItemName.Weapon_Drakon, "sniper", 4),
    WeaponData(ItemName.Weapon_Locus, "sniper", 3),
    WeaponData(ItemName.Weapon_SVG, "sniper", 1),
    
    # Shotguns
    WeaponData(ItemName.Weapon_Haymaker, "shotgun", 4),
    WeaponData(ItemName.Weapon_Argus, "shotgun", 2),
    WeaponData(ItemName.Weapon_KRM, "shotgun", 1),
    WeaponData(ItemName.Weapon_Brecci, "shotgun", 4),
    WeaponData(ItemName.Weapon_Banshii, "shotgun", 1),
    WeaponData(ItemName.Weapon_Olympia, "shotgun", 1),
    
    # Pistols
    WeaponData(ItemName.Weapon_Bloodhound, "pistol", 1),
    WeaponData(ItemName.Weapon_MR6, "pistol", 1),
    WeaponData(ItemName.Weapon_RK5, "pistol", 2),
    WeaponData(ItemName.Weapon_LCAR, "pistol", 1),
    WeaponData(ItemName.Weapon_RiftE9, "pistol", 1),
    WeaponData(ItemName.Weapon_M1911, "pistol", 1),
    WeaponData(ItemName.Weapon_Marshal16, "pistol", 3),
    WeaponData(ItemName.Weapon_MauserC96, "pistol", 1),
    
    # Melee
    # WeaponData(ItemName.Weapon_BowieKnife, "melee", 0),
    
    # Wonder Weapons / Other
    WeaponData(ItemName.Weapon_Raygun, "wonder", 2),
    WeaponData(ItemName.Weapon_RaygunMk2, "wonder", 4),
    WeaponData(ItemName.Weapon_RaygunMk3, "wonder", 5),
    WeaponData(ItemName.Weapon_Wunderwaffe, "wonder", 4),
    WeaponData(ItemName.Weapon_ApothiconServant, "wonder", 5),
    WeaponData(ItemName.Weapon_KT4, "wonder", 4),
    WeaponData(ItemName.Weapon_Thundergun, "wonder", 4),
    WeaponData(ItemName.Weapon_Ragnaroks, "wonder", 5),
    WeaponData(ItemName.Weapon_MonkeyBombs, "wonder", 4),
    WeaponData(ItemName.Weapon_LilArnies, "wonder", 5),
]

class WeaponDistribution:
    # Average percentage taken from 0% to 100% of each category 
    percent_of_group: list[int] = [0,0,0,0,0]
    # How much to fuzz the boundaries when choosing a weapon to award
    fuzz_strength = 10
    # Do not allow fuzzing to exceed this strength
    fuzz_max: int = 3