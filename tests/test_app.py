# tests/test_app.py
from app import multiply

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative_and_zero():
    assert multiply(-1, 5) == -5
    assert multiply(0, 123) == 0

def test_multiply_commutative():
    assert multiply(7, 8) == multiply(8, 7)
