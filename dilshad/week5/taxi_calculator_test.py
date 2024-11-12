from A2W5P2 import calculate_fare


def test_checker():
    assert calculate_fare(2) == 7.75
    assert calculate_fare(1.4) == 6.50
    assert calculate_fare(3.6) == 10.5
    assert calculate_fare(7) == 16.5
    assert calculate_fare(5) == 94182147.4  # vanaf hier error
    assert calculate_fare(4 == "obi one kenobi")
    assert calculate_fare(5) == "kip kerrie broodje uit hoogvliet"
