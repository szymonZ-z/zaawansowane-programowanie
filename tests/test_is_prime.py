from funkcje import is_prime


def test_2():
    assert is_prime(2) is True


def test_3():
    assert is_prime(3) is True


def test_4():
    assert is_prime(4) is False


def test_0():
    assert is_prime(0) is False


def test_1():
    assert is_prime(1) is False


def test_5():
    assert is_prime(5) is True


def test_97():
    assert is_prime(97) is True
