import pytest
from q01 import main, is_kaibun

def test_is_kaibun():
    r = is_kaibun("abccba")
    assert r == True, "abccba は回文"

def test_main():
    r = main()
    assert r == 585
