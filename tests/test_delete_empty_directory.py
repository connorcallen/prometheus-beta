import os
import pytest
import tempfile
import shutil

from src.delete_empty_directory import delete_empty_directory

def test_delete_empty_directory():
    """Test successful deletion of an empty directory."""
    with tempfile.TemporaryDirectory() as temp_parent:
        # Create an empty directory
        empty_dir = os.path.join(temp_parent, 'empty_dir')
        os.mkdir(empty_dir)
        
        # Verify directory exists before deletion
        assert os.path.exists(empty_dir)
        
        # Delete the empty directory
        result = delete_empty_directory(empty_dir)
        
        # Check deletion was successful
        assert result is True
        assert not os.path.exists(empty_dir)

def test_delete_nonexistent_directory():
    """Test deleting a non-existent directory raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as temp_parent:
        nonexistent_dir = os.path.join(temp_parent, 'nonexistent_dir')
        
        with pytest.raises(FileNotFoundError):
            delete_empty_directory(nonexistent_dir)

def test_delete_nonempty_directory():
    """Test deleting a non-empty directory raises OSError."""
    with tempfile.TemporaryDirectory() as temp_parent:
        nonempty_dir = os.path.join(temp_parent, 'nonempty_dir')
        os.mkdir(nonempty_dir)
        
        # Create a file inside the directory
        with open(os.path.join(nonempty_dir, 'file.txt'), 'w') as f:
            f.write('content')
        
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(nonempty_dir)

def test_delete_file_instead_of_directory():
    """Test attempting to delete a file raises ValueError."""
    with tempfile.TemporaryDirectory() as temp_parent:
        file_path = os.path.join(temp_parent, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('content')
        
        with pytest.raises(ValueError, match="Path is not a directory"):
            delete_empty_directory(file_path)

def test_delete_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        delete_empty_directory(123)
    
    with pytest.raises(TypeError):
        delete_empty_directory(None)