import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75

def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

