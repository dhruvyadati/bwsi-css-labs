"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_middle_elements():
    assert two_sum([1, 3, 4, 2], 6) == [2, 3]

def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3]

def test_mixed_positive_negative():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

def test_zeros():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

def test_large_numbers():
    assert two_sum([1000000, 500000, 500000], 1000000) == [1, 2]

def test_two_elements():
    assert two_sum([3, 7], 10) == [0, 1]

def test_no_solution():
    assert two_sum([1, 2, 3], 100) == []

if __name__ == "__main__":
    pytest.main()
