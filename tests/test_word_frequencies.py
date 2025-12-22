from funkcje import word_frequencies

def test_shekspir():
    assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}

def test_hello():
    assert word_frequencies("Hello, hello!") == {"hello": 2}

def test_empty():
    assert word_frequencies("") == {}

def test_python():
    assert word_frequencies("Python Python python") == {"python": 3}

def test_ignore():
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}
