import pytest
from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten("12345") == "12345"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("HELP ME") == "HLP M"
