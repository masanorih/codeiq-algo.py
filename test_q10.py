import pytest
from q10 import main, get_maxsum


@pytest.mark.timeout(30)
def test_main():
    r = main()
    assert r == 9


@pytest.mark.timeout(2)
def test_get_maxsum():
    r = get_maxsum(3, [1, 2, 3, 0, 1])
    assert r[0] == [1, 2, 3]
    assert r[1] == [2, 3, 0]
    assert r[2] == [3, 0, 1]
    assert r[3] == [0, 1, 1]
