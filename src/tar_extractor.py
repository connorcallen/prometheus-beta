import os
import tarfile
from typing import Union, List, Optional


def extract_tar_archive(
    tar_path: str, 
    extract_path: Optional[str] = None, 
    specific_files: Optional[Union[str, List[str]]] = None
) -> List[str]:
    """
    Extract files from a tar archive with flexible options.

    Args:
        tar_path (str): Path to the tar archive file.
        extract_path (str, optional): Directory to extract files to. 
            If not provided, extracts to the same directory as the tar file.
        specific_files (str or List[str], optional): Specific file(s) to extract.
            Can be a single filename or a list of filenames.

    Returns:
        List[str]: Paths of the extracted files.

    Raises:
        FileNotFoundError: If the tar archive does not exist.
        ValueError: If the tar_path is not a valid tar file.
        PermissionError: If there are insufficient permissions to extract.
    """
    # Validate input
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar archive not found: {tar_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(tar_path) or '.'
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)
    
    # Normalize specific_files to a list
    if specific_files is None:
        specific_files = []
    elif isinstance(specific_files, str):
        specific_files = [specific_files]
    
    # List to store extracted file paths
    extracted_files = []
    
    try:
        # Open the tar archive
        with tarfile.open(tar_path, 'r:*') as tar:
            # Validate tar file
            if not tar.getmembers():
                raise ValueError("The tar archive is empty.")
            
            # If no specific files are specified, extract all
            if not specific_files:
                tar.extractall(path=extract_path)
                extracted_files = [
                    os.path.join(extract_path, member.name) 
                    for member in tar.getmembers() 
                    if member.isfile()
                ]
            else:
                # Extract only specified files
                for filename in specific_files:
                    try:
                        tar.extract(filename, path=extract_path)
                        extracted_files.append(os.path.join(extract_path, filename))
                    except KeyError:
                        # Skip files not found in the archive
                        print(f"Warning: File {filename} not found in the archive.")
    
    except tarfile.TarError as e:
        raise ValueError(f"Invalid tar file: {e}")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract to {extract_path}")
    
    return extracted_files