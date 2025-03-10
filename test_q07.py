import pytest
from q07 import main

@pytest.mark.timeout(2)
def test_main():
    r = main()
    assert r == [
        '19660713',
        '19660905',
        '19770217',
        '19950617',
        '20020505',
        '20130201',
    ]
