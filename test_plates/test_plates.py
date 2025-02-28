import pytest
from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAAAAAA") == False

def test_start():
    assert is_valid("1ABC") == False
    assert is_valid("2XZY") == False
    assert is_valid("AB123") == True
    assert is_valid("!@#ABC") == False
    assert is_valid("123ABC") == False
    assert is_valid("A1234") == False
    assert is_valid("A1BC") == False


def test_ending():
    assert is_valid("AA00A") == False
    assert is_valid("AAAA11") == True
    assert is_valid("AB012") == False
    assert is_valid("AB1C2D") == False

def test_special():
    assert is_valid("AAAA2.") == False

