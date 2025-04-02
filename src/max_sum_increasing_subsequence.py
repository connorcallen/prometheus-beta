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
    
    # Dynamic programming array to track max sums
    max_sums = nums.copy()
    
    for i in range(1, len(nums)):
        for j in range(i):
            # If current number extends strictly increasing subsequence
            if nums[i] > nums[j]:
                # Update max possible sum for current subsequence
                max_sums[i] = max(max_sums[i], max_sums[j] + nums[i])
    
    return max(max_sums)