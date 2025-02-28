import pytest
import sys
from lines import line_counter

def test_line_counter(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['lines.py', 'test.py'])
    assert line_counter() == 2
