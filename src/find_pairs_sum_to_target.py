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
    num_count = {}
    unique_pairs = set()

    for num in numbers:
        # Ensure num is a number
        try:
            num = float(num)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid number in input list: {num}")
        
        # Count occurrences of each number
        num_count[num] = num_count.get(num, 0) + 1
        
        # Check if the complement exists
        complement = target - num
        
        # If complement exists in count
        if complement in num_count:
            # Special handling for when num == complement
            if num == complement:
                # Ensure at least 2 of the same number exists
                if num_count[num] > 1:
                    pair = (num, num)
                    unique_pairs.add(pair)
            elif num < complement:  # Avoid duplicate pairs
                pair = (num, complement)
                unique_pairs.add(pair)
    
    # Convert back to integer pairs if all numbers are integer-like
    if all(x.is_integer() for x in [target] + list(num_count.keys())):
        return [tuple(map(int, pair)) for pair in unique_pairs]
    
    return list(unique_pairs)