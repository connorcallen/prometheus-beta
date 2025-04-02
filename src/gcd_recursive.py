def recursive_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using recursion.
    
    This implementation uses the Euclidean algorithm recursively:
    - If b is 0, a is the GCD
    - Otherwise, recursively calculate GCD(b, a % b)
    
    Args:
        a (int): First integer (absolute value will be used)
        b (int): Second integer (absolute value will be used)
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        TypeError: If inputs are not integers
        ValueError: If both inputs are 0
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # Check for zero inputs
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined when both inputs are 0")
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a % b)
    return recursive_gcd(b, a % b)