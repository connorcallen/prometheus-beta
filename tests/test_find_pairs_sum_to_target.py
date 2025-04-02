import pytest
from src.find_pairs_sum_to_target import find_pairs_sum_to_target

def test_basic_pairs():
    """Test finding basic pairs that sum to target"""
    numbers = [1, 2, 3, 4, 5]
    target = 7
    expected = [(2, 5), (3, 4)]
    assert set(find_pairs_sum_to_target(numbers, target)) == set(expected)

def test_multiple_ways_to_sum():
    """Test list with multiple ways to reach the target"""
    numbers = [2, 3, 4, 4, 5, 6]
    target = 8
    expected = [(2, 6), (3, 5)]
    assert set(find_pairs_sum_to_target(numbers, target)) == set(expected)

def test_no_pairs():
    """Test when no pairs sum to target"""
    numbers = [1, 2, 3, 4, 5]
    target = 10
    assert find_pairs_sum_to_target(numbers, target) == []

def test_duplicate_numbers():
    """Test handling of duplicate numbers"""
    numbers = [3, 3, 3, 3]
    target = 6
    expected = [(3, 3)]
    assert set(find_pairs_sum_to_target(numbers, target)) == set(expected)

def test_float_numbers():
    """Test with floating point numbers"""
    numbers = [1.5, 2.5, 3.0, 4.0]
    target = 5.5
    expected = [(1.5, 4.0), (2.5, 3.0)]
    assert set(find_pairs_sum_to_target(numbers, target)) == set(expected)

def test_invalid_input_list():
    """Test invalid list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_pairs_sum_to_target("not a list", 10)

def test_invalid_target():
    """Test invalid target type"""
    with pytest.raises(TypeError, match="Target must be a numeric value"):
        find_pairs_sum_to_target([1, 2, 3], "not a number")

def test_invalid_number_in_list():
    """Test invalid number in the input list"""
    with pytest.raises(ValueError, match="Invalid number in input list"):
        find_pairs_sum_to_target([1, 2, "invalid"], 10)

def test_empty_list():
    """Test with an empty list"""
    assert find_pairs_sum_to_target([], 10) == []