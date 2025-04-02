import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file.

    Args:
        file_path (str): Path to the file whose owner needs to be retrieved.

    Returns:
        str: Username of the file owner.

    Raises:
        TypeError: If file_path is not a string.
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there's no permission to access file metadata.
    """
    # Type checking
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Validate file path
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        # Get file stats
        file_stats = os.stat(file_path)
        
        # Get owner's user ID
        owner_uid = file_stats.st_uid
        
        # Convert user ID to username
        owner_name = pwd.getpwuid(owner_uid).pw_name
        
        return owner_name
    
    except PermissionError:
        raise PermissionError(f"Permission denied to access metadata for {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file owner: {str(e)}")