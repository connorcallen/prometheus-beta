import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent")
    assert are_anagrams("rail safety", "fairy tales")
    assert are_anagrams("python", "typhon")

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert are_anagrams("Triangle", "Trailing")
    assert are_anagrams("Debit Card", "Bad Credit")

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert are_anagrams("astronomer", "moon starer")
    assert are_anagrams("a gentleman", "elegant man")

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert not are_anagrams("hello", "world")
    assert not are_anagrams("python", "java")
    assert not are_anagrams("test", "tests")

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "")
    assert not are_anagrams("", "a")
    assert not are_anagrams("a", "")

def test_same_string():
    """Test that a string is an anagram of itself"""
    assert are_anagrams("python", "python")

def test_unicode_characters():
    """Test anagrams with unicode characters"""
    assert are_anagrams("café", "face")
    assert are_anagrams("Σίγουρα", "ασύγκρι")

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "test")
    with pytest.raises(TypeError):
        are_anagrams("test", ["list"])
    with pytest.raises(TypeError):
        are_anagrams(None, "test")