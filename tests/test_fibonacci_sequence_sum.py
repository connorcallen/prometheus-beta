import pytest
from src.fibonacci_sequence_sum import fibonacci_sequence_sum

def test_fibonacci_sequence_sum_basic():
    """Test basic functionality of the function."""
    assert fibonacci_sequence_sum(1) == 0
    assert fibonacci_sequence_sum(2) == 1
    assert fibonacci_sequence_sum(3) == 2
    assert fibonacci_sequence_sum(5) == 7
    assert fibonacci_sequence_sum(7) == 22

def test_fibonacci_sequence_sum_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum("3")

def test_fibonacci_sequence_sum_large_n():
    """Test the function with larger input values."""
    # Increasing n values to test larger computations
    assert fibonacci_sequence_sum(10) == 88
    assert fibonacci_sequence_sum(15) == 463