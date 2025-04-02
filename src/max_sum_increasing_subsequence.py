from typing import List

def max_sum_increasing_subsequence(nums: List[int]) -> int:
    """
    Compute the maximum sum of an increasing subsequence.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n²)
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
    
    # Track maximum sum for subsequences
    dp = nums.copy()
    
    # Track absolute maximum
    max_subsequence_sum = dp[0]
    
    for i in range(1, len(nums)):
        # Consider every previous element to form increasing subsequence
        for j in range(i):
            # Check if we can extend an existing subsequence
            if nums[i] > nums[j]:
                # Compute potential maximum sum
                potential_sum = dp[j] + nums[i]
                dp[i] = max(dp[i], potential_sum)
        
        # Update global maximum
        max_subsequence_sum = max(max_subsequence_sum, dp[i])
    
    return max_subsequence_sum