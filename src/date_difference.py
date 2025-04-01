from datetime import datetime, date

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime or date): First date, either as a datetime object, 
                                         date object, or a string in 'YYYY-MM-DD' format
        date2 (str or datetime or date): Second date, either as a datetime object, 
                                         date object, or a string in 'YYYY-MM-DD' format

    Returns:
        int: Absolute number of days between the two dates

    Raises:
        ValueError: If dates are in an invalid format or cannot be parsed
        TypeError: If input is not a string, datetime, or date object
    """
    # Convert inputs to date objects
    def _to_date(input_date):
        # If already a date, return it
        if isinstance(input_date, date):
            return input_date
        
        # If datetime, return its date
        if isinstance(input_date, datetime):
            return input_date.date()
        
        # If string, parse it
        if isinstance(input_date, str):
            try:
                return datetime.strptime(input_date, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError(f"Invalid date format: {input_date}. Use YYYY-MM-DD.")
        
        # If not a recognized type, raise TypeError
        raise TypeError("Inputs must be datetime, date objects, or strings in YYYY-MM-DD format")
    
    # Convert both dates
    date1_obj = _to_date(date1)
    date2_obj = _to_date(date2)
    
    # Calculate and return absolute number of days
    return abs((date2_obj - date1_obj).days)