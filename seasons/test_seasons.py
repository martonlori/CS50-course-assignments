import pytest
from seasons import validate, convert

def test_convert():
    assert convert('2000-09-09') == 'Twelve million, eight hundred fifty thousand, five hundred sixty minutes'

def test_validate_format():
    with pytest.raises(SystemExit):
        validate('2000/09/09')
def test_validate_range():
    with pytest.raises(SystemExit):
        validate('3000-09-09')

def test_validate_whitespace():
    with pytest.raises(SystemExit):
        validate('2000 - 09 - 09')

def test_validate_correct():
    assert validate('2000-09-09') == '2000-09-09'
