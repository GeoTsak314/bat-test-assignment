import time



def calculate_bat_power(level):
    return level * 42


def signal_strength(distance_km):
    if distance_km < 10:
        return 100 - distance_km * 5
    return 0


bat_vehicles = {
    "batmobile": {"speed": 300, "armor": "high"},
    "batcycle": {"speed": 200, "armor": "medium"}
}


def get_bat_vehicle(name):
    if name in bat_vehicles:
        return bat_vehicles[name]
    raise ValueError("Unknown vehicle")


def fetch_joker_info():
    time.sleep(1)
    return {"mischief_level": 100, "location": "unknown"}
