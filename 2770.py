from typing import List
def maximumJumps(self, nums: List[int], target: int) -> int:
    n = len(nums)

    dp = [-float('inf')] * n
    dp[0] = 0  

    for i in range(n):
        if dp[i] == -float('inf'):
            continue  
        
        for j in range(i + 1, n):
            if abs(nums[j] - nums[i]) <= target:
                dp[j] = max(dp[j], dp[i] + 1)

    return dp[n-1] if dp[n-1] != -float('inf') else -1    