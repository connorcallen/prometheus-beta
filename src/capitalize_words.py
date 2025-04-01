def capitalize_words(text):
    """
    Capitalize the first letter of each word in a given string.

    Args:
        text (str): The input string to be transformed.

    Returns:
        str: A string with the first letter of each word capitalized.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Split the string into words, capitalize first letter of each, then join back
    return " ".join(word.capitalize() for word in text.split())