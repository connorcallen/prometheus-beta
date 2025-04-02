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
    num_count = {}
    unique_pairs = set()

    for num in numbers:
        complement = target - num
        
        # If complement exists
        if complement in num_count:
            # Check for duplicates or unique pairs
            if num != complement or num_count.get(num, 0) > 1:
                pair = tuple(sorted((num, complement)))
                unique_pairs.add(pair)
        
        # Update number count
        num_count[num] = num_count.get(num, 0) + 1
    
    # Convert back to integer pairs if possible
    if all(x.is_integer() for x in [target] + list(num_count.keys())):
        return [tuple(map(int, pair)) for pair in unique_pairs]
    
    return list(unique_pairs)