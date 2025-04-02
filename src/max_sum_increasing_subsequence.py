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
    
    # Maximum sums tracking ALL possible subsequences
    dp = nums.copy()
    
    # Global maximum tracker
    overall_max = dp[0]
    
    for i in range(1, len(nums)):
        # Consider ALL previous subsequences
        for j in range(i):
            # Key condition: only extend if strictly increasing
            if nums[i] > nums[j]:
                # Update potential subsequence sums
                current_sum = dp[j] + nums[i]
                dp[i] = max(dp[i], current_sum)
        
        # Update global maximum
        overall_max = max(overall_max, dp[i])
    
    return overall_max