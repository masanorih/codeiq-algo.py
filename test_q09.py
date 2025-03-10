import pytest
from q09 import main


@pytest.mark.timeout(60)
def test_main():
    r = main()
    assert r == 9
