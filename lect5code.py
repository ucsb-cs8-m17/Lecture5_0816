import math
import pytest

def perimRect(length,width):
    "perimeter of a rectangle"
    return 2 * length + 2 * width

def circumferenceCircle(radius):
    "circumference of a circle"
    return 2 * math.pi * radius

def test_perimRect():
    assert perimRect(4,5)==18

def test_circumferenceCircle():
    assert circumferenceCircle(1)==pytest.approx(6.28318)
