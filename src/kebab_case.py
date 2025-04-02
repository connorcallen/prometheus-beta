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
    # First, insert hyphen before capital letters
    converted = ''
    for i, char in enumerate(input_string):
        # Add hyphen before capital letters, except for the first character
        if i > 0 and char.isupper():
            converted += '-'
        
        # Convert to lowercase and handle non-alphanumeric characters
        if char.isalnum():
            converted += char.lower()
        elif char.isspace():
            converted += '-'
    
    # Remove consecutive hyphens and strip leading/trailing hyphens
    while '--' in converted:
        converted = converted.replace('--', '-')
    
    return converted.strip('-')