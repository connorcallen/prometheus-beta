import pytest
from src.find_median import find_median

def test_median_odd_length_list():
    """Test median for a list with odd number of elements"""
    assert find_median([1, 3, 5]) == 3
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([5, 3, 1]) == 3  # unsorted input

def test_median_even_length_list():
    """Test median for a list with even number of elements"""
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([2, 4, 6, 8]) == 5
    assert find_median([8, 6, 4, 2]) == 5  # unsorted input

def test_single_element_list():
    """Test median for a list with a single element"""
    assert find_median([42]) == 42

def test_float_inputs():
    """Test median with float inputs"""
    assert find_median([1.5, 2.5, 3.5]) == 2.5
    assert find_median([1.0, 2.0, 3.0, 4.0]) == 2.5

def test_error_empty_list():
    """Test that ValueError is raised for an empty list"""
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_error_non_list_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median("not a list")

def test_error_non_numeric_input():
    """Test that TypeError is raised for lists with non-numeric elements"""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, 2, "three"])
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, 2, None])