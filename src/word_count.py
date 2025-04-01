def count_words(text: str) -> int:
    """
    Count the number of words in a given string.

    A word is defined as a sequence of non-whitespace characters.
    
    Args:
        text (str): The input string to count words in.
    
    Returns:
        int: The number of words in the string.
    
    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("  Spaces   around   words  ")
        2
        >>> count_words("")
        0
        >>> count_words("   ")
        0
    """
    # Handle None or non-string input
    if text is None:
        return 0
    
    # Convert to string to handle potential non-string inputs
    text_str = str(text).strip()
    
    # If string is empty after stripping, return 0
    if not text_str:
        return 0
    
    # Split by whitespace and count non-empty elements
    return len([word for word in text_str.split() if word])