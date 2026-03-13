"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4, -1, 2, 1]

def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_all_negative():
    assert max_subarray_sum([-3, -2, -5, -1]) == -1

def test_single_element_positive():
    assert max_subarray_sum([5]) == 5

def test_single_element_negative():
    assert max_subarray_sum([-5]) == -5

def test_large_negative_then_positive():
    assert max_subarray_sum([-100, 1, 2, 3]) == 6

def test_positive_then_large_negative():
    assert max_subarray_sum([1, 2, 3, -100]) == 6

def test_alternating():
    assert max_subarray_sum([2, -1, 2, -1, 2]) == 4

def test_zeros():
    assert max_subarray_sum([0, 0, 0]) == 0

if __name__ == "__main__":
    pytest.main()
