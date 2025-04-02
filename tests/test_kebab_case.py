import pytest
from src.kebab_case import to_kebab_case

def test_basic_string_conversion():
    """Test basic string to kebab-case conversion"""
    assert to_kebab_case("Hello World") == "hello-world"

def test_camel_case_conversion():
    """Test conversion of camelCase to kebab-case"""
    assert to_kebab_case("camelCase") == "camel-case"

def test_pascal_case_conversion():
    """Test conversion of PascalCase to kebab-case"""
    assert to_kebab_case("PascalCase") == "pascal-case"

def test_snake_case_conversion():
    """Test conversion of snake_case to kebab-case"""
    assert to_kebab_case("snake_case") == "snake-case"

def test_mixed_case_conversion():
    """Test conversion of mixed case string"""
    assert to_kebab_case("HelloWorld") == "hello-world"

def test_empty_string():
    """Test conversion of empty string"""
    assert to_kebab_case("") == ""

def test_string_with_spaces():
    """Test conversion of string with multiple spaces"""
    assert to_kebab_case("Hello   World") == "hello-world"

def test_string_with_special_characters():
    """Test conversion of string with special characters"""
    assert to_kebab_case("Hello, World!") == "hello-world"

def test_error_handling():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        to_kebab_case(123)
    with pytest.raises(TypeError):
        to_kebab_case(None)

def test_consecutive_capitals():
    """Test conversion with consecutive capital letters"""
    assert to_kebab_case("HTTPRequest") == "http-request"

def test_single_word():
    """Test conversion of a single word"""
    assert to_kebab_case("Hello") == "hello"