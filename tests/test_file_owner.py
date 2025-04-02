import os
import pwd
import pytest
from src.file_owner import get_file_owner

def test_get_file_owner_existing_file(tmp_path):
    """Test retrieving owner of an existing file."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    current_user = pwd.getpwuid(os.getuid()).pw_name
    assert get_file_owner(str(test_file)) == current_user

def test_get_file_owner_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_owner("/path/to/nonexistent/file.txt")

def test_get_file_owner_edge_cases():
    """Test various edge cases for file ownership."""
    # Test with absolute path
    home_dir = os.path.expanduser("~")
    home_owner = get_file_owner(home_dir)
    assert isinstance(home_owner, str)
    assert len(home_owner) > 0

def test_get_file_owner_types():
    """Verify input and output types."""
    with pytest.raises(TypeError):
        get_file_owner(None)  # Non-string input
    
    with pytest.raises(TypeError):
        get_file_owner(123)  # Non-string input