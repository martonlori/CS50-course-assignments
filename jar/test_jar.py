import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_negative():
    with pytest.raises(ValueError):
        jar = Jar(-12)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(10)
    assert jar.size == 10

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(13)
    jar.deposit(8)
    jar.withdraw(7)
    assert jar.size == 1

