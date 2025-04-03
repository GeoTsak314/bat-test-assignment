import pytest
import bat_functions



# Stage 1: Basic Tests & Parametrization

def test_calculate_bat_power():
    assert bat_functions.calculate_bat_power(1) == 42
    assert bat_functions.calculate_bat_power(2) == 84
    assert bat_functions.calculate_bat_power(0) == 0

@pytest.mark.parametrize("distance,expected", [
    (0, 100),
    (5, 75),
    (10, 0),
    (12, 0)
])
def test_signal_strength(distance, expected):
    assert bat_functions.signal_strength(distance) == expected



# Stage 2: Fixtures

@pytest.fixture
def vehicle_data():
    return {
        "batmobile": {"speed": 300, "armor": "high"},
        "batcycle": {"speed": 200, "armor": "medium"}
    }

def test_get_bat_vehicle_known(vehicle_data):
    assert bat_functions.get_bat_vehicle("batmobile") == vehicle_data["batmobile"]
    assert bat_functions.get_bat_vehicle("batcycle") == vehicle_data["batcycle"]

def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError):
        bat_functions.get_bat_vehicle("batplane")



# Stage 3: Mocking External Dependencies 

def test_fetch_joker_info_mock(monkeypatch):
    def mock_response():
        return {"mischief_level": 0, "location": "captured"}

    monkeypatch.setattr(bat_functions, "fetch_joker_info", mock_response)
    result = bat_functions.fetch_joker_info()
    assert result == {"mischief_level": 0, "location": "captured"}
