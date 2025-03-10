import pytest
from q02 import main

@pytest.mark.timeout(2)
def test_main():
    r = main()
    assert r == [5931]
    # 1000..10000 だと実は1個しかない
