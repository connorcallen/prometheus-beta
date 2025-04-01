import pytest
from src.word_count import count_words

def test_basic_word_count():
    """Test basic word counting functionality."""
    assert count_words("Hello world") == 2
    assert count_words("One") == 1
    assert count_words("") == 0

def test_multiple_spaces():
    """Test word counting with multiple spaces."""
    assert count_words("  Hello   world  ") == 2
    assert count_words("  Spaces   around   words  ") == 3

def test_edge_cases():
    """Test edge cases and different input types."""
    assert count_words(None) == 0
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_mixed_input_types():
    """Test function with different input types."""
    assert count_words(123) == 1  # Non-string inputs are converted
    assert count_words(["Hello", "world"]) == 1  # Lists convert to strings