import pytest
import sys
from io import StringIO
from colorama import Fore
from src.colored_logger import log_colored_message

def test_log_colored_message_default():
    """Test default green color logging."""
    captured_output = StringIO()
    sys.stdout = captured_output
    
    log_colored_message("Test message")
    sys.stdout = sys.__stdout__
    
    assert Fore.GREEN in captured_output.getvalue()
    assert "Test message" in captured_output.getvalue()

def test_log_colored_message_all_colors():
    """Test logging with all supported colors."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN
    }
    
    for color in colors:
        captured_output = StringIO()
        sys.stdout = captured_output
        
        log_colored_message("Test message", color)
        sys.stdout = sys.__stdout__
        
        assert color_map[color] in captured_output.getvalue()
        assert "Test message" in captured_output.getvalue()

def test_log_colored_message_case_insensitive():
    """Test color name case insensitivity."""
    captured_output = StringIO()
    sys.stdout = captured_output
    
    log_colored_message("Test message", "RED")
    sys.stdout = sys.__stdout__
    
    assert Fore.RED in captured_output.getvalue()
    assert "Test message" in captured_output.getvalue()

def test_log_colored_message_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Unsupported color"):
        log_colored_message("Test message", "purple")