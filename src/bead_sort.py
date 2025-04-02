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
    
    # Find the maximum number to determine the number of 'rods'
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[1 if n >= k+1 else 0 for n in arr] for k in range(max_num)]
    
    # 'Drop' the beads (simulate gravity)
    for i in range(max_num):
        # Count beads in each column
        col_sum = sum(row[i] for row in beads)
        
        # Redistribute beads from bottom to top
        for j in range(len(arr)):
            beads[i][j] = 1 if col_sum > j else 0
    
    # Reconstruct the sorted array
    return [sum(row) for row in zip(*beads)]