import pytest
from q03 import main

@pytest.mark.timeout(2)
def test_main():
    r = main()
    assert r == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # 1x1, 2x2, 3x3 ...
