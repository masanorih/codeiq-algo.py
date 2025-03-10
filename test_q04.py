import pytest
from q04 import main, cutbar

@pytest.mark.timeout(2)
def test_main():
    r = main(20, 3)
    assert r == 8
    # r = main(100, 5)
    # assert r == 22 


@pytest.mark.timeout(2)
def test_cutbar():
    r = cutbar(20, 3, 1)
    assert r == 8
    r = cutbar(100, 5, 1)
    assert r == 22 
