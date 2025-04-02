import os
import shutil

def delete_empty_directory(directory_path):
    """
    Delete an empty directory.

    Args:
        directory_path (str): Path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory is not empty or cannot be deleted.
        ValueError: If the path is not a directory.

    Returns:
        bool: True if the directory was successfully deleted.
    """
    # Validate input is a string
    if not isinstance(directory_path, str):
        raise TypeError("Directory path must be a string")

    # Normalize the path to handle different path formats
    directory_path = os.path.normpath(directory_path)

    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory does not exist: {directory_path}")

    # Check if it's actually a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"Path is not a directory: {directory_path}")

    # Check if directory is empty
    if os.listdir(directory_path):
        raise OSError(f"Directory is not empty: {directory_path}")

    try:
        # Remove the empty directory
        os.rmdir(directory_path)
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete directory {directory_path}")
    except Exception as e:
        raise OSError(f"Could not delete directory: {e}")