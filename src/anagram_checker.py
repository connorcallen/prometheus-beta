import unicodedata

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. Comparison is case-insensitive 
    and ignores whitespace.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If either input is not a string
    """
    # Check input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Normalize unicode characters and remove accents
    def normalize(s: str) -> str:
        # Decompose characters, remove accents, convert to lowercase, remove whitespace
        return ''.join(
            char for char in unicodedata.normalize('NFKD', s.lower())
            if not unicodedata.combining(char)
        ).replace(' ', '')
    
    # Normalize and compare
    cleaned_str1 = normalize(str1)
    cleaned_str2 = normalize(str2)
    
    # Quick length check
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies
    for char in cleaned_str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in cleaned_str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2