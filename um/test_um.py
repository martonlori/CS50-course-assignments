import pytest
from um import count


def test_no_um():
    assert count("Hello, world!") == 0

def test_substring():
    assert count("Hello world, yummy!") == 0

def test_wrong_umm():
    assert count("hey, ummm..") == 0

def test_case_sensitive():
    assert count("Hey, UM, good q!") == 1

def test_correct_input():
    assert count("Hello, um, um, yummy world!") == 2
