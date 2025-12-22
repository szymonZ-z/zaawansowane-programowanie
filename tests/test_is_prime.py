from funkcje import is_prime

def test_2():
    assert is_prime(2) == True

def test_3():
    assert is_prime(3) == True

def test_4():
    assert is_prime(4) == False

def test_0():
    assert is_prime(0) == False

def test_1():
    assert is_prime(1) == False

def test_5():
    assert is_prime(5) == True

def test_97():
    assert is_prime(97) == True
