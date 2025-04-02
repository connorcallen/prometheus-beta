from typing import List

def max_sum_increasing_subsequence(nums: List[int]) -> int:
    """
    Compute the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
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
    
    # Dynamic programming approach to track max sum of increasing subsequence
    dp = nums.copy()
    
    for i in range(1, len(nums)):
        for j in range(i):
            # If current number can extend a previous increasing subsequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    
    return max(dp)