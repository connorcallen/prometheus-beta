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
    
    # Initialize Fibonacci sequence variables
    fib_numbers = [0, 1]
    
    # Generate Fibonacci sequence up to n numbers
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    
    # Return the sum of first n Fibonacci numbers
    return sum(fib_numbers[:n])