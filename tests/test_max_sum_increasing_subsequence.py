import pytest
from src.max_sum_increasing_subsequence import max_sum_increasing_subsequence

def test_standard_cases():
    assert max_sum_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 187
    assert max_sum_increasing_subsequence([1, 101, 2, 3, 100]) == 106

def test_edge_cases():
    assert max_sum_increasing_subsequence([]) == 0
    assert max_sum_increasing_subsequence([5]) == 5
    assert max_sum_increasing_subsequence([-1, -2, -3]) == -1

def test_all_increasing():
    assert max_sum_increasing_subsequence([1, 2, 3, 4, 5]) == 15

def test_no_increasing_subsequence():
    assert max_sum_increasing_subsequence([5, 4, 3, 2, 1]) == 5

def test_mixed_positive_negative():
    assert max_sum_increasing_subsequence([-2, 10, -5, 20, 15]) == 40

def test_duplicate_elements():
    assert max_sum_increasing_subsequence([1, 1, 1, 1, 1]) == 1

def test_large_range():
    large_input = list(range(1000))
    expected_sum = sum(range(1, 1001))
    assert max_sum_increasing_subsequence(large_input) == expected_sum