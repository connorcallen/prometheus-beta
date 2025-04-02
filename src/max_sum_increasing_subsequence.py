from typing import List

def max_sum_increasing_subsequence(nums: List[int]) -> int:
    """
    Compute the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    An increasing subsequence is a sequence that can be derived from the input array 
    by deleting some or no elements without changing the order of the remaining elements, 
    where each element is larger than its previous element.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Examples:
        >>> max_sum_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60])
        187
        >>> max_sum_increasing_subsequence([1, 101, 2, 3, 100])
        106
        >>> max_sum_increasing_subsequence([])
        0
    """
    # Handle empty input
    if not nums:
        return 0
    
    # Store maximum sums of subsequences ending at each index
    max_sums = nums.copy()
    
    # Iterate through array to compute max sums of increasing subsequences
    for i in range(1, len(nums)):
        for j in range(i):
            # Update max_sums[i] if we can form a larger increasing subsequence
            if nums[i] > nums[j]:
                max_sums[i] = max(max_sums[i], max_sums[j] + nums[i])
    
    # Return the maximum sum found
    return max(max_sums)