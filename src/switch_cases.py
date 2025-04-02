def switch_cases(str1: str, str2: str) -> str:
    """
    Take two strings and return a new string with swapped character cases.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: A new string where characters from str1 have their case swapped
    
    Raises:
        TypeError: If either input is not a string
    
    Examples:
        >>> switch_cases('Hello', 'World')
        'hELLO'
        >>> switch_cases('PyTHON', 'code')
        'pYthon'
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    # If str1 is empty, return an empty string
    if not str1:
        return ''
    
    # Swap the case of characters in str1
    return ''.join(
        char.lower() if char.isupper() else char.upper() 
        for char in str1
    )