from typing import List
def stoneGameII(self, piles: List[int]) -> int:
    n = len(piles)
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + piles[i]
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for m in range(1, n + 1):
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                stones_taken = suffix_sum[i] - suffix_sum[i + x]
                remaining = suffix_sum[i + x]
                total = stones_taken + (remaining - dp[i + x][max(m, x)])
                dp[i][m] = max(dp[i][m], total)
    
    return dp[0][1]    