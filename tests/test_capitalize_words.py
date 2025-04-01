import pytest
from src.capitalize_words import capitalize_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_words("hello world") == "Hello World"

def test_already_capitalized():
    """Test string with some words already capitalized."""
    assert capitalize_words("Hello world") == "Hello World"

def test_multiple_spaces():
    """Test string with multiple spaces between words."""
    assert capitalize_words("hello   world") == "Hello World"

def test_leading_trailing_spaces():
    """Test string with leading and trailing spaces."""
    assert capitalize_words("  hello world  ") == "Hello World"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_single_word():
    """Test single word capitalization."""
    assert capitalize_words("hello") == "Hello"

def test_multiple_words():
    """Test multiple word capitalization."""
    assert capitalize_words("hello world python programming") == "Hello World Python Programming"

def test_non_string_input():
    """Test non-string input raises TypeError."""
    with pytest.raises(TypeError):
        capitalize_words(123)

def test_mixed_case_input():
    """Test input with mixed case."""
    assert capitalize_words("hELLo wORLd") == "Hello World"