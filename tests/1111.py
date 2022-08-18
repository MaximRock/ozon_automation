import pytest


@pytest.mark.parametrize('number', [1, 2, 100, -2, -4])
def test_add(number):
    assert number > 0
