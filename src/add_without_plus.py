def add_without_plus(a, b):
    """
    Add two integers without using the + operator.
    
    This function uses bitwise operations to perform addition:
    - XOR (^) handles addition without carry
    - AND (&) and left shift (<<) handle carry bits
    
    Args:
        a (int): First integer to add
        b (int): Second integer to add
    
    Returns:
        int: Sum of a and b
    
    Raises:
        TypeError: If inputs are not integers
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Handle addition using bitwise operations
    while b != 0:
        # Carry contains common set bits of a and b
        carry = a & b
        
        # Sum of bits of a and b where at least one bit is not set
        a = a ^ b
        
        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry << 1
    
    return a