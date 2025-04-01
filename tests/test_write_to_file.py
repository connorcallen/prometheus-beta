import os
import pytest

from src.write_to_file import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    """Test successfully writing a string to a file."""
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    write_string_to_file(str(test_file), test_content)
    
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    """Test overwriting an existing file."""
    test_file = tmp_path / "test_file.txt"
    
    # First write
    write_string_to_file(str(test_file), "First content")
    
    # Overwrite
    new_content = "Updated content"
    write_string_to_file(str(test_file), new_content)
    
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == new_content

def test_write_string_to_file_empty_string(tmp_path):
    """Test writing an empty string."""
    test_file = tmp_path / "test_file.txt"
    
    write_string_to_file(str(test_file), "")
    
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""

def test_write_string_to_file_invalid_path_type():
    """Test raising TypeError for invalid file_path type."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    """Test raising TypeError for invalid content type."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("file.txt", 123)

def test_write_string_to_file_empty_path():
    """Test raising ValueError for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")