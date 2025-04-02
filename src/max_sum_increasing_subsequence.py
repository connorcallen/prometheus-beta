from typing import List
import bisect

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
    
    # Stores the maximum sum of increasing subsequence for each length
    max_sums = [nums[0]]
    # Stores the corresponding elements that achieve these sums
    subsequence = [nums[0]]
    
    for num in nums[1:]:
        # If current number is greater than the last in subsequence
        if num > subsequence[-1]:
            max_sums.append(max_sums[-1] + num)
            subsequence.append(num)
        else:
            # Find the right position to insert/replace to maintain increasing subsequence
            index = bisect.bisect_left(subsequence, num)
            subsequence[index] = num
            
            # Update max_sums for that index
            if index == 0:
                max_sums[index] = num
            else:
                max_sums[index] = max_sums[index-1] + num
    
    return max(max_sums)