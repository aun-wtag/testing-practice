import pytest
from features import add
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

