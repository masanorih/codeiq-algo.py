import pytest
from q08 import main

@pytest.mark.timeout(10)
def test_main():
    r = main()
    assert r == 324932
