from typing import List 
from math import gcd
def subsequencePairCount(self, nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    MAX_VAL = 200

    dp = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]
    dp[0][0] = 1
    
    for num in nums:
        new_dp = [row[:] for row in dp]
        
        for g1 in range(MAX_VAL + 1):
            for g2 in range(MAX_VAL + 1):
                if dp[g1][g2] == 0:
                    continue

                new_g1 = gcd(g1, num) if g1 != 0 else num
                if new_g1 <= MAX_VAL:
                    new_dp[new_g1][g2] = (new_dp[new_g1][g2] + dp[g1][g2]) % MOD

                new_g2 = gcd(g2, num) if g2 != 0 else num
                if new_g2 <= MAX_VAL:
                    new_dp[g1][new_g2] = (new_dp[g1][new_g2] + dp[g1][g2]) % MOD
        
        dp = new_dp

    answer = sum(dp[g][g] for g in range(1, MAX_VAL + 1)) % MOD
    return answer        