from funkcje import count_vowels

def test_python():
    assert count_vowels("Python") == 2

def test_AEIOUY():
    assert count_vowels("AEIOUY") == 6

def test_bcd():
    assert count_vowels("bcd") == 0

def test_empty():
    assert count_vowels("") == 0

def test_proba_zolwia():
    assert count_vowels("Próba żółwia") == 5
