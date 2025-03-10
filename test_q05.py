import pytest
from q05 import main

@pytest.mark.timeout(2)
def test_main():
    r = main()
    assert r == 20
