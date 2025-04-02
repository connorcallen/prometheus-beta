import os
import pytest
import tarfile
import tempfile
import shutil


from src.tar_extractor import extract_tar_archive


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def sample_tar_archive(temp_dir):
    """Create a sample tar archive for testing."""
    # Create some test files
    test_files = {
        'file1.txt': 'Content of file 1',
        'file2.txt': 'Content of file 2',
        'nested/file3.txt': 'Content of nested file'
    }
    
    tar_path = os.path.join(temp_dir, 'sample.tar')
    
    with tarfile.open(tar_path, 'w') as tar:
        for filename, content in test_files.items():
            # Create a temporary file with content
            temp_file_path = os.path.join(temp_dir, filename)
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            with open(temp_file_path, 'w') as f:
                f.write(content)
            
            # Add file to tar
            tar.add(temp_file_path, arcname=filename)
    
    return tar_path


def test_extract_all_files(sample_tar_archive, temp_dir):
    """Test extracting all files from a tar archive."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir)
    
    assert len(extracted_files) == 3
    assert all(os.path.exists(f) for f in extracted_files)
    assert set(os.path.basename(f) for f in extracted_files) == {'file1.txt', 'file2.txt', 'file3.txt'}


def test_extract_specific_files(sample_tar_archive, temp_dir):
    """Test extracting specific files from a tar archive."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir, specific_files='file1.txt')
    
    assert len(extracted_files) == 1
    assert os.path.basename(extracted_files[0]) == 'file1.txt'


def test_extract_multiple_specific_files(sample_tar_archive, temp_dir):
    """Test extracting multiple specific files from a tar archive."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir, 
                                          specific_files=['file1.txt', 'nested/file3.txt'])
    
    assert len(extracted_files) == 2
    assert set(os.path.basename(f) for f in extracted_files) == {'file1.txt', 'file3.txt'}


def test_extract_to_default_directory(sample_tar_archive):
    """Test extracting files to the default directory."""
    original_dir = os.path.dirname(sample_tar_archive)
    extracted_files = extract_tar_archive(sample_tar_archive)
    
    assert len(extracted_files) == 3
    # Check if files are extracted in the same directory as the tar file
    assert all(os.path.dirname(f) in [original_dir] for f in extracted_files)


def test_non_existent_tar_file():
    """Test extracting from a non-existent tar file."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/non/existent/file.tar')


def test_non_existent_specific_file(sample_tar_archive, temp_dir, capfd):
    """Test attempting to extract a non-existent file from the archive."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir, specific_files='non_existent.txt')
    
    # Should return an empty list
    assert len(extracted_files) == 0
    
    # Check captured output for warning
    out, _ = capfd.readouterr()
    assert "Warning: File non_existent.txt not found in the archive." in out


def test_invalid_tar_file(temp_dir):
    """Test extracting from an invalid tar file."""
    # Create an invalid tar file
    invalid_tar_path = os.path.join(temp_dir, 'invalid.tar')
    with open(invalid_tar_path, 'w') as f:
        f.write('This is not a valid tar file')
    
    with pytest.raises(ValueError, match="Invalid tar file"):
        extract_tar_archive(invalid_tar_path)