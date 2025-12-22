from funkcje import flatten_list


def test_normal_list():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_nested_list():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert flatten_list([]) == []


def test_nested_element():
    assert flatten_list([[[1]]]) == [1]


def test_nested_nested():
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
