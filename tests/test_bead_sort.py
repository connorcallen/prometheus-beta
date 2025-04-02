import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bead_sort import bead_sort

def test_bead_sort_empty_list():
    """Test sorting an empty list"""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test sorting a list with a single element"""
    assert bead_sort([5]) == [5]

def test_bead_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == input_list

def test_bead_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert bead_sort(input_list) == [1, 2, 3, 4, 5]

def test_bead_sort_unsorted_list():
    """Test sorting a randomly unsorted list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bead_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bead_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 2]
    assert bead_sort(input_list) == [1, 1, 2, 3, 3, 3]

def test_bead_sort_zero_elements():
    """Test sorting a list with zero elements"""
    input_list = [0, 0, 0, 0]
    assert bead_sort(input_list) == [0, 0, 0, 0]

def test_bead_sort_raises_on_negative_numbers():
    """Test that the function raises a ValueError for negative numbers"""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([-1, 2, 3])

def test_bead_sort_raises_on_non_integers():
    """Test that the function raises a ValueError for non-integer types"""
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([1, 2.5, 3])
    with pytest.raises(ValueError, match="Bead sort only works with non-negative integers"):
        bead_sort([1, "2", 3])