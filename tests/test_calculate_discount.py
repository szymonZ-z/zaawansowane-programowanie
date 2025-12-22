from funkcje import calculate_discount


def test_100_02():
    assert calculate_discount(100, 0.2) == 80.0


def test_50_0():
    assert calculate_discount(50, 0) == 50.0


def test_200_1():
    assert calculate_discount(200, 1) == 0.0


def test_100_minus01():
    assert calculate_discount(100, -0.1) is ValueError


def test_100_over1():
    assert calculate_discount(100, 1.5) is ValueError
