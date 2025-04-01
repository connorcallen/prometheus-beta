import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"

def test_remove_duplicates_empty_string():
    """Test handling of an empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicates_preserve_order():
    """Ensure original order of first occurrence is preserved."""
    assert remove_duplicate_chars("cabbage") == "cabge"

def test_remove_duplicates_mixed_case():
    """Test handling of mixed case characters."""
    assert remove_duplicate_chars("AaBbCc") == "AaBbCc"

def test_remove_duplicates_special_chars():
    """Test with special characters and spaces."""
    assert remove_duplicate_chars("a!b@c#a") == "a!b@c#"

def test_remove_duplicates_invalid_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(None)