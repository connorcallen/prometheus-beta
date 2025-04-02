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
    for i, char in enumerate(input_string):
        # Skip non-alphanumeric characters
        if not char.isalnum():
            if converted and converted[-1] != '-':
                converted.append('-')
            continue
        
        # Detect transitions between characters
        if i > 0:
            prev_char = input_string[i-1]
            
            # Add hyphen on camelCase or PascalCase transitions
            if ((char.isupper() and prev_char.islower()) or  # camelCase
                (char.isupper() and prev_char.isupper() and 
                 i+1 < len(input_string) and input_string[i+1].islower())):  # Acronym to normal case
                if converted and converted[-1] != '-':
                    converted.append('-')
        
        # Add lowercase character
        converted.append(char.lower())
    
    # Convert snake_case to kebab-case and remove consecutive hyphens
    result = ''.join(converted)
    result = result.replace('_', '-')
    
    while '--' in result:
        result = result.replace('--', '-')
    
    return result.strip('-')