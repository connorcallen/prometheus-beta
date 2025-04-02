import pytest
from src.find_primes import find_primes_below_n

def test_find_primes_below_n():
    # Test basic functionality
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(2) == []
    assert find_primes_below_n(3) == [2]
    
    # Test larger range
    large_primes = find_primes_below_n(30)
    assert large_primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # Test edge cases
    assert find_primes_below_n(1) == []
    assert find_primes_below_n(0) == []
    
    # Test type and value errors
    with pytest.raises(TypeError):
        find_primes_below_n("not a number")
    
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)
    
    # Test a larger range to ensure performance
    result = find_primes_below_n(100)
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert result == expected_primes