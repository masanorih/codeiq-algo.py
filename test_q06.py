import pytest
from q06 import main

@pytest.mark.timeout(2)
def test_main():
    r = main()
    assert r == 34
