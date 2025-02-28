import pytest
from working import convert

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9.00-17.00")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13:00 AM to 9 PM")


def test_wrong_minutes():
    with pytest.raises(ValueError):
        convert("9:66 AM to 5:00 PM")



def test_correct_input():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
