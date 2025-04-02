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

    # Convert to a list of floats
    try:
        numbers = [float(num) for num in numbers]
    except (TypeError, ValueError):
        raise ValueError("Invalid number in input list")

    # Track pairs and numbers
    num_set = set()
    unique_pairs = set()

    for num in numbers:
        complement = target - num
        
        # If complement is in the set, we found a pair
        if complement in num_set:
            # Ensure unique pairs and avoid duplicates
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Add current number to the set
        num_set.add(num)
    
    # Convert back to integer pairs if possible
    if all(x.is_integer() for x in [target] + list(num_set)):
        return [tuple(map(int, pair)) for pair in unique_pairs]
    
    return list(unique_pairs)