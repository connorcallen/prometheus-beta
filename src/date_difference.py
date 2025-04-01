from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime): First date, either as a datetime object or 
                                 a string in 'YYYY-MM-DD' format
        date2 (str or datetime): Second date, either as a datetime object or 
                                 a string in 'YYYY-MM-DD' format

    Returns:
        int: Absolute number of days between the two dates

    Raises:
        ValueError: If dates are in an invalid format or cannot be parsed
        TypeError: If input is not a string or datetime object
    """
    # Convert inputs to datetime objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError(f"Invalid date format for date1: {date1}. Use YYYY-MM-DD.")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError(f"Invalid date format for date2: {date2}. Use YYYY-MM-DD.")
    
    # Validate input types
    if not (hasattr(date1, 'date') and hasattr(date2, 'date')):
        raise TypeError("Inputs must be datetime or date objects, or strings in YYYY-MM-DD format")
    
    # Calculate and return absolute number of days
    return abs((date2 - date1).days)