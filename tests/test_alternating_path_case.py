import pytest
from src.alternating_path_case import convert_to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert convert_to_alternating_path_case("hello world") == "hello-World"
    assert convert_to_alternating_path_case("PYTHON PROGRAMMING") == "python-Programming"

def test_multiple_words():
    """Test conversion with multiple words."""
    assert convert_to_alternating_path_case("open AI chat GPT") == "open-Ai-chat-Gpt"
    assert convert_to_alternating_path_case("THE QUICK BROWN fox") == "the-Quick-brown-Fox"

def test_empty_string():
    """Test empty string input."""
    assert convert_to_alternating_path_case("") == ""

def test_single_word():
    """Test single word input."""
    assert convert_to_alternating_path_case("hello") == "hello"
    assert convert_to_alternating_path_case("WORLD") == "world"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert convert_to_alternating_path_case("HelloWorld") == "hello-World"
    assert convert_to_alternating_path_case("openAIchatGPT") == "open-Ai-chat-Gpt"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(None)
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(["hello", "world"])