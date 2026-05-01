from typing import List
def maxRotateFunction(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    
    total_sum = sum(nums)
    current = 0
    for i, val in enumerate(nums):
        current += i * val
    
    max_val = current
    
    for i in range(n-1, 0, -1):  
        current = current + total_sum - n * nums[i]
        max_val = max(max_val, current)
    
    return max_val