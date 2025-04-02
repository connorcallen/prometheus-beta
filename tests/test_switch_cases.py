import pytest
from src.switch_cases import switch_cases

def test_switch_cases_basic():
    """Test basic case swapping functionality."""
    assert switch_cases('Hello', 'World') == 'hELLO'
    assert switch_cases('PyTHON', 'code') == 'pYthon'

def test_switch_cases_mixed_case():
    """Test with mixed case inputs."""
    assert switch_cases('aBcDeF', 'xyz') == 'AbCdEf'

def test_switch_cases_empty_first_string():
    """Test with an empty first string."""
    assert switch_cases('', 'anything') == ''

def test_switch_cases_all_upper():
    """Test with an all uppercase input."""
    assert switch_cases('HELLO', 'world') == 'hello'

def test_switch_cases_all_lower():
    """Test with an all lowercase input."""
    assert switch_cases('hello', 'world') == 'HELLO'

def test_switch_cases_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        switch_cases(123, 'string')
    
    with pytest.raises(TypeError):
        switch_cases('string', [1, 2, 3])
    
    with pytest.raises(TypeError):
        switch_cases(None, 'string')