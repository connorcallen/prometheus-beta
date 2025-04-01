import re
import time
from src.current_time import get_current_time_formatted

def test_current_time_format():
    """
    Test that the returned time string matches the HH:MM:SS format.
    """
    # Get the current time string
    time_str = get_current_time_formatted()
    
    # Check that the string matches the HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time_str), \
        f"Time string {time_str} does not match HH:MM:SS format"

def test_current_time_consistency():
    """
    Test that the function returns a reasonable current time.
    Checks that two consecutive calls are close in value.
    """
    # Get first time
    time1 = get_current_time_formatted()
    
    # Wait a short time
    time.sleep(0.1)
    
    # Get second time
    time2 = get_current_time_formatted()
    
    # Ensure times are different (as time is passing)
    assert time1 != time2, "Time function did not update"

def test_current_time_parts():
    """
    Verify that hours, minutes, and seconds are within valid ranges.
    """
    time_str = get_current_time_formatted()
    
    # Split the time string
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Check ranges
    assert 0 <= hours < 24, f"Invalid hours: {hours}"
    assert 0 <= minutes < 60, f"Invalid minutes: {minutes}"
    assert 0 <= seconds < 60, f"Invalid seconds: {seconds}"