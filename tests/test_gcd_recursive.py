import pytest
from src.gcd_recursive import recursive_gcd

def test_recursive_gcd_basic():
    """Test basic GCD calculations"""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(17, 5) == 1

def test_recursive_gcd_zero():
    """Test GCD with zero inputs"""
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5

def test_recursive_gcd_negative():
    """Test GCD with negative inputs"""
    assert recursive_gcd(-48, 18) == 6
    assert recursive_gcd(48, -18) == 6
    assert recursive_gcd(-48, -18) == 6

def test_recursive_gcd_same_number():
    """Test GCD when both inputs are the same"""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(13, 13) == 13

def test_recursive_gcd_one_input_one():
    """Test GCD when one input is 1"""
    assert recursive_gcd(1, 5) == 1
    assert recursive_gcd(5, 1) == 1

def test_recursive_gcd_error_cases():
    """Test error handling"""
    # Both inputs zero
    with pytest.raises(ValueError, match="GCD is undefined when both inputs are 0"):
        recursive_gcd(0, 0)
    
    # Non-integer inputs
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd(3.14, 5)
    
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd(5, "10")