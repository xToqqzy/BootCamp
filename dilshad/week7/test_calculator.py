from unittes import add


def test_add_positive_numbers():
    assert add(5, 6) == 11
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-5, -5) == -10
    assert add(-4, -1) == -5
