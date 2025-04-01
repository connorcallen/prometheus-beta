import re
import time
from datetime import datetime
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
    Test that the function returns the current time.
    """
    # Get current datetime 
    current_datetime = datetime.now()
    
    # Get formatted time from function
    time_str = get_current_time_formatted()
    
    # Check that the time components match current datetime
    assert (current_datetime.hour == int(time_str.split(':')[0]) and
            current_datetime.minute == int(time_str.split(':')[1]) and
            current_datetime.second == int(time_str.split(':')[2])), \
            "Time function did not return current time"

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