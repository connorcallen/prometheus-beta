def fibonacci_sequence_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci 
                 sequence elements to sum.
    
    Returns:
        int: The sum of the first n numbers in the Fibonacci sequence.
    
    Raises:
        ValueError: If the input is not a positive integer.
    
    Examples:
        >>> fibonacci_sequence_sum(1)
        0
        >>> fibonacci_sequence_sum(2)
        1
        >>> fibonacci_sequence_sum(5)
        7
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle small n cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Initialize Fibonacci sequence variables
    a, b = 0, 1
    sequence_sum = a + b
    
    # Calculate sum of first n Fibonacci numbers
    for _ in range(3, n + 1):
        a, b = b, a + b
        sequence_sum += b
    
    return sequence_sum