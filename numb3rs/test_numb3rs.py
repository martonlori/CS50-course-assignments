import pytest
from numb3rs import validate


def test_validate_longer():
    assert validate("0.0.0.0.0") == False
    assert validate("0.0.0.0") == True

def test_validate_shorter():
    assert validate("0.0.0") == False
    assert validate("0.0.0.0") == True


def test_validate_string():
    assert validate("cat.0.0.0") == False
    assert validate("0.0.0.0") == True


def test_validate_range():
    assert validate("255.200.266.200") == False
    assert validate("255.255.255.255") == True


def test_validate_format():
    assert validate("0/0/0/0") == False
    assert validate("1.1.1.1") == True


