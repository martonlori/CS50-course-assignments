import pytest
from bank import value

def test_lower():
    assert value("hello") == 0
    assert value("bello") == 100

def test_upper():
    assert value("HELLO") == 0
    assert value("BELLO") == 100

def test_no_input():
    assert value("") == 100

def test_sentence():
    assert value("Hello there!") == 0
