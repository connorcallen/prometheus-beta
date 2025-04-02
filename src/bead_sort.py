def bead_sort(arr):
    """
    Implement the Bead Sort (Gravity Sort) algorithm for positive integers.
    
    Bead Sort is a natural sorting algorithm that works like an abacus or beads 
    on parallel rods affected by gravity. It only works for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers or non-integer values.
    """
    # Validate input
    if not arr:
        return []
    
    # Check for negative numbers or non-integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # Handle single element case
    if len(arr) == 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of 'rods'
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[1 if x >= i+1 else 0 for x in arr] for i in range(max_num)]
    
    # Simulate gravity by counting beads in each column
    sorted_arr = []
    for j in range(len(arr)):
        # Count beads in this 'rod'
        col_sum = sum(row[j] for row in beads)
        sorted_arr.append(col_sum)
    
    # Sort the results to get the final sorted list
    return sorted(sorted_arr)