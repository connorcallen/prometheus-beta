import os
import pytest
import logging
from src.keystroke_logger import KeystrokeLogger

def test_single_keystroke_logging(tmp_path):
    """Test logging a single keystroke"""
    log_file = os.path.join(tmp_path, 'test_keystroke.log')
    logger = KeystrokeLogger(log_file)
    
    logger.log_keystroke('a')
    
    # Read the log file and verify contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert 'Keystroke: a' in log_content

def test_multi_keystroke_logging(tmp_path):
    """Test logging multiple keystrokes"""
    log_file = os.path.join(tmp_path, 'test_multi_keystroke.log')
    logger = KeystrokeLogger(log_file)
    
    logger.log_text('hello')
    
    # Read the log file and verify contents
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert 'Keystroke: h' in log_content
    assert 'Keystroke: e' in log_content
    assert 'Keystroke: l' in log_content
    assert 'Keystroke: o' in log_content

def test_invalid_keystroke_single_input():
    """Test logging invalid single inputs"""
    logger = KeystrokeLogger()
    
    # Test multiple character input
    with pytest.raises(ValueError, match="Only single characters can be logged"):
        logger.log_keystroke('ab')
    
    # Test non-string input
    with pytest.raises(ValueError, match="Keystroke must be a string"):
        logger.log_keystroke(123)

def test_invalid_text_input():
    """Test logging invalid text inputs"""
    logger = KeystrokeLogger()
    
    # Test non-string input
    with pytest.raises(ValueError, match="Input must be a string"):
        logger.log_text(123)

def test_log_file_creation(tmp_path):
    """Test that log file is created when it doesn't exist"""
    log_file = os.path.join(tmp_path, 'nonexistent_dir', 'test_log.log')
    logger = KeystrokeLogger(log_file)
    
    # Ensure the directory is created
    assert os.path.exists(os.path.dirname(log_file))
    
    # Log something to verify no exceptions
    logger.log_keystroke('x')

def test_clear_log(tmp_path):
    """Test clearing the log file"""
    log_file = os.path.join(tmp_path, 'test_clear_log.log')
    logger = KeystrokeLogger(log_file)
    
    # Log some keystrokes
    logger.log_text('hello')
    
    # Clear the log
    logger.clear_log()
    
    # Verify log is empty
    with open(log_file, 'r') as f:
        log_content = f.read()
    
    assert log_content.strip() == ''