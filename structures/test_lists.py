"""a test suite for lists.py"""
from structures.lists import evens_only
from structures.lists import last_of_four_digits
from structures.lists import round_up
from structures.lists import find_negative

def test_evens_only():
    """verify evens_only()"""
    test = [5, 8, 17, 21, 15, 0, 6]
    result = evens_only(test)

    assert result[0] == 8
    assert result[1] == 0
    assert result[2] == 6
    assert len(result) == 3

    second = [0, 2, 4, 7, 8, 11]
    result = evens_only(second)

    assert result[0] == 0
    assert result[1] == 2
    assert result[2] == 4
    assert result[3] == 8
    assert len(result) == 4

def test_last_of_four_digits():
    """verify last_of_four_digits()"""
    test = [1200, 4343, 1789, 1897]
    result = last_of_four_digits(test)

    assert result[0] == 0
    assert result[1] == 3
    assert result[2] == 9
    assert result[3] == 7
    assert len(result) == 4

    second = [3333, 1777, 4587, 6500, 1999]
    result = last_of_four_digits(second)

    assert result[0] == 3
    assert result[1] == 7
    assert result[2] == 7
    assert result[3] == 0
    assert result[4] == 9
    assert len(result) == 5

def test_round_up():
    """verify round_up()"""
    test = [1.2, 0.4, 7.6, 8.9, 9.1]
    result = round_up(test)

    assert result[0] == 1
    assert result[1] == 0
    assert result[2] == 8
    assert result[3] == 9
    assert result[4] == 9

    second = [0.5, 1.2]
    result = round_up(second)

    assert result[0] == 1
    assert result[1] == 1

def test_find_negative():
    """verify find_negative()"""
    test = [2, 0, 4, 16]
    result = find_negative(test)

    assert result == -1

    second = [0, 13, 3, -4, 7, 11]
    result = find_negative(second)

    assert result == 3

def every_other():
    test = [1, 2, 3, 4, 5, 6]
    result = every_other(test)

    assert result == [1, 3, 5,]