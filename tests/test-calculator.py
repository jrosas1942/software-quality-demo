import pytest
from app.calculator import average

def test_average_normal():
    assert average([2, 4, 6]) == 4

def test_average_single_value():
    assert average([5]) == 5

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])