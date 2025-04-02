def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the input list that sum to the target value.

    Args:
        numbers (list): A list of numbers to search for pairs
        target (int): The target sum to find pairs for

    Returns:
        list: A list of unique pairs (as tuples) that sum to the target

    Raises:
        TypeError: If input is not a list or if target is not a number
        ValueError: If numbers cannot be converted to numeric type
    """
    # Validate input types
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a numeric value")

    # Convert to a set for O(1) lookup and remove duplicates
    num_set = set()
    unique_pairs = set()

    for num in numbers:
        # Ensure num is a number
        try:
            num = float(num)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid number in input list: {num}")
        
        # Check if the complement exists
        complement = target - num
        
        # If complement exists and is different from current number
        if complement in num_set and num != complement:
            # Always store the smaller number first to ensure unique pairs
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Add current number to set
        num_set.add(num)
    
    # Convert back to integer pairs if all numbers are integer-like
    if all(x.is_integer() for x in [target] + list(num_set)):
        return [tuple(map(int, pair)) for pair in unique_pairs]
    
    return list(unique_pairs)