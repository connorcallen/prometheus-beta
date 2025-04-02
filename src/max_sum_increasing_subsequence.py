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
    
    # Maximum sums of subsequences
    dp = nums.copy()
    
    global_max = dp[0]
    
    for i in range(1, len(nums)):
        for j in range(i):
            # If current number can extend a strictly increasing subsequence
            if nums[i] > nums[j]:
                # Update current maximum with potential larger subsequence
                dp[i] = max(dp[i], dp[j] + nums[i])
        
        # Track global maximum for all subsequences
        global_max = max(global_max, dp[i])
    
    return global_max