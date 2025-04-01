def counting_sort(arr):
    """
    Implement Counting Sort algorithm for sorting an array of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as the input.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    
    Time Complexity: O(n + k), where n is the number of elements and k is the range of input
    Space Complexity: O(n + k)
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check for non-integer elements or negative numbers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Input cannot contain negative numbers")
    
    # Find the maximum element to determine the range
    max_val = max(arr)
    
    # Create counting array to store the count of each unique object
    count = [0] * (max_val + 1)
    
    # Store the count of each element
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of each object
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    # Traverse array from right to maintain stability
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output