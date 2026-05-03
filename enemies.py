import json
from gameclasses import Character

ENEMY_TEMPLATES = {
    "Raft": {
        "max_hp": 5,
        "health": 5,
        "attack": 3,
        "defense": 1,
        "speed": 20,
        "current_location": "Ocean",
        "gold": 8
    },
    "Little Boat": {
        "max_hp": 15,
        "health": 15,
        "attack": 8,
        "defense": 4,
        "speed": 15,
        "current_location": "Ocean",
        "gold": 18
    },
    "Pirate Ship": {
        "max_hp": 50,
        "health": 50,
        "attack": 15,
        "defense": 13,
        "speed": 10,
        "current_location": "Ocean",
        "gold": 40
    },
    "Pirate Ship (Well-Armed)": {
        "max_hp": 50,
        "health": 50,
        "attack": 22,
        "defense": 11,
        "speed": 12,
        "current_location": "Ocean",
        "gold": 50
    },
    "Pirate Ship (Fortified)": {
        "max_hp": 70,
        "health": 70,
        "attack": 12,
        "defense": 25,
        "speed": 5,
        "current_location": "Ocean",
        "gold": 80
    },
    "Pirate Ship (Nimble)": {
        "max_hp": 40,
        "health": 40,
        "attack": 10,
        "defense": 8,
        "speed": 40,
        "current_location": "Ocean",
        "gold": 40
    },
    "Deserted Ship": {
        "max_hp": 50,
        "health": 50,
        "attack": 0,
        "defense": 13,
        "speed": 10,
        "current_location": "Ocean",
        "gold": 75
    },
    "💀 The Kraken": {
        "max_hp": 150,
        "health": 150,
        "attack": 35,
        "defense": 20,
        "speed": 20,
        "current_location": "Ocean",
        "gold": 250
    }
}

def create_enemy(name):
    stats = ENEMY_TEMPLATES[name]
    return Character(name, **stats)