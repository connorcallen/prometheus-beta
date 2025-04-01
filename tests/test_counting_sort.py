import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting of positive integers"""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_counting_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_counting_sort_with_zeros():
    """Test sorting with zeros"""
    assert counting_sort([0, 3, 0, 2, 1]) == [0, 0, 1, 2, 3]

def test_invalid_input_non_list():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_invalid_input_non_integers():
    """Test handling of non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, 'a', 3])

def test_invalid_input_negative_numbers():
    """Test handling of negative numbers"""
    with pytest.raises(ValueError, match="Input cannot contain negative numbers"):
        counting_sort([1, -1, 2, 3])

def test_large_range_numbers():
    """Test sorting with a wide range of numbers"""
    input_list = [100, 3, 2, 1000, 10, 50]
    assert counting_sort(input_list) == [2, 3, 10, 50, 100, 1000]

def test_duplicate_numbers():
    """Test sorting with many duplicate numbers"""
    assert counting_sort([5, 5, 5, 3, 3, 1, 1, 1]) == [1, 1, 1, 3, 3, 5, 5, 5]