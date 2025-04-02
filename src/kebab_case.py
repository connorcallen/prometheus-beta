def to_kebab_case(input_string: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Handles various input formats including camelCase, snake_case, 
    PascalCase, and spaces. Removes special characters and converts 
    to lowercase.
    
    Args:
        input_string (str): The input string to convert to kebab-case
    
    Returns:
        str: The input string converted to kebab-case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("camelCase")
        'camel-case'
        >>> to_kebab_case("PascalCase")
        'pascal-case'
        >>> to_kebab_case("snake_case")
        'snake-case'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to lowercase and replace various separators
    converted = []
    prev_char_type = None
    for i, char in enumerate(input_string):
        if not char.isalnum():
            # Replace non-alphanumeric characters with hyphen
            if converted and converted[-1] != '-':
                converted.append('-')
            continue
        
        # Handle consecutive capital letters and transitions
        curr_char_type = 'upper' if char.isupper() else 'lower'
        if (i > 0 and 
            ((curr_char_type == 'upper' and prev_char_type == 'lower') or  # camelCase transition
             (char.isupper() and prev_char_type == 'upper'))):  # UPPERCASE sequence
            if converted and converted[-1] != '-':
                converted.append('-')
        
        # Add lowercase character
        converted.append(char.lower())
        prev_char_type = curr_char_type
    
    # Convert snake_case and handle special characters
    result = ''.join(converted)
    result = result.replace('_', '-')
    
    # Remove consecutive hyphens and strip leading/trailing hyphens
    while '--' in result:
        result = result.replace('--', '-')
    
    return result.strip('-')