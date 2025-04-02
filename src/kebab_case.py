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
    i = 0
    while i < len(input_string):
        char = input_string[i]
        
        # Skip non-alphanumeric characters
        if not char.isalnum():
            if converted and converted[-1] != '-':
                converted.append('-')
            i += 1
            continue
        
        # Handle consecutive uppercase (like HTTP)
        if char.isupper():
            # Look ahead to see if it's an acronym
            j = i
            while j < len(input_string) and input_string[j].isupper():
                j += 1
            
            # If it's an acronym (multiple consecutive uppercase)
            if j > i + 1:
                # Add the entire uppercase sequence as lowercase
                converted.append(input_string[i:j].lower())
                i = j
                # Add a hyphen if needed
                if i < len(input_string) and converted and converted[-1] != '-':
                    converted.append('-')
                continue
        
        # Handle typical case and camelCase/PascalCase transitions
        if (i > 0 and 
            ((char.isupper() and not input_string[i-1].isupper()) or  # start of new word
             (char.isupper() and i+1 < len(input_string) and input_string[i+1].islower()))):  # camelCase or PascalCase
            if converted and converted[-1] != '-':
                converted.append('-')
        
        # Add lowercase character
        converted.append(char.lower())
        i += 1
    
    # Convert snake_case and handle special characters
    result = ''.join(converted)
    result = result.replace('_', '-')
    
    # Remove consecutive hyphens and strip leading/trailing hyphens
    while '--' in result:
        result = result.replace('--', '-')
    
    return result.strip('-')